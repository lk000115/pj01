import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtCore import QDir
from paySlipWin  import Ui_MainWindow
import pandas as pd
from wechat_work import WechatWork

class Myform(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('工资条发放小工具')
        self.corpid = 'wx86ade657d9d15fc5'
        self.appid = '1000015'
        self.corpsecret = 'vP_tz5m43cgFsQ-phNeWgZBhIelYxv3OEaXB4JLrHHY'

    def selectFile(self):
        dialog = QFileDialog()
        # 设置文件创建模式
        dialog.setFileMode(QFileDialog.AnyFile)
        # 选择文件
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            # 如果打开成功
            self.filename = dialog.selectedFiles()
        self.lineEdit.setText(self.filename[0])

    def pushpay(self):
        w = WechatWork(corpid=self.corpid,
                       appid=self.appid,
                       corpsecret=self.corpsecret)

        df = pd.read_excel(self.filename[0], sheet_name=0)
        # print(df.head().columns.values)  # 打印表头
        head = df.head().columns.values
        self.printf('以下用户的工资条发送成功:\n')
        for item in df.values:
            st = ''
            users = []
            for i in range(len(item)):  # 把表每一行循环拼接为字符串格式
                st = st + str(head[i]) + ' : ' + str(item[i]) + '\n'
            users.append(str(item[1]).zfill(6))      #把工号转换为6位字符串
            # print(users)
            # print(st)  # 打印表的值-不含表头行
            w.send_text(f'{st}', users)
            self.printf(str(item[2]))

        # print(df.values)


    def clear(self):
        self.textBrowser.clear()

    def printf(self, mes):    # 把控制台信息实施显示到控件textBrower中函数
        self.textBrowser.append(mes)
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Myform()
    main.show()
    sys.exit(app.exec_())