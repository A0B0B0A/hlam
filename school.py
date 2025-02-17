# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
# import sys

# class DivisibleNumbers(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
    
#     def initUI(self):
#         self.setWindowTitle("Ділення чисел")
#         self.setGeometry(100, 100, 500, 500)
        
#         layout = QVBoxLayout()
        
#         self.label = QLabel("Введіть число:")
#         layout.addWidget(self.label)
        
#         self.inputField = QLineEdit()
#         layout.addWidget(self.inputField)
        
#         self.resultArea = QTextEdit()
#         self.resultArea.setReadOnly(True)
#         layout.addWidget(self.resultArea)
        
#         self.button = QPushButton("Знайти числа")
#         self.button.clicked.connect(self.find_divisible_numbers)
#         layout.addWidget(self.button)
        
#         self.setLayout(layout)
    
#     def find_divisible_numbers(self):
#         try:
#             num = int(self.inputField.text())
#             if num <= 0:
#                 self.resultArea.setText("Введене число повинно бути більше нуля.")
#                 return
            
#             numbers = [str(i) for i in range(1001) if i % num == 0]
#             result_text = "Числа від 0 до 1000, які діляться на {}:\n".format(num) + " ".join(numbers) + f"\nЗнайдено {len(numbers)} чисел."
#             self.resultArea.setText(result_text)
#         except ValueError:
#             self.resultArea.setText("Будь ласка, введіть коректне число.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = DivisibleNumbers()
#     window.show()
#     sys.exit(app.exec_())



import tkinter as tk
from tkinter import messagebox

def find_divisible_numbers():
    try:
        num = int(entry.get())
        if num <= 0:
            messagebox.showerror("Помилка", "Введене число повинно бути більше нуля.")
            return
        
        numbers = [str(i) for i in range(1001) if i % num == 0]
        result_text = "Числа від 0 до 1000, які діляться на {}:\n".format(num) + " ".join(numbers) + f"\nЗнайдено {len(numbers)} чисел."
        result_area.config(state=tk.NORMAL)
        result_area.delete(1.0, tk.END)
        result_area.insert(tk.END, result_text)
        result_area.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректне число.")

# Головне вікно
root = tk.Tk()
root.title("Ділення чисел")
root.geometry("400x300")

tk.Label(root, text="Введіть число:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="Знайти числа", command=find_divisible_numbers)
btn.pack(pady=5)

result_area = tk.Text(root, height=10, state=tk.DISABLED)
result_area.pack(pady=5)

root.mainloop()
