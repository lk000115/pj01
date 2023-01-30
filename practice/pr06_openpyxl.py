from openpyxl import load_workbook
wb = load_workbook(r'F:\books\工资条.xlsx')
ws = wb.active
print(ws)
for cell in ws["1"]:
    print(cell.value)

