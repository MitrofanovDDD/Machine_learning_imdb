import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df_path = 'C:/Users/user/Desktop/Data science/Мо/imdb_top_1000.csv'
df_imdb = pd.read_csv(df_path)
df_imdb.shape
df_imdb.head()
s = (df_imdb.dtypes == 'object')
object_cols = list(s[s].index)
# Defining categorical variables
print("Categorical variables:")
print(object_cols)
del df_imdb['Poster_Link']
del df_imdb['Overview']
missing_data = df_imdb.isnull()
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print(" ")
# Changing NaN in the rating column to a more understandable value
print(df_imdb.Certificate.unique())
df_imdb[df_imdb['Certificate'].isna()]
df_imdb['Certificate'] = df_imdb['Certificate'].fillna('Unrated')
#Converting a column to numeric values
df_imdb['Series_Title'].loc[df_imdb['Certificate']=='Unrated']
df_imdb['Certificate'].replace({'A': 18, 'UA': 14,'U': 16,'R': 16,'G': 0,'Passed':0,'PG-13':13,
                            'PG':0,'Unrated':0,'GP':14,'Approved':12,'TV-PG':13,'U/A':13},
                            inplace = True)
# Converting 'Gross' column to numeric values
df_imdb.dropna(subset=["Gross"], axis=0, inplace=True)
df_imdb.reset_index(drop=True, inplace=True)
df_imdb.Gross[1].split(',')
for i in range(len(df_imdb["Gross"])):
    r=df_imdb.Gross[i].split(',')
    df_imdb['Gross'][i] = ''.join(r)
df_imdb['Gross'].astype(int)
df_imdb['Gross'].dtype
df_imdb.head()
# Building a column showing the initially missing values in the column 'Meta_score'
df_imdb['Metascore_NaN']=np.NaN
df_imdb['Metascore_NaN']=list(df_imdb['Meta_score'].isnull())
#Plotting a graph showing the relationship
sns.regplot(x=df_imdb['IMDB_Rating'], y=df_imdb['Meta_score'])
#Replacing NaN in the ratings column with averages
avg_Meta_score = df_imdb["Meta_score"].astype("float").mean(axis=0)
df_imdb["Meta_score"].replace(np.nan,avg_Meta_score, inplace=True)
# Analysis of values in the 'Released_Year' column
df_imdb['Released_Year'].unique()
df_imdb['Series_Title'].loc[df_imdb['Released_Year']=='PG']
print(df_imdb['Released_Year'][803])
df_imdb['Released_Year'][803]='1995'
df_imdb.Released_Year.astype(int)
df_imdb['Released_Year'].dtype
# Converting the 'Runtime' column to numeric values
for i in range(len(df_imdb['Runtime'])):
    g = df_imdb.Runtime[i].split()
    g.remove('min')
    df_imdb.Runtime[i] = ''.join(g)
df_imdb['Runtime'].head()
# Identifing famous and unknown directors
df_imdb['Director'].value_counts()
df_imdb['Director'].unique()
df_imdb['F_Directors'] = np.NaN
df_imdb['F_Directors']=list(df_imdb['Director'].isin(Famous_directors))
#Replacing with numeric values
df_imdb.F_Directors.replace({True: 1, False: 0}, inplace = True)
# Identifing famous and unknown actors
df_imdb['F_star'] = np.NaN
#Replacing with numeric values
df_imdb['F_star']=list(df_imdb['Star1'].isin(famous_actors))
df_imdb.F_star.replace({True: 1, False: 0}, inplace = True)
df_imdb['F2_star'] = np.NaN
df_imdb['F2_star']=list(df_imdb['Star2'].isin(famous_actors))
df_imdb.F2_star.replace({True: 1, False: 0}, inplace = True)
df_imdb['F3_star'] = np.NaN
df_imdb['F3_star']=list(df_imdb['Star3'].isin(famous_actors))
df_imdb.F3_star.replace({True: 1, False: 0}, inplace = True)
df_imdb['F4_star'] = np.NaN
df_imdb['F4_star']=list(df_imdb['Star4'].isin(famous_actors))
df_imdb.F4_star.replace({True: 1, False: 0}, inplace = True)
# Removing unnecessary columns
del df_imdb['Star1']
del df_imdb['Star2']
del df_imdb['Star3']
del df_imdb['Star4']
del df_imdb['Director']
del df_imdb['Genre']
# Converting columns to a numeric format
df_imdb['Released_Year'] = df_imdb['Released_Year'].astype(str).astype(int)
df_imdb['Released_Year'].dtype
df_imdb['Gross'] = df_imdb['Gross'].astype(str).astype(int)
df_imdb['Gross'].dtype
df_imdb['Runtime'] = df_imdb['Runtime'].astype(str).astype(int)   
df_imdb['Runtime'].dtype
df_imdb['IMDB_Rating'].dtype
df_imdb['Meta_score'].dtype
df_imdb['No_of_Votes'].dtype
# Processing of the received table
df_imdb = df_imdb[[c for c in df_imdb if c not in ['Gross']] 
       + ['Gross']]
df_imdb.to_csv('C:/Users/user/Desktop/Data science/Мо/imdb_pre-processing.csv', encoding='utf-8', index=False)
#





