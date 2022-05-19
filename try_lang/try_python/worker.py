
import time
import datetime

def worker():
	print 'worker', datetime.datetime.now()
	time.sleep(3)


if __name__ == '__main__':
	print datetime.datetime.now()
	print datetime.datetime.now().strftime('%y')
	print datetime.datetime.now().strftime('%Y')
	print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print datetime.datetime.now().strftime('%h %D')
	n = datetime.datetime.now()
	print n.strftime('%a %A %b %B -- %c --  %Z')
	print n.strftime('%j %p %U %w')
	print n.strftime('%x -- %X -- %%')

	for i in xrange(5):
		worker()


'''
python2 worker.py      
2022-05-19 17:32:23.619591
22
2022
2022-05-19 17:32:23
May 05/19/22
Thu Thursday May May -- Thu May 19 17:32:23 2022 --  
139 PM 20 4
05/19/22 -- 17:32:23 -- %
worker 2022-05-19 17:32:23.619697
worker 2022-05-19 17:32:26.621257
worker 2022-05-19 17:32:29.625409
worker 2022-05-19 17:32:32.629464
worker 2022-05-19 17:32:35.630480
'''