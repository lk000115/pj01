from sys import argv

script, filename = argv

try:
    txt = open(filename,encoding='utf-8')
    print ("Here's your file %r:" % filename)
# print (txt.read())
# print ("Type the filename again:")
# file_again = input("> ")
# txt_again = open(file_again,encoding='utf-8')
# print (txt_again.read())
except IOError:
    print('文件不存在')
