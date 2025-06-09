import tkinter as tk
import base64

def encode_to_base64():
    # Lấy chuỗi từ ô nhập
    input_string = input_entry.get()
    # Mã hóa thành Base64
    byte_string = input_string.encode('utf-8')
    base64_bytes = base64.b64encode(byte_string)
    base64_string = base64_bytes.decode('utf-8')
    # Hiển thị kết quả
    output_text.delete(1.0, tk.END)  # Xóa nội dung cũ
    output_text.insert(tk.END, base64_string)  # Chèn nội dung mới

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Mã Hóa Base64")

# Tạo khung nhập liệu
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Nhãn và ô nhập
input_label = tk.Label(input_frame, text="Nhập ký tự:")
input_label.pack()

input_entry = tk.Entry(input_frame, width=30)
input_entry.pack()

# Nút mã hóa
encode_button = tk.Button(input_frame, text="Mã Hóa", command=encode_to_base64)
encode_button.pack(pady=10)

# Tạo khung hiển thị kết quả
output_frame = tk.Frame(root)
output_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Text widget hiển thị kết quả
output_text = tk.Text(output_frame, width=30, height=10, bg="lightgrey")
output_text.pack()

# Chạy vòng lặp chính
root.mainloop()