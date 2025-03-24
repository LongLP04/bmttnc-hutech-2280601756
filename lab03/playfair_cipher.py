import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui.playfair import Ui_Dialog as Ui_MainWindow  # Đảm bảo bạn đã tạo file .ui và convert sang .py
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)
        self.ui.pushButton_3.clicked.connect(self.call_api_create_matrix)

    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.textEdit.toPlainText(),
            "key": self.ui.lineEdit.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setPlainText(data["encrypted_text"])
                self.show_message("Mã hóa thành công!")
            else:
                self.show_message("Lỗi khi gọi API", QMessageBox.Critical)
        except requests.exceptions.RequestException as e:
            self.show_message(f"Lỗi: {e}", QMessageBox.Critical)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.textEdit_2.toPlainText(),
            "key": self.ui.lineEdit.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setPlainText(data["decrypted_text"])
                self.show_message("Giải mã thành công!")
            else:
                self.show_message("Lỗi khi gọi API", QMessageBox.Critical)
        except requests.exceptions.RequestException as e:
            self.show_message(f"Lỗi: {e}", QMessageBox.Critical)
    def call_api_create_matrix(self):
        """Gửi yêu cầu tạo ma trận Playfair từ API"""
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
            "key": self.ui.lineEdit.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.update_table_widget(data["playfair_matrix"])  # Gọi hàm cập nhật bảng
                self.show_message("Tạo ma trận thành công!")
            else:
                self.show_message("Lỗi khi tạo ma trận", QMessageBox.Critical)
        except requests.exceptions.RequestException as e:
            self.show_message(f"Lỗi: {e}", QMessageBox.Critical)
    def update_table_widget(self, matrix):
        """Cập nhật QTableWidget với ma trận Playfair"""
        self.ui.tableWidget.setRowCount(5)  # Ma trận Playfair 5x5
        self.ui.tableWidget.setColumnCount(5)

        for i in range(5):
            for j in range(5):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(matrix[i][j]))


    def show_message(self, text, icon=QMessageBox.Information):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())
