#!/usr/bin/env python
# coding: utf-8

# In[47]:


from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


# In[48]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[49]:


get_ipython().run_line_magic('sql', 'postgresql://postgres:postgres@127.0.0.1:6543/postgres_db')


# # How many Ads per segment?

# In[141]:


df_ad_segments = get_ipython().run_line_magic('sql', 'select seg.segment,count(distinct ads.ad_id) number_of_adsfrom data_ads adsinner join data_segmentation seg on ads.user_id = seg.user_idgroup by segment;')

df_ad_segments


# In[153]:


df = DataFrame(df_ad_segments);
df.columns = ('segment', 'ads')
# df_ad_segments

df.head()


# In[162]:


fig = plt.figure(figsize=(10,6));
df.groupby('segment').ads.sum().sort_values().plot.barh(ylim=0, title='Segments by Ad occurences');
plt.xlabel('Number of Ads', fontsize = 10);
plt.ylabel('Segment', fontsize = 10);
plt.show();


# # How many Ads/Users per Category?

# In[178]:


df_ad_categories = get_ipython().run_line_magic('sql', 'select categ.category_name as category,count(distinct ads.ad_id) number_of_ads,count(distinct ads.user_id) number_of_usersfrom data_ads adsinner join data_categories categ on ads.category_id = categ.category_idgroup by categ.category_nameorder by 2 desc;')

df_ad_categories


# In[180]:


dfC = DataFrame(df_ad_categories);
dfC.columns = ('category', 'ads', 'users')
dfC.head()


# In[181]:


fig = plt.figure(figsize=(10,6));
dfC.groupby('category').ads.sum().sort_values().plot.barh(ylim=0, title='Categories by Ad occurences');
plt.xlabel('Number of Ads', fontsize = 10);
plt.ylabel('Category', fontsize = 10);
plt.show();


# In[182]:


fig = plt.figure(figsize=(10,6));
dfC.groupby('category').users.sum().sort_values().plot.barh(ylim=0, title='Categories by USer occurences');
plt.xlabel('Number of Users', fontsize = 10);
plt.ylabel('Category', fontsize = 10);
plt.show();

