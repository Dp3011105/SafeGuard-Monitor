# SafeGuard-Monitor
SafeGuard Monitor là phần mềm giám sát và khóa ứng dụng, trang web bị cấm trên máy tính. Tự động đóng ứng dụng, khóa màn hình cảnh báo yêu cầu mật khẩu hoặc mở khóa từ xa qua Discord Bot. Hỗ trợ tạm dừng giám sát bằng lệnh Discord với thời gian linh hoạt, giúp quản lý hiệu quả và bảo mật cao.


Hướng dẫn sử dụng phần mềm SafeGuard Monitor
1. Cài đặt và chuẩn bị
Chuẩn bị các file cấu hình theo đúng tên và định dạng sau:

webhook.txt: chứa URL webhook Discord để nhận thông báo.

exe_list.txt: danh sách tên các file thực thi (exe) bị cấm, mỗi dòng một tên.

website_list.txt: danh sách từ khóa tên website bị cấm, mỗi dòng một từ khóa.

password.txt: danh sách mật khẩu hợp lệ để mở khóa màn hình.

bot_token.txt: token bot Discord được tạo trên Discord Developer Portal.

2. Chạy phần mềm
Chạy file Python chính, phần mềm sẽ tự động:

Giám sát các ứng dụng bị cấm chạy trên hệ thống và đóng ngay khi phát hiện.

Giám sát các cửa sổ trình duyệt có chứa website bị cấm và đóng ngay.

Khi phát hiện vi phạm, màn hình cảnh báo toàn màn hình xuất hiện, khóa người dùng, yêu cầu nhập mật khẩu.

Gửi thông báo về Discord qua webhook.

3. Mở khóa màn hình cảnh báo
Có 2 cách mở khóa:

Nhập mật khẩu hợp lệ trên màn hình cảnh báo.

Gửi lệnh Discord thông qua bot:

diff
Sao chép
Chỉnh sửa
!unlock <mật_khẩu>
Ví dụ: !unlock admin123

4. Điều khiển tạm dừng giám sát qua Discord Bot
Bạn có thể gửi các lệnh sau trong kênh Discord mà bot đã được thêm vào:

!unlock30p : Tạm dừng giám sát trong 30 phút.

!unlock1h : Tạm dừng giám sát trong 1 tiếng.

!locknow : Kết thúc ngay thời gian tạm dừng, tiếp tục giám sát.

Lưu ý:

Nếu đang tạm dừng 30 phút mà gửi lệnh tạm dừng 1 tiếng, phần mềm sẽ báo bạn phải đợi hết 30 phút trước.

Tương tự, nếu đang tạm dừng 1 tiếng mà gửi lệnh tạm dừng 30 phút, phần mềm cũng sẽ yêu cầu đợi hết 1 tiếng.

5. Các lưu ý khác
Phần mềm yêu cầu chạy trên Windows để hỗ trợ đóng cửa sổ và xử lý các cửa sổ chương trình.

Phần mềm cần quyền quản trị (Administrator) để đóng các tiến trình và khóa phím hệ thống.

Hãy đảm bảo bot Discord đã được cấp quyền đọc và gửi tin nhắn trong server Discord.
