from openpyxl import load_workbook
wb = load_workbook(r'F:\books\工资条.xlsx')
ws = wb.active
print(ws)
<<<<<<< HEAD
for cell in ws["1"]:
    print(cell.value)
print('sdsdsd')

# 已经更新20230206
# 第二次测试 
# 第三次测试
777
=======
for cell in ws["2"]:
    print(cell.value)

>>>>>>> 47a4655 (Initial commit)
