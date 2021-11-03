#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[15]:


raw_csv_data = pd.read_csv(r'C:\Users\Charlgia\Downloads\Absenteeism_data.csv')


# In[16]:


raw_csv_data


# In[17]:


df = raw_csv_data.copy()


# In[18]:


df


# In[19]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None


# In[20]:


display(df)


# In[21]:


df.info()


# In[22]:


df.drop(['ID'], axis = 1)


# In[23]:


df


# In[24]:


df = df.drop(['ID'], axis = 1)


# In[25]:


df


# In[26]:


raw_csv_data


# In[27]:


df = raw_csv_data


# In[28]:


df


# In[29]:


df['Reason for Absence']


# In[30]:


df['Reason for Absence'].min()


# In[31]:


df['Reason for Absence'].max()


# In[32]:


pd.unique(df['Reason for Absence'])


# In[34]:


df['Reason for Absence'].unique()


# In[35]:


len(df['Reason for Absence'].unique())


# In[36]:


sorted(df['Reason for Absence'].unique())


# In[37]:


reason_columns = pd.get_dummies(df['Reason for Absence'])


# In[38]:


reason_columns


# In[39]:


reason_columns['check'] = reason_columns.sum(axis=1)
reason_columns


# In[44]:


reason_columns['check'].sum(axis=0)


# In[49]:


reason_columns 

reason_columns
# In[51]:


reason_columns = pd.get_dummies(df['reason for Absence'], drop_first = True)


# In[53]:


reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)


# In[54]:


reason_columns


# In[55]:


df.columns.values


# In[56]:


reason_columns.columns.values


# In[58]:


df = df.drop(['Reason for Absence'], axis = 1)


# In[59]:


df


# In[61]:


reason_columns.loc[:,15:17]


# In[62]:


reason_type_1 = reason_columns.loc[:,1:14].max(axis=1)
reason_type_2 = reason_columns.loc[:,15:17].max(axis=1)
reason_type_3 = reason_columns.loc[:,18:21].max(axis=1)
reason_type_4 = reason_columns.loc[:,22:].max(axis=1)


# In[63]:


reason_type_1


# In[64]:


reason_type_2


# In[65]:


reason_type_3


# In[66]:


reason_type_4


# In[67]:


df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis = 1)


# In[68]:


df


# In[70]:


df.columns.values


# In[71]:


column_names = ['ID', 'Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']


# In[72]:


df.columns = column_names


# In[73]:


df.head()


# In[77]:


column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[75]:


df.head()


# In[78]:


column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[79]:


df = df[column_names_reordered]


# In[80]:


df.head()


# In[90]:


df_reason_mod = df.copy()


# In[91]:


df_reason_mod


# In[85]:


df_reason_mod['Date']


# In[87]:


type(df_reason_mod['Date'][0])


# In[88]:


df_reason_mod['Date']= pd.to_datetime(df_reason_mod['Date'], format)


# In[89]:


df_reason_mod['Date']


# In[93]:


df_reason_mod['Date']= pd.to_datetime(df_reason_mod['Date'], format = '%d/%m/%Y')


# In[94]:


df_reason_mod['Date']


# In[95]:


type(df_reason_mod['Date'][0])


# In[96]:


df_reason_mod.info()


# In[100]:


df_reason_mod['Date'][0]


# In[101]:


df_reason_mod['Date'][0].month


# In[102]:


list_months = []
list_months


# In[103]:


df_reason_mod.shape


# In[104]:


for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)


# In[105]:


list_months


# In[106]:


len(list_months)


# In[107]:


df_reason_mod['Month Value'] = list_months


# In[108]:


df_reason_mod.head(20)


# In[109]:


df_reason_mod['Date'][699].weekday()


# In[110]:


df_reason_mod['Date'][699]


# In[111]:


def date_to_weekday(date_value):
    return date_value.weekday()


# In[113]:


df_reason_mod['Day of the week'] = df_reason_mod['Date'].apply(date_to_weekday)


# In[114]:


df_reason_mod.head()


# In[120]:


type(df_reason_mod['Transportation Expense'][0])


# In[121]:


df_reason_mod['Education'].unique()


# In[122]:


df_reason_mod['Education'].value_counts()


# In[123]:


display(df_reason_mod)


# In[124]:


df_reason_mod['Education'].unique()


# In[125]:


df_reason_mod['Education'].value_counts()


# In[126]:


df_reason_mod['Education'] = df_reason_mod['Education'].map({1:0,2:1,3:1,4:1})


# In[127]:


df_reason_mod['Education'].unique()


# In[128]:


df_reason_mod['Education'].value_counts()


# In[129]:


display(df_reason_mod)


# In[130]:


df_preprocessed = df_reason_mod.copy()
df_preprocessed.head(10)


# In[132]:


df_preprocessed.to_csv('C:/Users/Charlgia/Absenteeism_preprocessed.csv', index=False)


# In[ ]:




