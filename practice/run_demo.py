import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtCore import QDir

from demo import Ui_MainWindow

class Myform(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('测试窗体')
    def show01(self):
        dialog = QFileDialog()
        # 设置文件创建模式
        dialog.setFileMode(QFileDialog.AnyFile)
        # 选择文件
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            # 如果打开成功
            self.filename = dialog.selectedFiles()
        self.lineEdit.setText(self.filename[0])
    def song(self):
        print(self.filename[0])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Myform()
    main.show()
    sys.exit(app.exec_())
