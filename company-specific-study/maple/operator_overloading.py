class size:
	def __init__(self,size1,size2):
		self.size1=size1
		self.size2=size2
	def __repr__(self):
		return("size1 {} size 2{}".format(self.size1,self.size2))
	def __add__(self,other):
		s1s=self.size1+other.size1
		s2s=self.size2+other.size2
		rso=size(s1s,s2s)
		return(rso)
	def __ge__(self,other):
		return(True if self.size1>other.size1 else False)


o1=size(20,20)
o2=size(11,22)

# print(o1)

o3=o1+o2
print(o3)
o4=o1>=o2
print(o4)