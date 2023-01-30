import random


class Animal():
    def __init__(self):
        print('a animal')

    def fuxi(self):
        print('哺乳动物都可以呼吸氧气')


class Dog():
    def __init__(self):
        print('a dog')
    def eat(self):
        print(f'{self.name}---狗能啃骨头' )

class Dog01(Dog,Animal):
    def __init__(self):
        super(Dog01, self).__init__()
if __name__ == '__main__':
    # random.seed(10)
    dog01 = Dog01()
