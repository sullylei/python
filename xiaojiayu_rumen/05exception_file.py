try:
    
    f = open("nihao.txt",'w')
    print(f.write('你好啊'))
    sum = 1 + '1'
    f.close()
except(OSError,TypeError) as reason:
    print('出错了\n错误原因是：' + str(reason) )
finally:
    f.close()
