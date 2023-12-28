#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df =  pd.read_csv('DataSets/players_20.csv')
df


# In[3]:


#Removendo colunas desnecessárias 
df = df.iloc[:,:17]
df = df.drop(['player_url', 'dob'], axis=1)
df.head()


# In[4]:


lista = list(df.columns)
lista


# In[5]:


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


# In[6]:


if 'potential'in lista and 'potential' != lista[5]:
    colPot = df['potential']
    del df['potential']
    df.insert(5, 'potential', colPot)
    lista.insert(5, 'potential')
elif lista[5] == 'potential':
    print('A coluna "overall" já está na posição correta.')
else:
    print('A coluna "overall" não está presente no DataFrame.')


# In[7]:


#Ordenando por potencial
potential = df[df['age'] < 25]
potential = potential.sort_values(by='potential',ascending=False)


potential.head(20)


# In[8]:


brasil = df[df['nationality'] == 'Brazil']
brasilTop = brasil.head(10)
brasilTop


# In[9]:


brasil = df[df['nationality'] == 'Brazil']
brasilTop = brasil.head(10)
brasilTop


# In[12]:


brOld = brasil[brasil['age']>25]
brOld = brOld.head(15)

brYoung = brasil[brasil['age'] <=25]
brYoung = brYoung.sort_values(by='potential', ascending=False).head(15)


# In[13]:


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


# In[14]:


plt.figure(figsize=(8, 8))
nation_counts = df['nationality'].value_counts().head(10)
size = nation_counts.values
labels =  nation_counts.index
plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Principais Nacionalidades')


# In[ ]:




