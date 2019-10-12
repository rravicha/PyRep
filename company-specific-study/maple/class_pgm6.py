#polymorphism

class pycharm:
	def feature(self):
		print("Syntax Highlighting")


class maple:
	def feature(self):
		print("Syntax Highlighting")
		print("PEP8 check")

class code:
	def code(self,ide):
		ide.feature()

p=pycharm()
m=maple()
c1=code()
c1.code(m)