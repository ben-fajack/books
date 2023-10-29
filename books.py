#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy.engine import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from urllib.parse import quote_plus
username = "root"
password = quote_plus("206!!Lbs") # Using the quote function to make the password compatible
db_name = "books"
connection = f'mysql+pymysql://{username}:{password}@localhost/{db_name}'


# In[2]:


import pandas as pd


# In[3]:


engine = create_engine(connection)


# In[4]:


engine


# In[5]:


# create connection to database via the engine
conn = engine.connect()


# In[10]:


# Read in the users data and preview
users = pd.read_csv('HR DB Data/users  - users.csv')
users.info()
users.head()


# In[11]:


q = '''DESCRIBE users;'''
describe = pd.read_sql(q, conn)
describe


# In[12]:


# Read in the authors data and preview
users = pd.read_csv('HR DB Data/authors - authors.csv')
users.info()
users.head()


# In[13]:


q = '''DESCRIBE authors;'''
describe = pd.read_sql(q, conn)
describe


# In[14]:


# Read in the books data and preview
users = pd.read_csv('HR DB Data/books - books.csv')
users.info()
users.head()


# In[15]:


q = '''DESCRIBE books;'''
describe = pd.read_sql(q, conn)
describe


# In[16]:


# Read in the favorites data and preview
users = pd.read_csv('HR DB Data/favorites - favorites.csv')
users.info()
users.head()


# In[17]:


q = '''DESCRIBE favorites;'''
describe = pd.read_sql(q, conn)
describe


# In[25]:


SELECT books.Title, favorites.users_id
FROM books
JOIN favorites ON books.id = favorites.books_id
WHERE favorites.users_id = 
    (SELECT users.id FROM users WHERE (users.last_name = "Doe" AND users.first_name = "John"));

