import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm KMeans thủ công
def my_kmeans(pixels, k, max_iters=10):
    n_samples, n_features = pixels.shape
    random_idx = np.random.choice(n_samples, k, replace=False)
    centroids = pixels[random_idx]

    for _ in range(max_iters):
        distances = np.linalg.norm(pixels[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([
            pixels[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids

    return labels, centroids

# Hàm xử lý ảnh
def Xu_ly_anh(img_path, k, is_gray=False, use_custom=False):
    image = cv2.imread(img_path)
    if image is None:
        print("Không thể đọc ảnh. Hãy kiểm tra đường dẫn.")
        return None

    if is_gray:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixel_values = image.reshape((-1, 1 if is_gray else 3))
    pixel_values = np.float32(pixel_values)

    if use_custom:
        labels, centers = my_kmeans(pixel_values, k)
    else:
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
        kmeans.fit(pixel_values)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_

    segmented_image = centers[labels].reshape(image.shape)
    segmented_image = np.uint8(segmented_image)

    return segmented_image

# Chọn ảnh
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

# Xử lý ảnh
def process_image():
    img_path = entry_path.get()
    try:
        k = int(entry_k.get())
        if k < 1 or k > 100:
            raise ValueError("K nên nằm trong khoảng 1 đến 100.")
    except ValueError as e:
        print("Lỗi:", e)
        return

    is_gray = var_gray.get()
    use_custom = var_custom.get()

    kq = Xu_ly_anh(img_path, k, is_gray, use_custom)
    if kq is not None:
        display_image(kq)

# Hiển thị ảnh
def display_image(image):
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    label_image.config(image=image)
    label_image.image = image

# Giao diện tkinter
root = tk.Tk()
root.title("Xử lý ảnh với K-Means")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_select = tk.Button(frame, text="Chọn ảnh", command=select_image)
btn_select.grid(row=0, column=0, padx=5)

entry_path = tk.Entry(frame, width=40)
entry_path.grid(row=0, column=1, padx=5)

label_k = tk.Label(frame, text="Số cụm K:")
label_k.grid(row=1, column=0, padx=5)

entry_k = tk.Entry(frame, width=5)
entry_k.grid(row=1, column=1, padx=5)
entry_k.insert(0, "3")  # Giá trị mặc định

var_gray = tk.BooleanVar()
chk_gray = tk.Checkbutton(frame, text="Ảnh xám", variable=var_gray)
chk_gray.grid(row=2, column=0, columnspan=2)

var_custom = tk.BooleanVar()
chk_custom = tk.Checkbutton(frame, text="Dùng KMeans thủ công", variable=var_custom)
chk_custom.grid(row=3, column=0, columnspan=2)

btn_process = tk.Button(frame, text="Xử lý ảnh", command=process_image)
btn_process.grid(row=4, column=0, columnspan=2, pady=10)

label_image = tk.Label(root)
label_image.pack()

root.mainloop()
