# format

示例1：'{0} love {1}.{2}'.format('sully','ruly','baozi')

示例2：'{a} love {b}.{c}'.format(a='sully',b='ruly',c='baozi')

示例3: '{0:.1f}{1}'.format(27.456,'GB')

# 字符串格式化符号含义

| 符号 | 说明                               |
| ---- | ---------------------------------- |
| %C   | 格式化字符及其ASCII码              |
| %S   | 格式化字符串                       |
| %d   | 格式化整数                         |
| %o   | 格式化无符号八进制数               |
| %x   | 格式化无符号十六进制               |
| %X   | 格式化无符号十六进制数(大写)       |
| %f   | 格式化定点数，可指定小数点后的精度 |
|      |                                    |
|      |                                    |

格式化操作符辅助指令

| 符号 | 说明                                   |
| ---- | -------------------------------------- |
| m.n  | m是显示的最小总宽度，n是小数点后的位数 |
| -    | 用于左对齐                             |
| +    | 在正数前面显示加号(+)                  |
|      |                                        |

%c示例： 

```
>>> '%c %c %c' % (98,99,100)
'b c d'
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

%s示例：

```
>>> '%s' % 'i love Fishc.com'
'i love Fishc.com'
>>> print('%s is the president' % 'Trump')
Trump is the president
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

%d示例：

```
>>> '%d + %d = %d' % (4,5,9)
'4 + 5 = 9'
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

%o,%x,%X示例：

```
>>> '%o' % 10
'12'
>>> '%x' % 10
'a'
>>> '%X' % 10
'A'
>>> '%X' % 168
'A8'
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

%f,%e,m.n示例：

```
>>> '%.1f' % 12.23456
'12.2'
>>> '%.4e' % 12.23456
'1.2235e+01'
>>> '%3.1f' % 1222.23456
'1222.2'
>>> '%9.1f' % 1222.23456
'   1222.2'
>>> 
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

字符串转义字符的含义

| 符号 | 说明           |
| ---- | -------------- |
| \'   | 单引号         |
| \"   | 双引号         |
| \a   | 发出系统响铃声 |
| \b   | 退格符         |
| \n   | 换行符         |
| \t   | 横向制表符     |
| \r   | 回车符         |