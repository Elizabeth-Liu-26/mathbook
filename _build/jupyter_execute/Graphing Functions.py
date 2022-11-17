#!/usr/bin/env python
# coding: utf-8

# ### Using Derivatives to Graph Functions

# #### First, some definitions

# ```{dropdown} The function is <b> positive </b>.
# For a given $x$ , $f(x) > 0$. aka the value of the function, at that point, is a positive number. 
# 
# Similarly, if the function is <b> negative </b>, the function is a negative number. (For a given $x$ , $f(x) < 0$.
# ```

# ```{dropdown} The function is <b> increasing </b>.
# For a given interval, as $x$ increases (gets bigger), $f(x)$ also increases (gets bigger). "climbing uphill" 
# 
# Similarly, if the function is <b> decreasing </b>, as $x$ increases (gets bigger), $f(x)$ decreases (gets smaller). "going downhill"
# ```

# ```{note}
# Note that we define positive/negative for the function at a give point ($x$). Whereas we define increasing/decreasing for the function on a given interval ([$x_1,x_2$])
# ```

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.arange(-2,6,.01)
y = .25*(x**3-6*x**2)+4


# In[3]:


plt.plot(x,y)
plt.ylabel('some numbers')
plt.show()


# In[ ]:




