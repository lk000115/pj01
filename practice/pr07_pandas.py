import pandas as pd



df = pd.read_excel(r'D:\py_sty\pj01\res\gz.xlsx',sheet_name=0)
# print(df.head().columns.values)  # 打印表头
head = df.head().columns.values
for item in df.values:
    st = ''
    for i in range(len(item)):  # 把表每一行循环拼接为字符串格式
        st = st + str(head[i]) + ' : ' + str(item[i]) + '\n'
    user = str(item[1])
    print(user)
    print(st)  # 打印表的值-不含表头行
print(df.values)




# print('------------------')
# tmp=[]
# tmp=df.head().columns.values
# print(tmp)
