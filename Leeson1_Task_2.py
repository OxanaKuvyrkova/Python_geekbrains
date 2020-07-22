#!/usr/bin/env python
# coding: utf-8

# In[199]:


import pandas as pd
import numpy as np


# In[200]:


a = {
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
}

authors = pd.DataFrame(a)

authors


# In[201]:


b = {
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
}

book = pd.DataFrame(b)

book


# In[202]:


authors_price = pd.merge(authors, book, on='author_id', how='outer')
authors_price


# In[203]:


top5 = (authors_price.sort_values(by="price")).tail()
top5.set_index("author_id", inplace=True)


# In[204]:


top5


# In[205]:


authors_stat = top5.groupby("author_name")
authors_stat


# In[206]:


authors_min = pd.DataFrame(authors_stat["price"].min())
authors_min.reset_index(inplace=True)
authors_min


# In[207]:


authors_max = pd.DataFrame(authors_stat["price"].max())
authors_max.reset_index(inplace=True)
authors_max


# In[208]:


authors_mean = pd.DataFrame(authors_stat["price"].mean())
authors_mean.reset_index(inplace=True)
authors_mean


# In[209]:


authors_stat = pd.merge(authors_min, authors_max,  on='author_name', how='inner')
authors_stat = pd.merge(authors_stat, authors_mean,  on='author_name', how='inner')
authors_stat


# In[210]:


authors_stat.rename(columns={'price_x': 'price_min', 'price_y': 'price_max', 'price': 'price_mean'}, inplace=True)
authors_stat


# In[211]:


authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price


# In[212]:


authors_price.groupby(['author_name', 'cover'])['price'].sum()


# In[213]:


book_info = pd.pivot_table(authors_price,  values='price', index='author_name', columns='cover', aggfunc=np.sum)
book_info


# In[214]:


book_info['мягкая'].fillna(0, inplace=True)
book_info['твердая'].fillna(0, inplace=True)
book_info


# In[215]:


book_info.to_pickle("h.pkl")
book_info = pd.read_pickle("h.pkl")
book_info


# In[ ]:




