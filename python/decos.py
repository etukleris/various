

def runthreetimes(n):
	def addmore(fun):
		def add(x):
			#print(n,x)
			x=n+" IS "
			#print(n,x)
			value = fun(x)
			return value
		return add
	return addmore
	
@runthreetimes("THIS")	
def addtwo(x):
	return (x+"DECORATOR")
	
	
	
print(addtwo("IS"))