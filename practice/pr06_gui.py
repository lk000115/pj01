from  PyQt5.Qt import  *
import sys

class  Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试主窗体")
        self.resize(500,500)
        self.set_ui()

    def set_ui(self):
        label = QLabel(self)
        label.setText("Lable的文本控件")



if __name__ == '__main__':
    # 1 创建一个应用程序
    app = QApplication(sys.argv)
    # 2 创建控件
    window = Window()
    window.show()
    # 3 进入消息循环
    sys.exit(app.exec_())
