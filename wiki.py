
# coding: utf-8

# # Useful links, tutorials, and reads when starting a Bioinformatics project #
# 
# This simple page contain links to various sources that are good to know
# before and during a Bioinformatics project. It is written using
# [Markdown](https://bitbucket.org/tutorials/markdowndemo) which is
# simple mark-up language to produce a richer experience over a simple
# text file.
# 
# 
# 
# 
# ### Installation ###
# 
# 1. Create an SNIC user at https://supr.snic.se/person/register/new/? this will allow you
# access to the SuperComputing Resources available to the
# group. Currently, around 300,000 core hours/month.
#        * When you have gotten the SUPR account apply to membership in all the projects: https://supr.snic.se/project/request/?search=wallner
# 
# 
# 
# # Learn some stuff #
# 
# 
# 
# ### Python ###
# 
# 
# 
# We are still using Python 2, mostly because it works and we have not seen any reason to move to Python 3.
# These quite old articles still hold:
# 
# * https://learntocodewith.me/programming/python/python-2-vs-python-3/
# * http://blog.thezerobit.com/2014/05/25/python-3-is-killing-python.html
# 
# Code Academy is good place to learn python interactively. 
# 
# * https://www.codecademy.com/learn/learn-python
# 
# We can also recommend the Google Python Class that contains Videos lectures as well.
# 
# * https://developers.google.com/edu/python/
# 
# 
# ### Specific python modules ###
# 
# Here is a list of the most common modules we are using. They can be installed using for instance:
# 
# ```
# pip install scipy
# pip install scikit-learn
# pip install seaborn
# 
# ```
# 
# [SciPy](https://www.scipy.org) (pronounced “Sigh Pie”) contains these core packages:
# 
# * NumPy - Base N-dimensional array package
# * SciPy library - Fundamental library for scientific computing
# * Matplotlib - Comprehensive 2D Plotting
# * IPython - Enhanced Interactive Console
# * Sympy - Symbolic mathematics
# * pandas - Data structures & analysis
# 
# 
# 
# [scikit-learn](http://scikit-learn.org/) is the package we use to do machine learning.
# 
# [scikit-learn tutorials](http://scikit-learn.org/stable/tutorial/index.html) contains an introduction to scikit-learn. 
# 
# [seaborn](https://seaborn.pydata.org) is used to produce publication grade plots with minimal effort.
# 
# 
# 
# 
# ### Problems and comments ###
# 
# Send an email to bjornw_AT_ifm.liu.se
# 
# 
# 
# 

# 
# ### Jupyter ###
# Jupyter is a notebook system that enables you to write code, run it and document it in an iteractive environment. It is strongly suggesed that you use it.
# 
# 
# #### securing the notebook ####
# From: http://jupyter-notebook.readthedocs.io/en/stable/public_server.html#notebook-server-security
# 
# First generate a config file you do not already have one.
# ```
# jupyter notebook --generate-config
# 
# ```
# Prepare a hashed password using the following code:

# In[8]:

from notebook.auth import passwd
passwd()


# In[2]:

get_ipython().magic(u'matplotlib notebook')

import pandas as pd
import numpy as np
import matplotlib

from matplotlib import pyplot as plt
import seaborn as sns

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot(); plt.legend(loc='best')

