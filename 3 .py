#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importa la libreria de pymongo para  usar el MongoCliente

from pymongo import MongoClient

#luego me conecto a MongoDB localmente
CLIENT_LIZ = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT_LIZ.admin.command('ismaster')
    print('MongoDB connection: Conexion exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexion fallida', cf)


# In[2]:


#Importo laslibrerias necesarias para hacer webscraping, la de json  para convertir archivos

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[13]:


response = requests.get('https://www.elcomercio.com/deportes/')
soup = BeautifulSoup(response.content, "lxml")


Noticia=[]



post_noticia=soup.find_all("p", class_="article-highlighted__description")

for element in post_noticia:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Noticia.append(limpio.strip())
    

print(post_noticia)


print(Noticia)




# In[14]:


noticias=pd.DataFrame({'Noticia':Noticia})


# In[16]:


print(noticias)


# In[18]:


db=CLIENT_LIZ['juegosolimpicos']
collection= db['noticias']

collection.insert_one({'Noticia':Noticia})


# In[26]:





# In[ ]:




