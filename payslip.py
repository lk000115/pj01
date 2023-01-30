from openpyxl import load_workbook
from wechat_work import WechatWork
import tkinter as tk
from tkinter import filedialog

st = ['月份', '工号', '姓名', '部门', '应出勤天数', '法定假', '实际出勤天数', '基本工资', '岗位津贴', '加班补贴', '绩效工资',
      '加班工资', '夜班补贴', '高温津贴', '奖惩', '其他补贴', '应发合计', '代扣缴社保', '代扣缴公积金', '代扣缴个人所得税',
      '房租电费', '上期个税调整', '税前工资', '实发工资']
st1 = ['月份', '工号', '姓名', '部门', '应出勤天数', '法定假', '有薪假', '实际出勤', '基本工时', '平时加班', '周末加班',
       '法定假加班', '基本工资', '加班工资', '岗位津贴', '绩效工资', '夜班补贴', '超产奖', '高温补贴', '奖罚', '其他补贴',
       '应发合计', '代扣缴社保', '代扣缴公积金', '代扣缴个人所得税', '房租电费', '其它代扣', '上期个税调整', '税前工资', '实发工资']

corpid = 'wx86ade657d9d15fc5'
appid = '1000015'
corpsecret = 'vP_tz5m43cgFsQ-phNeWgZBhIelYxv3OEaXB4JLrHHY'
users = []
w = WechatWork(corpid=corpid,
               appid=appid,
               corpsecret=corpsecret)

root = tk.Tk()
root.title('工资条发送小工具')
root.geometry('400x400')
var = tk.StringVar()
var2 = tk.StringVar()


def get_file():
    global Filepath
    sub_root = tk.Toplevel(root)
    sub_root.withdraw()
    Filepath = filedialog.askopenfilename()
    var.set(Filepath)
    sub_root.destroy()  # 销毁窗体


def send_pay():
    wb = load_workbook(Filepath)
    sheet = wb.worksheets[0]
    i = 0
    for row in sheet.iter_rows(min_row=2):  # 从第二行开始读
        lt = []
        users = []
        for r in row:
            lt.append(r.value)

        users.append(lt[1])
        # print(
        #     f'{st[0]}:{lt[0]}\n{st[1]}:{lt[1]}\n{st[2]}:{lt[2]}\n{st[3]}:{lt[3]}\n{st[4]}:{lt[4]:.2f}\n'
        #     f'{st[5]}:{lt[5]:.2f}\n{st[6]}:{lt[6]:.2f}\n{st[7]}:{lt[7]:.2f}\n{st[8]}:{lt[8]:.2f}\n{st[9]}:{lt[9]:.2f}\n'
        #     f'{st[21]}:{lt[21]:.2f}\n{st[22]}:{lt[22]:.2f}\n{st[23]}:{lt[23]:.2f}\n'
        #     f'{users}')
        # 发送文本
        i += 1
        w.send_text(f'{st[0]}:{lt[0]}\n{st[1]}:{lt[1]}\n{st[2]}:{lt[2]}\n{st[3]}:{lt[3]}\n{st[4]}:{lt[4]:.2f}\n'
                    f'{st[5]}:{lt[5]:.2f}\n{st[6]}:{lt[6]:.2f}\n{st[7]}:{lt[7]:.2f}\n{st[8]}:{lt[8]:.2f}\n{st[9]}:{lt[9]:.2f}\n'
                    f'{st[10]}:{lt[10]:.2f}\n{st[11]}:{lt[11]:.2f}\n{st[12]}:{lt[12]:.2f}\n{st[13]}:{lt[13]:.2f}\n{st[14]}:{lt[14]:.2f}\n'
                    f'{st[15]}:{lt[15]:.2f}\n{st[16]}:{lt[16]:.2f}\n{st[17]}:{lt[17]:.2f}\n{st[18]}:{lt[18]:.2f}\n{st[19]}:{lt[19]:.2f}\n'
                    f'{st[20]}:{lt[20]:.2f}\n{st[21]}:{lt[21]:.2f}\n{st[22]}:{lt[22]:.2f}\n{st[23]}:{lt[23]:.2f}\n', users)
    var2.set(f'发送成功,总共发送{i}条数据')


def send_pay1():
    wb = load_workbook(Filepath)
    sheet = wb.worksheets[1]
    i = 0
    for row in sheet.iter_rows(min_row=2):  # 从第二行开始读
        lt = []
        users = []
        for r in row:
            lt.append(r.value)

        users.append(lt[1])
        # print(
        #     f'{st1[0]}:{lt[0]}\n{st[1]}:{lt[1]}\n{st[2]}:{lt[2]}\n'
        #     f'{st1[3]}:{lt[3]}\n{st[4]}:{lt[4]}\n{st[23]}:{lt[29]}\n{users}')
        # 发送文本
        i += 1
        w.send_text(f'{st1[0]}:{lt[0]}\n{st1[1]}:{lt[1]}\n{st1[2]}:{lt[2]}\n{st1[3]}:{lt[3]}\n{st1[4]}:{lt[4]:.2f}\n'
                    f'{st1[5]}:{lt[5]:.2f}\n{st1[6]}:{lt[6]:.2f}\n{st1[7]}:{lt[7]:.2f}\n{st1[8]}:{lt[8]:.2f}\n{st1[9]}:{lt[9]:.2f}\n'
                    f'{st1[10]}:{lt[10]:.2f}\n{st1[11]}:{lt[11]:.2f}\n{st1[12]}:{lt[12]:.2f}\n{st1[13]}:{lt[13]:.2f}\n{st1[14]}:{lt[14]:.2f}\n'
                    f'{st1[15]}:{lt[15]:.2f}\n{st1[16]}:{lt[16]:.2f}\n{st1[17]}:{lt[17]:.2f}\n{st1[18]}:{lt[18]:.2f}\n{st1[19]}:{lt[19]:.2f}\n'
                    f'{st1[20]}:{lt[20]:.2f}\n{st1[21]}:{lt[21]:.2f}\n{st1[22]}:{lt[22]:.2f}\n{st1[23]}:{lt[23]:.2f}\n{st1[24]}:{lt[24]:.2f}\n'
                    f'{st1[25]}:{lt[25]:.2f}\n{st1[26]}:{lt[26]:.2f}\n{st1[27]}:{lt[27]:.2f}\n{st1[28]}:{lt[28]:.2f}\n{st1[29]}:{lt[29]:.2f}\n', users)
    var2.set(f'发送成功,总共发送{i}条数据')


l = tk.Label(root, textvariable=var, font=('Arial', 12), width=60, height=6)
l.pack()

btn = tk.Button(root, text="添加工资条", command=get_file)
btn.pack()

l2 = tk.Label(root, textvariable=var2, font=('Arial', 12), width=30, height=6)
l2.pack()

btn2 = tk.Button(root, text="发送管理工资条", command=send_pay)
btn2.pack()

btn3 = tk.Button(root, text="发送计时工资条", command=send_pay1)
btn3.pack()

root.mainloop()
