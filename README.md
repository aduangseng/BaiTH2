1. Bài làm về gì

Bài làm xây dựng một ứng dụng web tra cứu thông tin thời tiết sử dụng Python Flask làm backend và Google Firestore làm cơ sở dữ liệu.
Ứng dụng cho phép người dùng:

Lọc theo thời gian để tìm kiếm thông tin thời tiết.

Hiển thị kết quả trực tiếp trên cùng trang.

Thông báo nếu không tìm thấy dữ liệu.

Mục tiêu chính:

Luyện tập kết nối Flask với Firestore.

Xây dựng giao diện tìm kiếm và hiển thị dữ liệu.

Thực hành thao tác CRUD cơ bản với dữ liệu thời tiết.

2. Sử dụng công nghệ, thuật toán, ngôn ngữ lập trình 
🔹 Ngôn ngữ lập trình
Python 3.8+ (xử lý logic backend).

HTML/Jinja2 (hiển thị dữ liệu trên frontend).

🔹 Công nghệ & thư viện
Flask: Framework web Python nhẹ và linh hoạt.

Firebase Admin SDK: Kết nối và thao tác với Google Firestore.

Google Firestore: Lưu trữ dữ liệu thời tiết (NoSQL Database).

Bootstrap/CSS (tùy chọn): Tạo giao diện đẹp và responsive.

🔹 Thuật toán & xử lý
Truy vấn dữ liệu theo điều kiện:

Tìm kiếm bản ghi theo ID.

Xử lý dữ liệu JSON từ Firestore và render sang HTML.

Điều kiện logic: Kiểm tra doc.exists để báo “Không tìm thấy dữ liệu” nếu không có kết quả.

3. Một số giao diện cơ bản 
- 🖼 Giao diện nhập và lưu thông tin thời tiết.
- <img width="567" height="670" alt="image" src="https://github.com/user-attachments/assets/aec3ac49-76fb-426e-9c4e-764d2849c322"/>
- 🖼 Giao diện tìm kiếm thời tiết (Người dùng tìm kiếm thông tin bằng cách lọc theo thời gian)
<img width="957" height="442" alt="image" src="https://github.com/user-attachments/assets/028f9eff-0482-4e86-8457-863a53416ea9" />







