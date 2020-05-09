#python中的类名约定以大写字母开头
class Turtle:
    #属性
    color = 'green'
    weight = 10
    leg = 4
    mouth = '小嘴'

    #方法
    def climb(self):
    	print('我正努力的想上爬...')

    def run(self):
        print('我正在飞快的向前跑...')

    def bite(self):
    	print('咬死你咬死你')


if __name__ == '__main__':
	tt = Turtle()
	tt.climb()
	tt.bite()
