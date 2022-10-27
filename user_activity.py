#!/usr/bin/env python3

# Python 3.9.5

# user_activity.py

# Dependencies
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'C:\\Users\\user\\...'
os.chdir(path)

# Import data
usage = pd.read_csv('user_activity.csv')
# Check data
usage.head()

# Data has the following structure
# user,time,count,hour
# 80,07:45,30,7
# 39,08:15,48,8
# ...

# Aggregate data
table = pd.pivot_table(usage, index='hour', aggfunc=np.sum)

# Plot data to a vertical bar chart.
table.plot.bar()
plt.show()
