import os
import pandas as pd

# gather all file names from fault data
f_all = [files for _,_a,files in os.walk('./data/faults/')]
f_all = f_all[0]
# _ = f_all.pop(f_all.index('plots.ipynb'))

def cleandf(df_):
    retvar = df_[df_.Time>0.6]
    retvar = retvar[retvar.Time<1.4]
    retvar = retvar.reset_index()
    retvar = retvar.drop(columns = 'index')
    return retvar

# Drop time and clen starting and ending
for f_n in f_all: 
    f_pn = './data/faults/'+f_n
    df1 = pd.read_csv(f_pn)
    df1 = cleandf(df1)
    df1 = df1.drop(columns='Time')
    df1.to_csv('./cleaned_data/faults/'+f_n,index=False,header=False)

# Keep only the current data and clean starting and ending
for f_n in f_all: 
    f_pn = './data/faults/'+f_n
    df1 = pd.read_csv(f_pn)
    df1 = cleandf(df1)
    df1 = df1.drop(columns='Time')
    df1 = df1.drop(columns=' VdcL(Rectifier)')
    df1.to_csv('./cleaned_data/faults_current_only/' + f_n,index=False,header=False)

# Save Time Data of cleaned file
f_pn = './data/faults/'+f_all[13]
df1 = pd.read_csv(f_pn)
df1 = cleandf(df1)
df1 = df1.drop(columns=' VdcL(Rectifier)')
df1 = df1.drop(columns=' IdcL(Rectifier)')
df1.to_csv('./cleaned_data/time/time.txt',index=False,header=False)