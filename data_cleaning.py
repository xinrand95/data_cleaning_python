# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:33:21 2020

@author: erind
"""

import pandas as pd
excel_file = 'data_cleaning.xlsx'
df = pd.read_excel(excel_file)
df.dtypes

#change datatype to string
for column in df.columns:
    df[column] = df[column].astype(str)



#remove special charactor
## W = number or alphabet     \W <> number or alphabet
for column in df.columns:
    df[column] = df[column].str.replace(r'\W', '')
    
#remove number from Department column
df["Department"] = df["Department"].str.replace(r'\d+', '')  


#format Phone_Nbr into (XXX)XXX-XXXX
df['Phone_Nbr']=df["Phone_Nbr"].apply(lambda x: '('+x[:3]+')'+x[3:6]+'-'+x[6:10])

#check the data before output
print(df)

#output as a new excel
df.to_excel("column_cleaned.xlsx")