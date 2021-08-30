'''
in 这个关键字会一直遍历 iterable, 直至发现。
发现，便会退出。itrable里会有剩余未迭代部分的数据。
'''


it = iter('abcde')

if 'c' in it:
    print('c yes')
else:
    print('c no')

#print('1 list: ', list(it))
#print('1.5 list: ', list(it))

if 'a' in it:
    print('a yes')
else:
    print('a no')


if 'e' in it:
    print('e yes')
else:
    print('e no')

print('2 list: ', list(it))

if 'x' in it:
    print('x yes')
else:
    print('x no')

print('3 list: ', list(it))


# print('next: ', next(it))


'''
c yes
1 list:  ['d', 'e']
1.5 list:  []
e no
2 list:  []
x no
3 list:  []ss
Traceback (most recent call last):
  File "test_if_in_iter.py", line 29, in <module>
    print('next: ', next(it))
StopIteration
'''
