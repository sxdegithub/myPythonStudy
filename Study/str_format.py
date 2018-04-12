# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: sx

age = 20
name = 'sx'


print('{0} was {1} years old when he read this book'.format(name, age))
print('why is {0} playing with that python'.format(name))


# 对于浮点数 '保留小数点后三位
print('{0:.3f}'.format(10.0/3))

# 整数格式化输出，{ x:2d}  其中x代表第几个位置，2代表宽度，d代表十进制
for x in range(1, 10):
    print('{0:1d},{1:2d},{2:3d}'.format(x, x*x, x*x*x))

# 使用下划线填充文本，保持文字处于中间位置
# 使用(^)定义'___hello___'字符串长度为11
print('{0:_^11}'.format('hello'))

# 基于关键词的输出
print('{name} wrote {book}'.format(name='Swaroop', book='Byte of Python'))

# 指定空白结尾,print方法默认会以\n换行结尾
print('a', end=' ')
print('b', end='')
# 单独打印一个\n
print('')
# 加上默认换行，下面的实际打印了4个换行符
print('\n\n\n')
# 转义(\),在引号中使用引号
print('What\'s is your name?\n')

print('This is first line \nThis is second line')

# 在一行结尾添加（\），会使字符串继续，但是不会开始新行
print('This is first line \
This is second line')

# （r）来指定原始raw字符串
# 在处理正则表达式时，应全程使用原始字符串，否则有大量的backhacking处理
print(r"'Newlines are indicated by \n'")

# 运算符
print('a'+'b')

# 乘方
print(4**2)

# 整除(//)，向下取整数至最接近的整数
print('{0:.2f}'.format(10/3))
print(10//3)

# 取模（%），和取余正数时候一致，负数时候不一致，详见百度百科
print('取模操作（%）：{}'.format(-7%4))
# 左移位
print(2)
# 输出2的二进制表达10，移位操作后1000
print('二进制的2进行移位操作:{0:b}'.format(2))
print(2<<2)
# 二进制的2
print('二进制2的格式化输出为10进制：{0:d}'.format(0b1000))
print('十六进制的13格式化输出为10进制：{0:d}'.format(0xd))
print('八进制的7格式化输出为10进制：{0:d}'.format(0o7))

# 其他的一些转换
print('16进制的ff转10进制：{}'.format(int('ff', 16)))
print('16进制的ff转10进制：{}'.format(int('0xff', 16)))
print('2进制的1000转10进制：{}'.format(int('1000', 2)))

# 右移位

print('二进制的11（1011）：{0:b}'.format(11))
print('二进制的2：{0:d}'.format(0b10))
print('11进行右移2位操作二进制的:{0:b}'.format(11>>2))

# 按位与(&)，对数字进行按位与
print(0b1000010&0b111)
print('二进制2的格式化输出为10进制：{0:d}'.format(0b10))
# 按位或（|），
print('对数字3与5按位或：{}'.format(0b0101|0b0011))
# 按位异或
print('对数字3与5按位异或：{}'.format(0b0101^0b0011))
# 按位取反，x取反结果就是-（x+1）
print('对数字5按位取反：{}'.format(~5))
