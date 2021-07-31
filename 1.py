#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[2]:


#credenciales de twitter
ckey = "JmEIPt9XHuVAvZP9R9I4UKXlz"
csecret = "JF8BKDmZ83OmFS2wgZPFl8WZCWJH9ZLD0iSKxpsdpuUuVWvRO6"
atoken = "1415798278688497666-Dny3zzgqLbE4d8efWyfsCSGnPPJxyR"
asecret = "mH3pMXpRyeerpHqkfBIh2JMIlkGpiPD2pUbLndGph0BXn"


# In[3]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''usuario y contraseña de couchdb'''
server = couchdb.Server('http://admin:Liz1234.@localhost:5984/') 
try:
    db = server.create('juegosolimpicoslocation')  # creo la base de datos juegos olimpicos
except:
    db = server['juegosolimpicoslocation']  #caso contrariosi existe se accede a la BDD
    
'''Busco tweets segun la locacion, en este caso Japon '''    

twitterStream.filter(locations=[124.03,22.24,155.52,47.21])  #tokyo
twitterStream.filter(locations=[120.93,23.21,152.43,47.92])  #kanazawua
twitterStream.filter(locations=[123.31,24.82,154.8,49.09]) #niigata


# In[ ]:




