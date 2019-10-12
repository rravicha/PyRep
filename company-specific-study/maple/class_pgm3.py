#static/instance and class methods
#static/instance and class variables

class policy:
	#class variable
	carrier="Cigna"
	#instance method with instance variable
	def __init__(self,policy_id,eff_dt):
		self.policy_id = policy_id
		self.eff_dt	   = eff_dt
	#class method 
	@classmethod
	def get_carrier(cls):
		return(cls.carrier)
	@staticmethod
	def get_details():
		print("This is an active carrier")

p1=policy(23658,'01/01/2019')
print(p1.policy_id)
print(p1.carrier)
print(p1.get_carrier())
p1.get_details()