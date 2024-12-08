import sys

from PySide6.QtWidgets import QApplication

from view.Window import Window


def main():
    # 创建应用
    app = QApplication([])
    # 创建窗口
    window = Window()
    window.showFullScreen()
    # 结束
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
