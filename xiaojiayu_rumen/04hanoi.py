#汉诺塔游戏解法，递归实现方式
def hanoi(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)#将前n-1个盘子从A移动到B上
        print(a,'-->',c)#将最底下的最后一个盘子从A移动到C上
        hanoi(n-1,b,a,c)#将B上的n-1个盘子移动到C上

if __name__ == '__main__':
    n = int(input('请输入汉诺塔的层数：'))
    print('%d个盘子从A柱全部移动到C柱的解法顺序是：' % n)
    hanoi(n,'A','B','C')
