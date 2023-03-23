class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'
        print('父类的init方法')
    def make_cake(self):
        print(f'我是父类的cake方法')


class School(object):
    pass

class Prentice(Master):
    def __init__(self):
        # super().__init__()
        self.make_cake()

pren = Prentice()



