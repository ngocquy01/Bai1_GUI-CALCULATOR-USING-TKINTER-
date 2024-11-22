import tkinter as tk
from tkinter import messagebox
import math

# Hàm xử lý sự kiện khi nhấn nút
def click(button_text):
    current_expression = entry.get()
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = str(eval(current_expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            messagebox.showerror("Error", "Biểu thức không hợp lệ")
    elif button_text == "√":
        try:
            result = str(math.sqrt(float(current_expression)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Số không hợp lệ cho căn bậc hai")
    elif button_text == "%":
        try:
            result = str(float(current_expression) / 100)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Biểu thức không hợp lệ cho %")
    elif button_text == "DEL":
        entry.delete(len(current_expression) - 1, tk.END)
    elif button_text == "x^2":
        try:
            result = str(float(current_expression) ** 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Biểu thức không hợp lệ cho mũ 2")
    else:
        entry.insert(tk.END, button_text)

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.geometry("405x550")
root.config(bg="white")
root.resizable(0, 0)

# Tạo biến lưu trữ văn bản
entry_var = tk.StringVar()

# Thiết kế hộp nhập và hiển thị kết quả
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 33), justify='right', bd=10, insertwidth=2, bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Các nút trên máy tính
buttons = [
    '', '', 'C', 'DEL',
    '√', 'x^2', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '(','0', ')', '='
]

# Tạo các nút và thêm vào lưới
row_val = 1
col_val = 0

for button_text in buttons:
    if button_text:
        # Bỏ qua các nút trống
        color = "white"  # Màu trắng mặc định cho các nút
        if button_text == "=":
            color = "green"  # Màu xanh lá cho nút "="
        elif button_text in {'+', '-', '*', '/', 'DEL', '√', '%', '(', ')', 'x^2'}:
            color = "gray70"  # Màu xám cho các nút chức năng
        elif button_text == "C":
            color = "red"  # Màu đỏ cho nút "C"

        button = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 14),
                        bg=color, fg="black", relief="raised", command=lambda text=button_text: click(text))
        button.grid(row=row_val, column=col_val, padx=5, pady=5,sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Cho phép các nút co giãn theo chiều dọc và chiều ngang
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

# Chạy ứng dụng
root.mainloop()