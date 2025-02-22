from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
import sys

def process_array(numbers):
    if not numbers:
        return "Масив порожній"
    
    max_value = max(numbers)
    min_value = min(numbers)
    avg_value = sum(numbers) / len(numbers)
    
    return f"Максимальне: {max_value}\nМінімальне: {min_value}\nСереднє арифметичне: {avg_value:.2f}"

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Обробка масиву")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Введіть числа через пробіл:")
        layout.addWidget(self.label)
        
        self.inputField = QLineEdit()
        layout.addWidget(self.inputField)
        
        self.resultArea = QTextEdit()
        self.resultArea.setReadOnly(True)
        layout.addWidget(self.resultArea)
        
        self.button = QPushButton("Обчислити")
        self.button.clicked.connect(self.calculate)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def calculate(self):
        try:
            numbers = list(map(int, self.inputField.text().split()))
            result = process_array(numbers)
            self.resultArea.setText(result)
        except ValueError:
            self.resultArea.setText("Будь ласка, введіть коректні числа.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
