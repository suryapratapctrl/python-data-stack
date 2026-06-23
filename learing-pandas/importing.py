import pandas as pd

df = pd.read_csv('pokemon.csv',index_col='Name')   #to location data by new index label which Name
#df= pd.read_json('pokemon.json')

#excerise on selection

#pokemon=input('enter the name of a pokemon: ')

#try:
#  print(df.loc[pokemon])
#except KeyError:
#  print(f"{pokemon} not found")


#Filtering= Keeping the rows that match a condition 
#tall_pokemon=df[df['Height']>=2]
#print(tall_pokemon)


#data cleaning : this is the process of cleaning and fixing incomplete , irrevalent or incorrect data


#1 drop irrelevant columns

df=df.drop(kcolumns=['Legendary','No'])


#2 handle missing data

df=df.dropna(subset=['Type2'])
df=df.fillna({'Type2':'NONE'})



#3 fix or replace values

df['Type1']=df['Type1'].replace({'Grass':'GRASS',
                                 'Fire':'FIRE'})
 

#4 Standardize text

df['Name']=df['Name'].str.lower()

#5 fix data types

df['Legendary']=df['Legendary'].astype(bool)

# 6 remove duplicate values

df=df.drop_duplicates()