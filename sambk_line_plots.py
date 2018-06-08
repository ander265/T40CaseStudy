import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy

os.chdir('insert directory to data here')

dta = pd.read_csv('EXTR_RPSale.csv')
'''dta.head(10) -> First 9 rows'''

df = pd.DataFrame(dta, columns = ['DocumentDate'])

df['DocumentYear'] = pd.DatetimeIndex(df['DocumentDate']).year
df['DocumentMonth'] = pd.DatetimeIndex(df['DocumentDate']).month
df['DocumentCount'] = 1
'''df[:10] -> First 10 rows'''

#Filter 20XX
df.loc[df['DocumentYear'] == 2014]

df['DocumentMonth'].hist(bins = 20, facecolor = 'gray')
