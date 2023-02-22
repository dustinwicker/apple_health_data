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

# Save out
export_df.to_csv("export_df.csv")

export_df.columns
export_df.dtypes
export_df[:10]
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

set(export_df['HKCharacteristicTypeIdentifierDateOfBirth'])
set(export_df['HKCharacteristicTypeIdentifierBloodType'])
set(export_df['workoutActivityType'])

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
