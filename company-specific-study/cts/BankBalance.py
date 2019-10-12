import timeit
timeit.timeit()
import pandas as pd
timeit.timeit()
import seaborn as sns
timeit.timeit()
bal=pd.read_csv('/home/susi/Downloads/statement.csv')
timeit.timeit()
sns.lineplot(data=bal,x='Date',y='Balance')
timeit.timeit()
import matplotlib.pyplot as plt
plt.show()
