#gen.py
from time import sleep
# top-level syntax, function --> underscore method
#  x() 										__call__

def add1(x, y):
	return x+y


class Adder:
	def __call__(self, x, y):
		return x + y + self.z

add2 = Adder()


class Compute:
	def __iter__ (self):
		self.last = 0
		return self

	def __next__ (self):
		rv = self.last
		self.last += 1
		if self.last > 10
			raise StopIteration()
		sleep(.5)
		return rv

#function that can be iterated over
##Generator formulation
def compute():
	for i in range(10)
		sleep(.5)
		yield i

for val in Compute():
	print(val)


# for x in xs:
#	pass

#xi = iter(xs)		-> __iter__
#while True:
# 	x = next(xi)	-> __iter__


#generators can allow for interweaving of code and proper sequencing of functions

class Api:
	def run_this_first(self):
		first()
	def run_this_second(self):
		second()
	def run_this_last(self):
		last()

def api():
	first()
	yield
	second()
	yield
	last()