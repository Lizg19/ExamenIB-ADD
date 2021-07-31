#!/usr/bin/env python
# coding: utf-8

# In[1]:


from facebook_scraper import get_posts
import couchdb
import json
import time


# In[2]:


#importa la libreria de pymongo para  usar el MongoCliente

from pymongo import MongoClient

#luego me conecto a MongoDB localmente
CLIENT_LIZ = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT_LIZ.admin.command('ismaster')
    print('MongoDB connection: Conexion exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexion fallida', cf)


# In[3]:


i=1
for post in get_posts('olympics', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    collection={}
     
    collection['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))
        


# In[4]:


#importa la libreria de pymongo para  usar el MongoCliente

from pymongo import MongoClient

#luego me conecto a MongoDB localmente
CLIENT_LIZ = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT_LIZ.admin.command('ismaster')
    print('MongoDB connection: Conexion exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexion fallida', cf)


# In[5]:



#Se crea la base de datos en MongoDB y se crea tambien la colleccion y en cada uno de ellos un documento que tiene un elemento de facebook
db=CLIENT_LIZ['juegosolimpicos2']
collection= db['facebook']


i=i
for post in get_posts('olympics', pages=1000, extra_info=True):
    collection.insert_one({'texto':post['text']})
    collection.insert_one({'date':mydate.timestamp()})
    collection.insert_one({'likes':post['likes']})
    collection.insert_one({'shares':post['shares']})
    


# In[ ]:




