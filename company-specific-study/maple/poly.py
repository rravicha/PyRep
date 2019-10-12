class pycharm:
	def feature(self):
		print("syntax highligting")
class maple:
	def feature(self):
		print("syntax highligting")
		print("pep8 highligting")
class code:
	def ide(self,ide):
		ide.feature()
p=pycharm()
m=maple()
c=code()
c.ide(m)