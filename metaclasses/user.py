#user.py
from library import Base

#derived class enforce constraint on base class
#assert hasattr(Base, 'foo'), "attr foo not available"

class Derived(Base):
	def bar(self):
		return 'bar'