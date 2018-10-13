import sys
import os
import pandas as pd
import shutil
"""os.mkdir('invasive')
os.mkdir('non_invasive')"""
x=len(os.listdir('train'))
df=pd.read_csv('train_labels/train_labels.csv')
x1='train'
x2='invasive'
x3='non_invasive'
ext='.jpg'
for i in range(0,x):
    y=str(df.ix[i,0])
    z=df.ix[i,1]
    #print(y.dtype)
    if z==0:
        shutil.copyfile(os.path.join(x1,y+ext),os.path.join(x3,y+ext))
        #shutil.copyfile(src,dest1)
    elif z==1:
        #shutil.copyfile(src,dest2)
        shutil.copyfile(os.path.join(x1,y+ext),os.path.join(x2,y+ext))