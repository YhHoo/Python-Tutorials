'''
THIS IS NumPy and Matplotlib.pyplot examples****
'''

import numpy as np
import matplotlib.pyplot as plt

N = 8
# create an array of 8 zeros
y = np.zeros(N)
# create 2 arrays , both with 8 elements in btw 0 to 10
x1 = np.linspace(0, 10, N) # 10 is included
x2 = np.linspace(0, 10, N, endpoint=False) # 10 is not included
# plot lines to axes
plt.plot(x1, y, 'ro') 
plt.plot(x2, y+0.5, 'bo')
# set limit of y axes
plt.ylim(-0.5, 1)
#this is a MUST to show them 
plt.show()

'''
[CONSOLE]
the 2 lines are plotted in a same graph in one window
'''
# if add these 2 lines right before line 15 and 16 respectively
# first digit 2 is no_of_rows, 
# second digit 1 is no_of_columns,
# third digit 1 or 2 is plot no
plt.subplot(211)
plt.subplot(212)

'''
[CONSOLE]
the 2 lines are plotted in 2 graphs in one window
Basically it is to let u set how many graphs to be plot in one windows 
and how they should be positioned
'''

# now add in fig, ax = plt.subplots()

fig, ax = plt.subplots()
ax.plot(x1, y, 'ro')
ax.set_title('Graph 1')

fig, ax = plt.subplots()
ax.plot(x2, y+0.5, 'bo')
ax.set_title('Graph 2')

plt.ylim(-0.5, 2)
plt.show()

'''
[CONSOLE]
this will plot the 2 graphs in 2 windows
'''