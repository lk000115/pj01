import re

pat = 'abc'
s = 'abcrtrtrtrtabcrf ff'
sp = re.findall(pat, s)
if sp:
    print(sp)
else:
    print('k')

#  正则表达式替换函数  sub
pat = '破解'
s = '我想学习破解内容,破解编程'
new_s = re.sub(pat,'xxx',s)
print(new_s)

# 正则表达式分割函数 split
