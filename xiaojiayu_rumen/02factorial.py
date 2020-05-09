#coding = gbk
import sys
#print sys.getdefaultencoding()
def factorial(n):
	result = n
	for i in range(1,n):
		result *= i
	return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print(result)