Các file trên đã có mã nguồn app chuyển đổi những kỹ tự thường thành mã hóa base 64 
QR để tạo có thẻ truy cập https://ducphuocprofilecvweb.netlify.app/link2qr


1. Yêu Cầu Hệ Thống





Hệ điều hành: Windows 7/8/10/11.



Phần cứng:





Camera (nếu sử dụng tính năng quét mã QR).



Kết nối internet (để gửi thông báo qua Discord và điều khiển từ xa).



Quyền truy cập: Chạy phần mềm với quyền quản trị viên (Administrator) để đảm bảo hoạt động đầy đủ.

2. Cài Đặt Phần Mềm





Tải và giải nén:





Tải file .exe và thư mục cấu hình từ nhà cung cấp.



Giải nén thư mục (nếu có) vào một vị trí cố định, ví dụ: C:\PhanMemGiamSat.



Kiểm tra file cấu hình:





Trong thư mục phần mềm, đảm bảo có các file:





webhook.txt: Chứa URL Discord Webhook để gửi thông báo.



exe_list.txt: Danh sách ứng dụng bị cấm (đã mã hóa).



website_list.txt: Danh sách trang web bị cấm (đã mã hóa).



password.txt: Danh sách mật khẩu (mặc định: 12345678).



admin_password.txt: Mật khẩu quản trị viên (mặc định: admin123).



bot_token.txt: Token của Discord Bot để điều khiển từ xa.



Liên hệ nhà cung cấp nếu thiếu file hoặc cần hỗ trợ chỉnh sửa.



Chạy phần mềm:





Nhấp đúp vào file .exe để khởi động.



Nếu được yêu cầu, chọn "Run as Administrator" để đảm bảo phần mềm hoạt động đúng.

3. Cách Sử Dụng

3.1. Khởi động và giám sát





Sau khi chạy file .exe, phần mềm sẽ tự động giám sát các ứng dụng và trang web được liệt kê trong exe_list.txt và website_list.txt.



Nếu mở một ứng dụng hoặc trang web bị cấm, phần mềm sẽ:





Đóng ứng dụng/trang web ngay lập tức.



Hiển thị màn hình cảnh báo màu đỏ toàn màn hình với thông báo lý do (ví dụ: "Ứng dụng bị cấm: [tên ứng dụng]" hoặc "Trang web bị cấm: [tên trang web]").



Gửi thông báo đến kênh Discord được cấu hình.

3.2. Mở khóa màn hình cảnh báo

Khi màn hình cảnh báo xuất hiện, bạn có thể mở khóa bằng một trong hai cách:

a. Nhập mật khẩu





Nhập mật khẩu 8 chữ số vào ô nhập liệu.





Chỉ nhập số, không nhập chữ hoặc ký tự đặc biệt.



Nếu nhập quá 8 số, phần mềm sẽ tự động cắt bớt.



Nhấn nút Xác nhận hoặc đợi sau khi nhập đủ 8 số.



Nếu mật khẩu đúng (mặc định: 12345678 hoặc mật khẩu được cung cấp), màn hình sẽ mở khóa và phần mềm tiếp tục giám sát.



Nếu sai, thông báo lỗi sẽ hiển thị.

b. Quét mã QR





Nhấn nút Quét QR để kích hoạt camera.



Đưa mã QR chứa mật khẩu (do nhà cung cấp cung cấp) trước camera.



Nếu mã QR hợp lệ, màn hình sẽ tự động mở khóa.



Nhấn lại nút Quét QR để tắt camera nếu không cần sử dụng.

3.3. Điều khiển từ xa qua Discord

Phần mềm hỗ trợ điều khiển từ xa thông qua Discord Bot. Để sử dụng:





Thêm bot vào server Discord của bạn bằng token trong bot_token.txt (liên hệ nhà cung cấp nếu cần hướng dẫn).



Sử dụng các lệnh sau trong kênh Discord:





!unlock <mật khẩu>: Mở khóa màn hình cảnh báo.





Ví dụ: !unlock 12345678 hoặc !unlock admin123.



!unlock30p: Tạm dừng giám sát trong 30 phút (chỉ hoạt động khi không có màn hình cảnh báo).



!unlock1h: Tạm dừng giám sát trong 1 giờ (chỉ hoạt động khi không có màn hình cảnh báo).



!locknow: Hủy trạng thái tạm dừng và tiếp tục giám sát ngay lập tức.

3.4. Tắt máy





Trên màn hình cảnh báo, nhấn nút Tắt máy để tắt máy tính ngay lập tức.



Lưu ý: Hành động này không thể hoàn tác, hãy đảm bảo lưu dữ liệu trước khi thực hiện.

4. Các Tính Năng Nổi Bật





Khóa phím tắt: Các phím như Alt, F4, Tab, Esc, Win bị chặn khi màn hình cảnh báo xuất hiện để ngăn thoát chương trình.



Thông báo qua Discord: Mỗi hành động (đóng ứng dụng/trang cấm, mở khóa, tạm dừng) được gửi qua Discord Webhook.



Tự động khởi động lại: Nếu gặp lỗi, phần mềm sẽ tự động khởi động lại để đảm bảo hoạt động liên tục.

5. Lưu Ý Quan Trọng





Camera: Đảm bảo máy tính có camera hoạt động nếu sử dụng tính năng quét mã QR.



File cấu hình: Không chỉnh sửa các file cấu hình trừ khi được hướng dẫn bởi nhà cung cấp, vì có thể gây lỗi.



Quyền quản trị: Luôn chạy phần mềm với quyền quản trị viên để đảm bảo đóng ứng dụng/trang web cấm thành công.



Dừng phần mềm: Để dừng phần mềm, sử dụng Task Manager (Ctrl+Shift+Esc) và tắt tiến trình liên quan đến file .exe.



Mật khẩu mặc định: Nếu không được cung cấp mật khẩu riêng, sử dụng 12345678 hoặc liên hệ nhà cung cấp.

6. Xử Lý Sự Cố





Màn hình cảnh báo không mở khóa:





Kiểm tra mật khẩu hoặc mã QR.



Sử dụng lệnh !unlock qua Discord.



Camera không hoạt động:





Kiểm tra camera có được kết nối và cấp quyền.



Đảm bảo ánh sáng đủ để quét mã QR.



Không nhận thông báo Discord:





Kiểm tra URL trong webhook.txt và kết nối internet.



Đảm bảo bot Discord đang hoạt động (kiểm tra bot_token.txt).



Phần mềm không chạy:





Chạy lại với quyền quản trị viên.



Kiểm tra các file cấu hình có tồn tại và đúng định dạng.



Liên hệ nhà cung cấp nếu lỗi vẫn xảy ra.

7. Liên Hệ Hỗ Trợ

Nếu gặp vấn đề hoặc cần hỗ trợ thêm, vui lòng liên hệ nhà cung cấp phần mềm qua:





Email: [Thêm email nhà cung cấp].
