import numpy as np
import pandas as pd
import tensorflow as tf
import os

def cleandf(df_):
    retvar = df_[df_.Time>0.6]
    retvar = retvar[retvar.Time<1.4]
    retvar = retvar.reset_index()
    retvar = retvar.drop(columns = 'index')
    return retvar

allFiles = [fn for _, _1, fn in os.walk('./data/test/')]
allFiles = allFiles[0]

f_current_data = []
for f in allFiles:
    tmp = pd.read_csv('./data/test/'+f)
    tmp = cleandf(tmp)
    tmp = tmp.drop(columns=['Time', ' VdcL(Rectifier)'])
    tmp = tmp.to_numpy(dtype=float)
    tmp = tmp.reshape(tmp.size,)
    tmp = tmp[3000:-3000]
    tmp = tmp.reshape(1,tmp.size)
    f_current_data += [tmp]

model = tf.keras.models.load_model('./downloads/Models/Adam_input_reduced_split')
os.system('cls')
print("Model ")
model.summary()

print('\n\n')
print(80*"#")
print("")
for xt in f_current_data:
    ans = model.predict(xt)
    print("Estimated Fault Loaction: ", ans[0])
print('')
print(80*'#')
print('\n')
os.system('PAUSE')