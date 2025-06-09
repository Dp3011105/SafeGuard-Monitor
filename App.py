import threading
import time
import psutil
import requests
import tkinter as tk
from tkinter import messagebox
import keyboard
import os
import sys
import pygetwindow as gw
from discord_webhook import DiscordWebhook
import discord
from discord.ext import commands

# =========================
# CẤU HÌNH ĐƯỜNG DẪN FILE
# =========================
WEBHOOK_FILE = "webhook.txt"
EXE_FILE = "exe_list.txt"
WEBSITE_FILE = "website_list.txt"
PASSWORD_FILE = "password.txt"
ADMIN_PASSWORD_FILE = "admin_password.txt"
BOT_TOKEN_FILE = "bot_token.txt"

# =========================
# HÀM HỖ TRỢ
# =========================
def read_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ Không tìm thấy file: {file_path}")
        return []

def send_discord_message(message):
    if webhook_url:
        try:
            webhook = DiscordWebhook(url=webhook_url, content=message)
            webhook.execute()
        except Exception as e:
            print(f"❌ Lỗi gửi Discord webhook: {e}")

def restart_program():
    print("🔁 Khởi động lại chương trình...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

# =========================
# ĐỌC CẤU HÌNH
# =========================
webhook_url = read_config(WEBHOOK_FILE)[0] if read_config(WEBHOOK_FILE) else ""
exe_list = read_config(EXE_FILE)
website_list = read_config(WEBSITE_FILE)
password_chars = read_config(PASSWORD_FILE)
admin_password = read_config(ADMIN_PASSWORD_FILE)[0] if read_config(ADMIN_PASSWORD_FILE) else "admin123"
bot_token = read_config(BOT_TOKEN_FILE)[0] if read_config(BOT_TOKEN_FILE) else ""

# =========================
# BIẾN TOÀN CỤC
# =========================
unlock_flag = False
current_warning_screen = None
monitoring_active = True
BLOCKED_KEYS = ['alt', 'f4', 'tab', 'esc', 'win']

pause_duration = 0  # Thời gian tạm dừng còn lại (giây)
pause_active = False
pause_lock = threading.Lock()

# =========================
# ĐÓNG ỨNG DỤNG/TRANG BỊ CẤM
# =========================
def close_forbidden_apps():
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            proc_name = proc.info['name'].lower()
            if any(exe.lower() in proc_name for exe in exe_list):
                proc.kill()
                send_discord_message(f"🚫 Đóng ứng dụng cấm: {proc_name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    try:
        windows = gw.getAllTitles()
        for title in windows:
            lower_title = title.lower()
            for website in website_list:
                if website.lower() in lower_title:
                    for win in gw.getWindowsWithTitle(title):
                        win.close()
                        send_discord_message(f"🌐 Đóng tab cấm: {title}")
                        break
    except Exception as e:
        print(f"Lỗi khi kiểm tra cửa sổ: {e}")

# =========================
# GIAO DIỆN CẢNH BÁO (Updated to stay on top)
# =========================
class WarningScreen:
    def __init__(self, reason):
        global current_warning_screen
        self.reason = reason
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='red')
        self.root.overrideredirect(True)
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.root.attributes('-topmost', True)  # Make sure it stays on top
        current_warning_screen = self

        for key in BLOCKED_KEYS:
            keyboard.block_key(key)

        tk.Label(self.root, text=f"CẢNH BÁO: {reason}", font=("Arial", 30), bg='red', fg='white').pack(pady=50)
        tk.Label(self.root, text="Nhập mật khẩu hoặc chờ mở khóa từ Discord:", font=("Arial", 20), bg='red', fg='white').pack(pady=20)
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 20))
        self.password_entry.pack(pady=10)
        tk.Button(self.root, text="Xác nhận", command=self.check_password, font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Tắt máy", command=self.shutdown, font=("Arial", 20)).pack(pady=10)
        self.check_unlock_status()

    def check_password(self):
        if self.password_entry.get() in password_chars:
            self.perform_unlock()
        else:
            messagebox.showerror("Lỗi", "Mật khẩu không đúng!")

    def check_unlock_status(self):
        if unlock_flag:
            self.perform_unlock()
        else:
            self.root.after(1000, self.check_unlock_status)

    def perform_unlock(self):
        global unlock_flag, current_warning_screen
        close_forbidden_apps()
        self.root.destroy()
        for key in BLOCKED_KEYS:
            keyboard.unblock_key(key)
        unlock_flag = False
        current_warning_screen = None
        send_discord_message("✅ Đã mở khóa hệ thống")

    def shutdown(self):
        os.system("shutdown /s /t 1")

    def run(self):
        self.root.mainloop()

# =========================
# GIÁM SÁT ỨNG DỤNG
# =========================
def monitor_exe_thread():
    global current_warning_screen
    while monitoring_active:
        # Nếu đang pause thì không giám sát
        with pause_lock:
            if pause_active:
                time.sleep(1)
                continue

        if current_warning_screen is None:
            for proc in psutil.process_iter(['name']):
                try:
                    proc_name = proc.info['name'].lower()
                    if any(exe.lower() in proc_name for exe in exe_list):
                        WarningScreen(f"Ứng dụng bị cấm: {proc_name}").run()
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        time.sleep(1)

def monitor_website_thread():
    import win32gui

    def get_all_window_titles():
        def callback(hwnd, titles):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if title:
                    titles.append(title.lower())
            return True

        titles = []
        win32gui.EnumWindows(callback, titles)
        return titles

    global current_warning_screen
    while monitoring_active:
        with pause_lock:
            if pause_active:
                time.sleep(1)
                continue

        if current_warning_screen is None:
            try:
                titles = get_all_window_titles()
                for title in titles:
                    for website in website_list:
                        if website.lower() in title:
                            WarningScreen(f"Trang web bị cấm: {website}").run()
                            break
            except Exception as e:
                print(f"Lỗi kiểm tra website: {e}")
        time.sleep(1)


# =========================
# THREAD ĐẾM NGƯỢC TẠM DỪNG
# =========================
def pause_timer_thread():
    global pause_duration, pause_active
    while True:
        with pause_lock:
            if pause_active and pause_duration > 0:
                pause_duration -= 1

            if pause_active and pause_duration == 0:
                pause_active = False
                send_discord_message("⏱️ Hết thời gian tạm dừng. Giám sát tiếp tục.")
        time.sleep(1)

# =========================
# DISCORD BOT
# =========================
def discord_bot_thread():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"🤖 Bot đã sẵn sàng: {bot.user.name}")

    @bot.command()
    async def unlock(ctx, *, password=None):  # Make password optional
        global unlock_flag
        if password is None:
            await ctx.send("⚠️ Vui lòng nhập mật khẩu sau lệnh `!unlock` (ví dụ: `!unlock matkhau123`)")
            return
            
        if password in password_chars or password == admin_password:
            unlock_flag = True
            await ctx.send("🔓 Mật khẩu đúng! Đang mở khóa...")
        else:
            await ctx.send("❌ Mật khẩu sai!")

    @bot.command()
    async def unlock30p(ctx):
        global pause_duration, pause_active, current_warning_screen
        
        # Check if warning screen is active
        if current_warning_screen is not None:
            await ctx.send("⚠️ Hệ thống đang bị khóa! Vui lòng mở khóa bằng lệnh `!unlock` trước khi sử dụng lệnh này.")
            return
            
        with pause_lock:
            if pause_active:
                await ctx.send(f"⚠️ Đang trong thời gian tạm dừng. Vui lòng đợi {pause_duration // 60} phút.")
                return
            pause_duration = 30 * 60
            pause_active = True
            await ctx.send("⏸️ Tạm dừng chương trình trong 30 phút.")

    @bot.command()
    async def unlock1h(ctx):
        global pause_duration, pause_active, current_warning_screen
        
        # Check if warning screen is active
        if current_warning_screen is not None:
            await ctx.send("⚠️ Hệ thống đang bị khóa! Vui lòng mở khóa bằng lệnh `!unlock` trước khi sử dụng lệnh này.")
            return
            
        with pause_lock:
            if pause_active:
                await ctx.send(f"⚠️ Đang trong thời gian tạm dừng. Vui lòng đợi {pause_duration // 60} phút.")
                return
            pause_duration = 60 * 60
            pause_active = True
            await ctx.send("⏸️ Tạm dừng chương trình trong 1 giờ.")

    @bot.command()
    async def locknow(ctx):
        global pause_duration, pause_active, current_warning_screen
        
        # Check if warning screen is active
        if current_warning_screen is not None:
            await ctx.send("⚠️ Hệ thống đang bị khóa! Vui lòng mở khóa bằng lệnh `!unlock` trước khi sử dụng lệnh này.")
            return
            
        with pause_lock:
            if pause_active:
                pause_duration = 0
                pause_active = False
                await ctx.send("🔒 Đã dừng tạm dừng và tiếp tục giám sát.")
            else:
                await ctx.send("✅ Giám sát đang hoạt động bình thường.")

    try:
        bot.run(bot_token)
    except Exception as e:
        print(f"❌ Lỗi bot Discord: {e}")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    threading.Thread(target=monitor_exe_thread, daemon=True).start()
    threading.Thread(target=monitor_website_thread, daemon=True).start()
    threading.Thread(target=pause_timer_thread, daemon=True).start()
    if bot_token:
        threading.Thread(target=discord_bot_thread, daemon=True).start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitoring_active = False
        sys.exit(0)
