#dec.py
from time import time

#decorators wrap a fucntion modifying its behavior ex : adding a timer to add/sub functions without making annoying changes to user code


#print((getsource(add)))
#print add.__code__

def timer(func):
	def f(*args, **kwargs):
		before = time() 
		rv = func(*args,**kwargs)
		after = time()
		print ('elapsed', after - before)
		return rv
	return f

def ntimes(n):
	def inner(f):
		def wrapper(*args, **kwargs):
			for _ in range (n):
				print('running {.__name__}'. format(f))
				rv = f(*args, **kwargs)
			return rv
		return wrapper
	return inner

@ntimes(6)
def add(x, y=20):
	return x+y

@timer
def sub(x, y= 10):
	return x-y

print('add(10)', add(10))
print('add(20,30)', add(20, 30))
print('add("a", "b")', add("a","b"))
print('sub(10)', sub(10))
print('sub(20,30)', sub(20, 30))