# library.py

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		if name != 'Base' and not bar in Body:
			raise TypeError("Bad user class")
		print('BaseMeta.__new__', name, bases, body)
		return super().__new__(cls, name, bases body)

class Base(metaclass=BaseMeta):
	def foo(self):
		return self.bar()

	def __init_subclass__(cls, *a, **kw):
		print('init__sublcass', a, kw)
		return super().__init_subclass__(*a,**kw)


# from dis import dis
# dis(_)
## define hooks old method
'''
old_bc = __build_class__
def my_bc(fun, name, base=None, **kw):
	if base is Base:
		print('Check if bar method is defined')
	if base is not None:
		return old_bc(fun, name, base, **kw)
	return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__= my_bc
'''