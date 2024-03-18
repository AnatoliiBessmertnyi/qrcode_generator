import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
import qrcode

from qrcode_window import Ui_Form


class QRCodeApp(QMainWindow, Ui_Form):
    """
    QRCodeApp - это QMainWindow, который использует Ui_Form из qrcode_window.
    Он предоставляет функциональность для генерации QR-кода из входных данных и
    сохраняет его в файл.
    """
    def __init__(self):
        super(QRCodeApp, self).__init__()
        self.setupUi(self)
        self.pushGenerate.clicked.connect(self.generate_qr_code)
        self.pushSave.clicked.connect(self.save_qr_code)
        self.qr_image = None

    def generate_qr_code(self):
        """
        Генерирует QR-код из входного текста, преобразует его в изображение и
        отображает его в окне.
        """
        text = self.lineEdit.text()
        if not text:
            QMessageBox.warning(self, "Warning", "The text field is empty.")
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save("qr_code.png")
        pixmap = QPixmap("qr_code.png")
        self.label.setPixmap(pixmap)

    def save_qr_code(self):
        """
        Сохраняет изображение QR-кода в файл, выбранный пользователем.
        """
        if not QPixmap("qr_code.png"):
            QMessageBox.warning(
                self,
                "Warning",
                "No QR code has been generated."
            )
            return
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save QR Code",
            "",
            "PNG Files (*.png);;All Files (*)"
        )
        if filename:
            QPixmap("qr_code.png").save(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
