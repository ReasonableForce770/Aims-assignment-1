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
  { "name": "Electrike", "type": "Electric" }
]
mydf=pd.DataFrame(data)
#print(mydf)
#print(mydf[mydf['type']== 'Fire'])
mydf['encode']=0
for i in range(11):
    if mydf.iloc[i-1,1]=='Fire':
        a=0
    elif mydf.iloc[i-1,1]=='Water':
        a=1
    elif mydf.iloc[i-1,1]=='Electric':
        a=2
  
    mydf.iloc[i-1,-1]=a
print(mydf)
