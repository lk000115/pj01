import pandas as pd

# d = {'a':1,'b':2,'c':3,'d':4,'e':5}
# df = pd.Series(d)
df = pd.read_excel(r'F:\books\工资条.xlsx')
print(df.head().columns.values)  # 打印表头
print(df.values)  # 打印表的值-不含表头行
print('------------------')
tmp=[]
tmp=df.head().columns.values
print(tmp)
