import tkinter as tk
from tkinter import filedialog
import pandas as pd
from wechat_work import WechatWork

corpid = 'wx86ade657d9d15fc5'
appid = '1000015'
corpsecret = 'vP_tz5m43cgFsQ-phNeWgZBhIelYxv3OEaXB4JLrHHY'
w = WechatWork(corpid=corpid,
               appid=appid,
               corpsecret=corpsecret)



def dele():
    text.delete('0.0','end')
def get_file():
    global Filepath
    sub_root = tk.Toplevel(root)
    sub_root.withdraw()
    Filepath = filedialog.askopenfilename()
    var.set(Filepath)
    sub_root.destroy()  # 销毁窗体
def send_pay():
    df = pd.read_excel(Filepath, sheet_name=0)
    # print(df.head().columns.values)  # 打印表头
    head = df.head().columns.values
    for item in df.values:
        st = ''
        users = []
        for i in range(len(item)):  # 把表每一行循环拼接为字符串格式
            st = st + str(head[i]) + ' : ' + str(item[i]) + '\n'
        users.append(str(item[1]).zfill(6))
        # print(st)  # 打印表的值-不含表头行
        bul = w.send_text(f'{st}', users)
        if bul:
            text.insert('insert', f'工资条发送成功:')
            text.insert('insert', f'工号:{str(item[1])} , 姓名:{str(item[2])}\n')
        else:
            text.insert('insert', f'工资条发送失败:')
            text.insert('insert', f'工号:{str(item[1])} , 姓名:{str(item[2])}\n')
        # print(str(item[2]))

    # print(df.values)



root = tk.Tk()
root.title('工资条发送小工具')
root.geometry('450x450')
var = tk.StringVar()

entry = tk.Entry(root,textvariable=var)
entry.place(relx=0.05,rely=0.1,relwidth=0.75,relheight=0.05)
btn = tk.Button(root, text="添加" , command=get_file)
btn.place(relx=0.81,rely=0.1,relwidth=0.15,relheight=0.05)

text = tk.Text(root)
text.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.6)

btn1 = tk.Button(root, text="清空" , command=dele)
btn1.place(relx=0.15,rely=0.8,relwidth=0.15)

btn2 = tk.Button(root, text="发送",command=send_pay)
btn2.place(relx=0.7,rely=0.8,relwidth=0.15)

root.mainloop()



