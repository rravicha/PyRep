# creating an empty panel
import pandas as pd
import numpy as np

##data = np.random.rand(2,4,5)
##p = pd.Panel(data)
##print(p)

##data = np.random.rand(2,3,4)
##print(data)

data = {'Item1' : pd.DataFrame(np.random.randn(2, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print(p.minor_xs(2))



##var = [[5,6,8,9],[5,8,9,74]]
##data = pd.DataFrame(var)
##print(data)

##var = [{"Name":"Mohan", "Age": 32}]
##data = pd.DataFrame(var)
##print(data)
