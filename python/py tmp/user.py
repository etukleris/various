from time import time


def timer (fun):
	def f (x, y):
		before = time()
		value = fun(x,y)
		after = time()
		print('time used = ', after-before)
		return value
	return f
	
#wrapper to run function twice
def ntimes(fun):
	def wrapper(*args,**kwargs):
		for _ in range(2):
			print('running {.__name__}'.format(fun))
			rv = fun(*args,**kwargs)
		return rv
	return wrapper

	
@ntimes
def addition (a, b):
	return a+b
	
#addition = timer(addition)
print (addition(5,6))