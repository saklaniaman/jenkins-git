#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:



dataset = pd.read_csv("diabetes.csv")


# In[3]:


dataset.head()


# In[4]:


x= dataset.iloc[ : , 0:8]


# In[5]:


x.head()


# In[6]:


y= dataset['Outcome']


# In[7]:


y.head() 


# In[8]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[9]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# In[10]:


model = LogisticRegression()

model.fit(X_train, y_train)


# In[11]:



y_pred = model.predict(X_test)

accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)


# In[ ]:





# In[ ]:




