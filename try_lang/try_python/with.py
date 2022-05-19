
class Test(object):
	def __init__(self, num):
		self.num = num

	def __enter__(self):
		print('__enter__')
		return self

	def __exit__(self, type, value, traceback):
		print('__exit__')
		print(type)
		print(value)
		print(traceback)
		return self

if __name__ == '__main__':
	t = Test(66)
	with t:
		print(t.num)
		raise Exception('is an exception')

	print('in main')

'''
py3 with.py         
__enter__
66
__exit__
<class 'Exception'>
is an exception
<traceback object at 0x7f9d15d3bec0>
in main
'''