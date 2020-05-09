class Tortoise:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.tortoise = Tortoise(x)
        self.fish = Fish(y)

    def print_num(self):
        print('池中总共有乌龟%d只，鱼%d条' % (self.tortoise.num , self.fish.num))

        
