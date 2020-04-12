import random
secret = random.randint(1,10)
print(secret)
print("---------我爱ruly-----------")
temp = input("不妨猜一下小甲鱼现在心里想的哪个数字:")
guess = int(temp)
while guess != secret:
    if guess > secret:
        print("猜大了！")
    elif guess < secret:
        print("猜小了!")
    temp = input("请重新猜:")
    guess = int(temp)

print("猜对啦，小甲鱼现在心里想的是："+ str(secret))
print("游戏结束，不玩啦")
