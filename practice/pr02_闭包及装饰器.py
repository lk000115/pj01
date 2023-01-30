'''
 块注释
打开选择文件夹对话框
Pyinstaller -F setup.py 打包exe
Pyinstaller -F -w payslip.py 不带控制台的打包
Pyinstaller -F -i xx.ico setup.py 打包指定exe图标打包
root2.destroy()   # 销毁窗口

闭包和装饰器

'''
import time


# 装饰器
def outer(origin):
    def inner(*args,**kwargs):
        t1 = time.time()
        origin(*args,**kwargs)
        t2 = time.time()
        print(f"finish func:{origin.__name__},time cost:{t2 - t1:.20f}(sec)")

    return inner

@outer        #此语句代替  30行语句  myfunc = outer(myfunc)
def myfunc1():
    for i in range(1000000):
        pass
    print("我是myfunc函数")
# myfunc = outer(myfunc)
myfunc1()

@outer
def myfunc2(a):
    for i in range(1000000):
        pass
    print(f"我是myfunc函数{a}----")
myfunc2('g')
