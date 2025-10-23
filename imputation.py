import pandas as pd
import numpy as np
data =[
  { "name": "Charmander", "type": "Fire" },
  { "name": "Vulpix", "type": "Fire" },
  { "name": "Growlithe", "type": "Fire" },
  { "name": "Squirtle", "type": "Water" },
  { "name": "Psyduck", "type": "Water" },
  { "name": "Seel", "type": "Water" },
  { "name": "Magnemite", "type": "Electric" },
  { "name": "Voltorb", "type": "Electric" },
  { "name": "Pichu", "type": "Electric" },
  { "name": "Electrike", "type": "Electric" },
  { "name": "Missing"}
]
mydf=pd.DataFrame(data)
#print(mydf)
#print(mydf[mydf['type']== 'Fire'])
a=0
b=0
c=0
for i in range(11):
    if mydf.iloc[i-1,1]=='Fire':
        a=a+1
    elif mydf.iloc[i-1,1]=='Water':
        b=b+1
    elif mydf.iloc[i-1,1]=='Electric':
        c=c+1
x=int(input("Enter 1 for mode , 2 for median "))
if x==1:
    if max(a,b,c)==a:
        mydf.iloc[10,1]='Fire'
    if max(a,b,c)==b:
        mydf.iloc[10,1]='Water'
    if max(a,b,c)==c:
        mydf.iloc[10,1]='Electric'
if x==2:
    mydf.iloc[10,-1]=(mydf.iloc[5,-1])

print(mydf)
