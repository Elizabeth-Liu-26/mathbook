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

# ```{admonition} Note
# :class: dropdown
# Note that we define positive/negative for the function at a give point ($x$). Whereas we define increasing/decreasing for the function on a given interval ([$x_1,x_2$])
# ```

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

{
    "tags": [
        "hide-input",
    ]
}


# In[2]:


fig, ax = plt.subplots()

x = np.arange(-2,6,.01)
y = .25*(x**3-6*x**2)+4
ax.plot(x,y,color="#999B84")

#adding lines at x=0, y=0
y_line = 0
ax.axhline(y_line, color='gray', linestyle='dashed')
x_line = 0
ax.axvline(x_line, color='gray', linestyle='dashed')

ax.text(-1.5, 2, "Pos. & Inc.", ha="center", va="center", rotation=70, size=10,
        bbox=dict(boxstyle="rarrow,pad=0.3", fc="#EFD9D1", ec="black", lw=1))

ax.text(1.65, 2.5, "Pos. & Dec.", ha="center", va="center", rotation=-58, size=10,
        bbox=dict(boxstyle="rarrow,pad=0.3", fc="#EFD9D1", ec="black", lw=1))

ax.text(2.4, -2.5, "Neg. & Dec.", ha="center", va="center", rotation=-58, size=10,
        bbox=dict(boxstyle="rarrow,pad=0.3", fc="#DDB7AB", ec="black", lw=1))

ax.text(5.4, -2.5, "Neg. & Inc.", ha="center", va="center", rotation=66, size=10,
        bbox=dict(boxstyle="rarrow,pad=0.3", fc="#DDB7AB", ec="black", lw=1))

plt.show()
{
    "tags": [
        "hide-input",
    ]
}


# ### First Derivative Test

# ```{admonition} Note
# :class: dropdown
# Remember that local maxmima and minima are critical numbers, but not all critical numbers need to be a maximum or minimum.
# ```

# In[ ]:




