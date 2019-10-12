class item:
	def __init__(self,size1,size2):
		self.size1=size1
		self.size2=size2
	def __add__(self,obj):
		s1s=self.size1+obj.size1
		s2s=self.size2+obj.size2

		s3=item(s1s,s2s)
		return(s3)
	def __gt__(self,obj):
		s1=self.size1+self.size2
		s2=obj.size1+obj.size2

		if s1>s2:
			return True
		else:
			return False

i1=item(1,2)
i2=item(3,4)

i3=i1+i2
print(i3.size1)
print(i3.size2)
if i1>i2:
	print("i1")
else:
	print("i2")