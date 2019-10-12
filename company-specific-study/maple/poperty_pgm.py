import os
import glob
import logging
logformat="%(asctime) %(level) %(message)s"
logging.basicConfig(
    filename='policy_log.dat',
    filemode='w',
    format=logformat,
    level=logging.DEBUG
    )
l=logging.getLogger()
class policy:
    aptc_amt=0.75
    policy_count=0
    def __init__(self,inp):
        self.inp=inp.split('~')
        self.first,self.last=self.inp[0].split(' ')
        self.policy_name=self.inp[1]
        self.premium=int(self.inp[2])
        policy.policy_count+=1
        #print(self.first,self.last,self.policy_name)
    @classmethod
    def apply_aptc(cls,amt):
        cls.aptc_amt=amt
        
data=[]
for file in glob.glob("*.txt"):
    print('reading file {}'.format(file))
    with open(file) as f:
        data.append(f.readline())
print(data)
policy.aptc_amt=80
user1=policy(data[0])
user2=policy(data[1])
print(policy.policy_count)
l.debug("End debug message")
os.system('cat policy_log.dat')