# encoding:utf-8

'''
https://book.pythontips.com/en/latest/__slots__magic.html
'''

class A(object):
	name = 'A'

class B(object):
	name = 'B'
	__slots__ = ['a', 'b']

class C(object):
	name = 'C'
	__slots__ = ['a', 'b', '__dict__']

# 不继承于object的都会不会有异常
class D():
	name = 'D'

class E():
	name = 'E'
	__slots__ = ['a', 'b']

class F():
	name = 'F'
	__slots__ = ['a', 'b', '__dict__']



def test_obj(obj):
	try:
		obj.x = 10
		print(obj.x)
	except Exception as e:
		print('error:' +obj.name)
		print(str(e))
	else:
		pass
	finally:
		pass


if __name__ == '__main__':
	test_obj(A())
	test_obj(B())
	test_obj(C())
	test_obj(D())
	test_obj(E())

'''
python3 slots.py
10
error:B
'B' object has no attribute 'x'
10
10
error:E
'E' object has no attribute 'x'
'''