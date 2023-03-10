import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Increase maximum width in characters of columns - will put all columns in same line in console readout
pd.set_option('expand_frame_repr', False)
# Increase number of rows printed out in console
pd.options.display.max_rows = 200
pd.options.display.min_rows = None
# Be able to read entire value in each column (no longer truncating values)
pd.set_option('display.max_colwidth', None)
np.set_printoptions(threshold=np.inf, suppress=True)

# Change and update directory
os.chdir("C:\\Users\wickerd\Desktop\\apple_health_export")
# List files in current directory by last modified time
files = list(filter(os.path.isfile, os.listdir(os.getcwd())))
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
print(files)

import lxml
export_df = pd.read_xml('export.xml')
export_df_copy = export_df.copy()



# Drop rows where NULL (i.e. no values provided)
nunique_eq_0 = export_df.nunique()[export_df.nunique()==0]
export_df = export_df.drop(columns=nunique_eq_0.index)

nunique_eq_1 = export_df.nunique()[export_df.nunique()==1]

nunique_eq_2 = export_df.nunique()[export_df.nunique()==2]

ft_lb_df = export_df.loc[export_df.unit.isin(['ft','lb'])]

export_df = export_df.loc[~export_df.unit.isin(['ft','lb'])]
#export_df['value'].dropna().apply(lambda x: len(x)).value_counts().index[export_df['value'].dropna().apply(lambda x: len(x)).value_counts().index>20]

nunique_eq_1_df = []
for col in nunique_eq_1.index:
    unique_values = list(export_df[col].unique())
    unique_values = [x for x in unique_values if x is not None]# or str(x) != 'nan')]
    col, [x for x in unique_values if str(x) != 'nan']
    nunique_eq_1_df.extend([ col, [x for x in unique_values if str(x) != 'nan'] ])

export_df = export_df.drop(columns=nunique_eq_1.index)
# Save out
export_df.to_csv("export_df.csv")

export_df.iloc[  export_df['value'].dropna().apply(lambda x: len(x))[ export_df['value'].dropna().apply(lambda x: len(x))==33 ].index  ]




export_df.index.isin(  export_df['value'].dropna().apply(lambda x: len(x))[ export_df['value'].dropna().apply(lambda x: len(x))==33 ].index  )
export_df

df = export_df[['value','startDate','unit']]
df.dtypes
df.loc[:,'startDate'] = pd.to_datetime(df['startDate'].str[:-6])
df['startDate_'] = pd.to_datetime(df['startDate'], format='%Y%m%d')
df['value'].astype(float)
df.columns
df.unit.value_counts()
df.loc[df.unit=='ft']
df.loc[df.unit=='lb']
df.loc[df.unit=='mi']

df=df[4:]


df.dtypes

df.loc[df.value=='HKCategoryValueSleepAnalysisAsleep']
df[2214020:2218395]
export_df[2214020:2218395]

df.shape
df = df.loc[df.unit.notnull()]
df['value'] = df['value'].astype(float)

for i in df['unit'].value_counts().index:
    i
    df.loc[df.unit==i,'value'].describe()
    print('\n')

df = df.set_index('startDate')
df.loc[df.unit=='count/min','value'].describe()
df.loc[df.unit=='count/min'][:500][['value', 'startDate']].plot()

df.loc[df.unit=='count/min']['value'][:500]
df.index.dt

plt.plot(df.loc[df.unit=='count/min']['value'])
plt.xticks(df.loc[df.unit=='count/min']['startDate'])
plt.show()
df.loc[:,'day'] = df.index.day
df.loc[:,'month'] = df.index.month
df.loc[:,'year'] = df.index.year

for c in export_df.columns:
    print(export_df[c].unique())
    print('-')
    print(' ')

# Change and update directory
os.chdir("C:\\Users\wickerd\Desktop\\apple_health_export\electrocardiograms")

# List files in current directory by last modified time
files = list(filter(os.path.isfile, os.listdir(os.getcwd())))
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
print(files)

# Read one of the csv files
ecg = pd.read_csv('ecg_2019-09-21.csv')
ecg.shape
ecg[:10]
ecg[9:].shapedf[]
