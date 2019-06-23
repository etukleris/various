class Base():
	def foo(self):
		return self.bar()
		
		
		
def add(a,b):
	return a+b 
	
from time import sleep
def numbers():
	values = []
	for i in range(0,10,2):
		sleep(0.5)
		values.append(i)
	return (values)
		
last = 0
for val in numbers():
	print (add(last,val))
	last = val