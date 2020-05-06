#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[8]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]
y=[]
for i in x:
    z=m*x+c
    y.append(z)
print (y)


# In[9]:





# In[11]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]
y=[]
for i in x:
    z=m*i+c
    y.append(z)
print (y)


# In[12]:


import numpy as np
m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]
X = np.array(x)
Y = m*X + c
print (y)


# In[27]:


import matplotlib.pyplot as plt
import numpy as np
m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]
X = np.array(x)
Y = m*X + c
fig=plt.figure()
fig.add_axes([0,0,1,1])
plt.title('Scatter Plot Y versus X')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(X,Y)
plt.show()


# In[ ]:


()

