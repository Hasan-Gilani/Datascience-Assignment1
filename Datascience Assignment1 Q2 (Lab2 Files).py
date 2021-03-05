import pandas as pd
import os
import numpy as np


if __name__ == '__main__':
    df1 = pd.read_csv(r'Documents\data\data1.csv', index_col=0)
    df2 = pd.read_csv(r'Documents\data\data2.csv', index_col=1)
    
    df3 = pd.concat([df1, df2], sort=False)
    print(df3)

    df4 = pd.read_csv(r'Documents\data\data3.csv',index_col=0)
    print(df4)
    
    df5 = pd.concat([df3, df4], axis=1)
    print(df5)
    
    df6 = pd.read_json(r'Documents\data\data.json')
    df7 = pd.concat([df5, df6],sort=False)
    
    df7 = df7.replace(to_replace='Hello', value=np.nan)
    df7['A'] = df7['A'].astype('float64')
    df7 = df7.fillna(df7.mean())

    print(df7)


    

