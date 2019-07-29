import pandas as pd
import numpy as np
##from pandas.plotting._misc import (scatter_matrix, radviz,
##                                   andrews_curves, bootstrap_plot,
##                                   parallel_coordinates, lag_plot,
##                                   autocorrelation_plot)
##from pandas.plotting._core import boxplot
##from pandas.plotting._style import plot_params
##from pandas.plotting._tools import table
##
##from pandas.plotting._converter import \
##    register as register_matplotlib_converters
##from pandas.plotting._converter import \
##    deregister as deregister_matplotlib_converters

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',periods=10), columns=list('ABCD'))

df.plot()
