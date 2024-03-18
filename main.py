import sys
import os

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox
)
from PySide6.QtGui import QPixmap, QGuiApplication
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
        self.lineEdit.setPlaceholderText(
            'Enter data to convert to QR code'
        )  # Установка текста подсказки для lineEdit
        self.pushGenerate.clicked.connect(self.generate_qr_code)
        self.label.setScaledContents(True)
        self.pushSave.clicked.connect(self.save_qr_code)
        self.qr_image = None
        self.centerOnScreen()  # центрует картинку внутри окна
        self.pushZoomIn.clicked.connect(self.zoom_in)
        self.pushZoomOut.clicked.connect(self.zoom_out)


    def generate_qr_code(self):
        """
        Генерирует QR-код из входного текста, преобразует его в изображение и
        отображает его в окне.
        """
        text = self.lineEdit.text()

        # Если не ввели данные - ошибка при генерации QR-кода
        if not text:
            QMessageBox.warning(self, 'Warning', 'The text field is empty.')
            return
        # Проверка максимальной длины текста > 200
        elif len(text) > 200:
            QMessageBox.warning(
                self, 'Warning', 'The text is too long for a QR code.'
            )
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Проверка доступа к файловой системе
        try:
            img.save('qr_code.png')
        except IOError:
            QMessageBox.warning(
                self, 'Warning', 'Failed to save the QR code image.'
            )
            return

        pixmap = QPixmap('qr_code.png')
        self.label.setPixmap(pixmap)

    def save_qr_code(self):
        """
        Сохраняет изображение QR-кода в файл, выбранный пользователем.
        """
        # Если QR-код не сгенерирован - ошибка при попытке сохранения файла
        if not QPixmap('qr_code.png'):
            QMessageBox.warning(
                self, 'Warning', 'No QR code has been generated.'
            )
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, 'Save QR Code', '', 'PNG Files (*.png);;All Files (*)'
        )
        if filename:
            QPixmap('qr_code.png').save(filename)

        # Проверка успешного сохранения файла
            success = QPixmap('qr_code.png').save(filename)
            if not success:
                QMessageBox.warning(
                    self, 'Warning', 'Failed to save the QR code image.'
                )

    def centerOnScreen(self):
        """
        Центрирует окно на экране.
        """
        resolution = QGuiApplication.primaryScreen().geometry()
        self.move(
            (resolution.width() / 2) - (self.frameSize().width() / 2),
            (resolution.height() / 2) - (self.frameSize().height() / 2)
        )

    def zoom_in(self):
        """
        Увеличивает размер QR-кода.
        """
        self.label.resize(self.label.width() * 1.1, self.label.height() * 1.1)

    def zoom_out(self):
        """
        Уменьшает размер QR-кода.
        """
        self.label.resize(self.label.width() * 0.9, self.label.height() * 0.9)

if __name__ == '__main__':
    # Удалить файл qr_code.png, если он существует
    if os.path.exists('qr_code.png'):
        os.remove('qr_code.png')

    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
