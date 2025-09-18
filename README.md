# PhanCumAnh
Bài toán phân cụm ảnh nhằm nhóm các ảnh có đặc điểm tương đồng vào cùng một cụm mà không cần nhãn. Ứng dụng trong quản lý ảnh, tìm kiếm ảnh tương tự, tiền xử lý dữ liệu và hỗ trợ các bài toán thị giác máy tính khác.

│── data/
│ ├── car1.jpg
│ ├── car2.jpg
│ ├── cargray.jpg
│ └── manycar.jpg
│── main.py
│── README.md


---

🚀 Cách chạy
Cài đặt thư viện cần thiết
```bash
pip install opencv-python pillow scikit-learn numpy

Chạy ứng dụng
python app.py

🖼️ Tính năng

Chọn ảnh từ máy bằng nút Chọn ảnh.

Chọn ảnh từ folder data/ bằng combobox.

Chọn số cụm K (mặc định = 3).

Chế độ ảnh xám hoặc ảnh màu.

Dùng KMeans thủ công (tự cài đặt) hoặc KMeans của sklearn.

Hiển thị kết quả ảnh sau khi phân cụm trực tiếp trên GUI.

🛠️ Công nghệ sử dụng

Python 3.x

OpenCV (cv2) → đọc/tiền xử lý ảnh

NumPy → tính toán ma trận

Scikit-learn → thuật toán KMeans

Tkinter → giao diện GUI

Pillow (PIL) → hiển thị ảnh trên Tkinter

📌 Ví dụ kết quả

Ảnh đầu vào: car1.jpg
Số cụm K = 3
Kết quả: ảnh được phân đoạn thành 3 vùng màu chính.


whatsaname_1
