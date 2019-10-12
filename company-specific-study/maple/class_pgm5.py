#inheritance
class broker:
	def __init__(self):
		print('broker init')
	def broker_details():
		pass
	def passin(self):
		print('broker pass')
class obama_hc:
	def __init__(self):
		print('obama init')
	def subsidy(self):
		print('susbidy info')
	def passin(self):
		print('obama pass')

class policy_holder(obama_hc,broker):
	def __init__(self):
		super().__init__()
		print('policy init')
	def holder_info(self):
		#super().subsidy()
		print('holder info')
		super().passin()

ph1=policy_holder()
print('---')
ph1.holder_info()

