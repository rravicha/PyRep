#class inside class

class policy:
	def __init__(self,pid,bid):
		self.pid=pid
		self.b=self.broker(bid)
	def show(self):
		print(self.pid)
		self.b.show()

	class broker:
		def __init__(self,bid):
			self.bid=bid

		def show(self):
			print(self.bid)

p1=policy(8247269,999)
p1.show()

