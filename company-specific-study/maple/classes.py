import concurrent.futures
class hps:
    allowed_carriers=['cigna','kaiser','hcsc','christus']#class variable
    def __init__(self,arg):#instance method
        self.inbound=arg#instance variable
        print(self.inbound)
    

    @classmethod
    def hps_overview(cls):#class method
        print('3rd Party Interface for creating policy')

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor() as exe:
        data="passed data"
        exe.submit(hps(data))