#斐波拉契数列的迭代实现方式
def fabonacci(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n==1 or n ==2:
        return 1
    while (n>2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n = n -1
    return n3   

if __name__ == '__main__':
    n = input('请输入一个正整数:')
    result = fabonacci(int(n))
    print('{0}个月后，产下的兔子为{1}对 '.format(n,result))
	
