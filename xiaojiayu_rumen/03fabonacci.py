#斐波拉契数列的递归实现方式
def fabonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

input_param = input('请输入一个正整数:')
result = fabonacci(int(input_param))
print("result:" + str(result))
