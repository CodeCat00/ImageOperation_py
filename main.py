import sys

from PySide6.QtWidgets import QApplication

from model.ImageOperationmodel import ImageOperationModel
from view.Window import Window


def main():
    app = QApplication([])

    window = Window(ImageOperationModel())
    window.showFullScreen()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
