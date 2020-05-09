# 序列

列表list、元组tuple、字符串string的共同点

1. 都可以通过索引得到每一个元素
2. 默认索引值都是从0开始
3. 可通过分片的方法得到一个范围内的元素的集合
4. 有很多共同的操作(重复操作符、拼接操作符、成员关系操作符)

list把一个可迭代对象转换成列表

```
>>> a = []
>>> len(a）
    
SyntaxError: invalid character in identifier
>>> a
[]
>>> b = 'i love fishc.com'
>>> len(b)
16
>>> b
'i love fishc.com'
>>> b = list(b)
>>> b
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'f', 'i', 's', 'h', 'c', '.', 'c', 'o', 'm']
>>> max(b)
'v'
>>> numbers = [3,5,6,23,56,-109,87]
>>> max(numbers)
87
>>> min(numbers)
-109
>>> chars='0123456789'
>>> max(chars)
'9'
>>> min(chars)
'0'
>>> tuple1 = (1,2,3,5,6,7,8,9)
>>> max(tuple1)
9
>>> numbers.append('a')
>>> type(numbers)
<class 'list'>
>>> type(tuple1)
<class 'tuple'>
>>> max(numbers)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    max(numbers)
TypeError: '>' not supported between instances of 'str' and 'int'
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

# list的sorted、reversed、zip示例

```
>>> numbers = [3,12,56,12,53,6,0,-10]
>>> sorted(numbers)
[-10, 0, 3, 6, 12, 12, 53, 56]
>>> reversed(numbers)
<list_reverseiterator object at 0x00386850>
>>> list(reversed(numbers))
[-10, 0, 6, 53, 12, 56, 12, 3]
>>> list(enumerate(numbers))
[(0, 3), (1, 12), (2, 56), (3, 12), (4, 53), (5, 6), (6, 0), (7, -10)]
>>> a = [1,2,3,4,5,6,7,8]
>>> b = [4,5,6,7,8]
>>> zip(a,b)
<zip object at 0x0364FDC8>
>>> list(zip(a,b))
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
>>> type(numbers)
<class 'list'>
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)