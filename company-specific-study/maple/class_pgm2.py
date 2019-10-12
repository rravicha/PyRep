class RoyalBankScotland:
	bank_alias='RBS' # class variable

	def __init__(self,details):
		self.details =	details.split('~') #instance variables
		self.idd	 =	self.details[0]
		self.name	 =	self.details[1]
		self.age	 =	self.details[2]
	def display_details(self):
		print(self.idd)
		print(self.name)
		print(self.age)


dtl1="34867298634~Peter Parker~27"
customer1=RoyalBankScotland(dtl1)

customer1.display_details()					# Accessing instance variable
RoyalBankScotland.bank_alias="RBScot1/9"	# Alter class Variable
print(customer1.bank_alias) 				# Accessing class variable

customer2=RoyalBankScotland(dtl1)
customer2.bank_alias="AAA"
print(customer2.bank_alias)

customer2.ssn=433426
print(dir(customer2))
print(dir(customer)1)