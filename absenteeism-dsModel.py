#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


# Load the Data


# In[4]:


data_preprocessed = pd.read_csv('Absenteeism_preprocessed.csv')


# In[5]:


data_preprocessed.head()


# In[6]:


# logistic regression = type of classification : using classes to predict excessively Absent and Moderately absent


# In[7]:


# create tje targets


# In[8]:


data_preprocessed['Absenteeism Time in Hours'].median()


# In[9]:


# Class1 = Moderately absent <= 3 hrs   Class2 = Excessively absent (>= 4hrs) 


# In[10]:


# assigning value of 1 if an observation > 3hrs and 0 if Not. ML model


# In[11]:


targets = np.where(data_preprocessed['Absenteeism Time in Hours'] > 3,1,0)


# In[12]:


targets


# In[13]:


targets = np.where(data_preprocessed['Absenteeism Time in Hours'] > 
                   data_preprocessed['Absenteeism Time in Hours'].median(),1,0)


# In[14]:


data_preprocessed['Excessive Absenteeism'] = targets


# In[15]:


data_preprocessed.head()


# In[16]:


targets.sum()


# In[19]:


targets.shape[0]


# In[20]:


targets.sum() / targets.shape[0]


# In[21]:


#checkpoint


# In[22]:


data_with_targets = data_preprocessed.drop(['Absenteeism Time in Hours'], axis=1)


# In[23]:


data_with_targets is data_preprocessed


# In[24]:


data_with_targets.head()


# In[25]:


# select the inputs for the regression


# In[26]:


data_with_targets.shape


# In[29]:


data_with_targets.iloc[:,:13]


# In[65]:


data_with_targets.drop(['Date'], axis = 1)


# In[67]:


unscaled_inputs = data_with_targets.iloc[:,:-1]


# In[35]:


#standardize the data : Absenteeism_scaler will be used to substract the mean and divide by the SD variablewise(featurewise)


# In[69]:


from sklearn.preprocessing import StandardScaler
absenteeism_scaler = StandardScaler()


# In[57]:


absenteeism_scaler.fit(unscaled_inputs)


# In[50]:


df.drop(['ID'], axis = 1)  unscaled_inputs


# In[58]:


data_with_targets


# In[63]:


unscaled_inputs


# In[66]:


data_with_targets


# In[70]:


from sklearn.preprocessing import StandardScaler
absenteeism_scaler = StandardScaler()


# In[71]:


absenteeism_scaler.fit(unscaled_inputs)


# In[72]:


# whenever we get new data we know that the standardization information is contained in absenteeism_scaler - we prepared the scaling Mechanism


# In[75]:


scaled_inputs = absenteeism_scaler.transform(unscaled_inputs)


# In[76]:


scaled_inputs


# In[77]:


scaled_inputs.shape 


# In[78]:


# we have 700 observation and 14 features


# In[79]:


from sklearn.model_selection import train_test_split


# In[80]:


#SPlit array1: training dataset with inputs, array 2: training dataset with targets array3: test dataset with inputs, array4: test dataset with targets


# In[81]:


train_test_split(scaled_inputs, targets)  


# In[88]:


x_train, x_test, y_train, y_test = train_test_split(scaled_inputs, targets, train_size = 0.8, random_state = 20)


# In[89]:


print(x_train.shape, y_train.shape)


# In[90]:


print (x_test.shape, y_test.shape)


# In[87]:


# the inputs above contain 525 obsv along 14 features(variables) 1 target var,  the test 175 obsv along 14 features(variables) - target var -75% obser will help for trainign and 25% for testing


# In[91]:


#logistic regression with sklearn


# In[92]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# In[93]:


# training the model


# In[94]:


reg = LogisticRegression()


# In[95]:


reg.fit(x_train, y_train)


# In[96]:


reg.score(x_train,y_train)


# In[97]:


## manually check the accuracy


# In[100]:


model_outputs = reg.predict(x_train)
model_outputs


# In[101]:


y_train


# In[102]:


model_outputs == y_train


# In[105]:


np.sum((model_outputs==y_train))


# In[106]:


model_outputs.shape[0]


# In[107]:


np.sum((model_outputs==y_train))/model_outputs.shape[0]


# In[108]:


# finding the intercept and coefficients


# In[109]:


reg.intercept_


# In[110]:


reg.coef_


# In[117]:


unscaled_inputs.columns.values


# In[113]:


feature_name = unscaled_inputs.columns.values


# In[138]:


summary_table = pd.DataFrame (columns =['Feature name'], data = feature_name)
summary_table['coefficient'] = np.transpose(reg.coef_)
summary_table


# In[139]:


summary_table.index = summary_table.index + 1
summary_table.loc[0] = ['Intercept', reg.intercept_[0]]
summary_table = summary_table.sort_index()
summary_table


# In[141]:


summary_table


# In[144]:


summary_table.sort_values('Odds_ratio', ascending=False)


# In[ ]:




