from openpyxl import load_workbook
wb = load_workbook(r'F:\books\工资条.xlsx')
ws = wb.active
print(ws)
l=[]
for cell in ws[1]:
    l.append(cell.value)
print(l)
#jjjjj
