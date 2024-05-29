import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap


if __name__ == '__main__':
    url_image = 'https://autozam.ru/wp-content/uploads/2019/11/imagetools22.jpg'
    app = QApplication(sys.argv)
    image = QImage()
    image.loadFromData(requests.get(url_image).content)

    image_label = QLabel()
    image_label.setPixmap(QPixmap.fromImage(image))
    image_label.show()

    sys.exit(app.exec_())
