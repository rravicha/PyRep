import time
import multiprocessing
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
pc=[]
if __name__=='__main__':
	srt=time.perf_counter()
	dtl1="34867298634~Peter Parker~27"
	for i in range(5):
		p=multiprocessing.Process(target=RoyalBankScotland(dtl1))
		pc.append(pc)
	stp=time.perf_counter()
	print(f'exec in {stp-srt} time')