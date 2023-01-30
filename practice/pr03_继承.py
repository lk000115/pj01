class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'
    def make_cake(self):
        print(f'')


class School(object):
    pass

class Prentice(Master):
    pass


mros = Prentice.mro()

for mro in mros:
    print(mro)


