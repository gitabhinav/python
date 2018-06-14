
# coding: utf-8

# In[34]:

import logging
import mysql.connector as db


# In[43]:

logging.basicConfig(level='DEBUG')


# In[44]:

log = logging.getLogger()


# In[54]:

class db_ops:
    def __init__(self,user,password,host,port, database, log):
        self.user= user
        self.passw = password
        self.host = host
        self.port = port
        self.db = database
        self.conn = db.connection
        self.log = log
    
    def connect(self):
        try:
            self.conn = db.connect(user = self.user, password = self.passw,host = self.host, port = self.port, database = self.db)
            return self.conn
        except db.Error as err:
            # raise some error 
            self.log.error(err)
    
    def close(self):
        self.conn.commit()
        self.conn.close()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



