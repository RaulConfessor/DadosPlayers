#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pyodbc
import pymssql as sql
import warnings
warnings.filterwarnings("ignore")


# In[84]:


df =  pd.read_csv('DataSets/players_20.csv')
df


# In[85]:


#Removendo colunas desnecessárias 
df = df.iloc[:,:17]
df = df.drop(['player_url', 'dob'], axis=1)
df.head()


# In[86]:


lista = list(df.columns)
lista


# In[87]:


#Alterando o posicionamento da coluna Overall e Potential
if 'overall' in lista and 'overall' != lista[4]:
    colOverall = df['overall']
    del df['overall']
    lista.insert(4,'overall')
    df.insert(4, 'overall', colOverall)
elif lista[4] == 'overall':
    print('A coluna "overall" já está na posição correta.')
else:
    print('A coluna "overall" não está presente no DataFrame.')


# In[88]:


if 'potential'in lista and 'potential' != lista[5]:
    colPot = df['potential']
    del df['potential']
    df.insert(5, 'potential', colPot)
    lista.insert(5, 'potential')
elif lista[5] == 'potential':
    print('A coluna "overall" já está na posição correta.')
else:
    print('A coluna "overall" não está presente no DataFrame.')


# In[89]:


#Ordenando por potencial
potential = df[df['age'] < 25]
potential = potential.sort_values(by='potential',ascending=False)


potential.head(20)


# In[90]:


brasil = df[df['nationality'] == 'Brazil']
brasilTop = brasil.head(10)
brasilTop


# In[91]:


brasil = df[df['nationality'] == 'Brazil']
brasilTop = brasil.head(10)
brasilTop


# In[92]:


brOld = brasil[brasil['age']>25]
brOld = brOld.head(15)

brYoung = brasil[brasil['age'] <=25]
brYoung = brYoung.sort_values(by='potential', ascending=False).head(15)


# In[93]:


#Comparação entre os principais jogadores dos Brasil x Promissores

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(15, 6, forward=True)
lenOld = np.arange(len(brOld['short_name']))
size = 0.35
plt.tight_layout()
#x = braOld['short_name']
x1 = lenOld - size /2
x2 = lenOld + (size + 0.07) / 2
oldOver = ax[0].bar(x1, brOld['overall'],width=size, label= "Overall")
oldPot = ax[0].bar(x2, brOld['potential'],width=size, label= 'Potencial')
ax[0].set_xticks(lenOld)
ax[0].set_xticklabels(brOld['short_name'])
ax[0].tick_params(axis='x', rotation=45)
ax[0].legend()
for i, v in enumerate(brOld['overall']):
    ax[0].text(x1[i], v + 0.02, str(v), ha='center', va='bottom')
    
for i, v in enumerate(brOld['potential']):
    ax[0].text(x2[i], v + 0.02, str(v), ha='center', va='bottom')
    
    
    
lenYoung = np.arange(len(brOld['short_name']))
size = 0.35
x1= lenYoung - size/2
x2= lenYoung + (size +0.06)/2
youngOver = ax[1].bar(x1, brYoung['overall'], width=size, label= 'Overall')
youngPot = ax[1].bar(x2, brYoung['potential'], width=size, label= 'Potential')
ax[1].set_xticks(lenYoung)
ax[1].set_xticklabels(brYoung['short_name'])
ax[1].tick_params(axis='x', rotation=45)
ax[1].legend()

for i, v in enumerate(brYoung['overall']):
    ax[1].text(x1[i], v + 0.02, str(v), ha='center', va='bottom')
    
for i, v in enumerate(brYoung['potential']):
    ax[1].text(x2[i], v + 0.02, str(v), ha='center', va='bottom')


# In[94]:


plt.figure(figsize=(8, 8))
nation_counts = df['nationality'].value_counts().head(10)
size = nation_counts.values
labels =  nation_counts.index
plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Principais Nacionalidades')


# In[95]:


df.head()


# In[107]:


connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-1VPOTLF\SQLEXPRESS;DATABASE=FIFA;Trusted_Connection=yes;')
print('BANCO CONECTADO')


# In[108]:


cursor = connect.cursor()

InsertQuery = "INSERT INTO PLAYERS (ID_PLAYERS, SHORT_NAME, LONG_NAME, AGE, OVERALL, POTENTIAL, HEIGHT_CM, WEIGHT_KG, NATIONALITY, CLUB, VALUE_EUR, WAGE_EUR, POSITIONS, PREFERRED_FOOT, INTERNAT_REPUTION) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

for index, row in df.iterrows():
    DataTuple = (
        row['sofifa_id'], row['short_name'], row['long_name'], row['age'], row['overall'], row['potential'], row['height_cm'],
        row['weight_kg'], row['nationality'], row['club'], row['value_eur'], row['wage_eur'], row['player_positions'], row['preferred_foot'],
        row['international_reputation']
    )
    cursor.execute(InsertQuery, DataTuple)
    
    connect.commit()


# In[105]:


cursor.close()
connect.close()


# In[ ]:




