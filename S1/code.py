import pandas as pd
file_path = 'data.csv'
data = pd.read_csv(file_path)
data

reversed_df = data.iloc[::-1].reset_index(drop=True)
reversed_df


#-------------------------------------------------------

import matplotlib.pyplot as plt

plt.plot(reversed_df['Value'])


plt.show()


#----------------------------------------------------------
reversed_df['Return2'] = reversed_df['Value'].pct_change() 
returns = [(reversed_df['Value'][i] - reversed_df['Value'][i - 1]) / reversed_df['Value'][i - 1] * 100
           if i > 0 else 0
           for i in range(len(reversed_df))]
reversed_df


plt.plot(reversed_df['Return'])


plt.show()
