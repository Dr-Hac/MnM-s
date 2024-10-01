"""
NAME: M&M.py
PURPOSE: plot a 3D graph in matplotlib with MnM's.csv data
DATE: 5/4/24
PROGRAMMER: Dr Hac
"""

import matplotlib.pyplot as plt, pandas as pd, numpy as np

plt.style.use('ggplot')

# set projection type to 3 dimensional
ax = plt.axes(projection='3d')

# read data from the MnM's.csv file
MnM = pd.read_csv("MnM's.csv", usecols=['Color', 'Normal', 'Peanut', 'Peanutbutter', 'Total'], index_col=0)

# use total category in MnM dataframe to sort data
MnM = MnM.sort_values('Total', ascending=True)
print(MnM)

for color in range(len(MnM.index)):
    for col in range(len(MnM.columns) - 1):
        if MnM.index[color] != 'Broken' and MnM.index[color] != 'Total':
            # add bar to the graph
            ax.bar3d(col - 0.075, color - 0.25, 1, dx=0.25, dy=0.25, dz=MnM.loc[MnM.index[color], MnM.columns[col]], shade=True, color=MnM.index[color], alpha=0.8)
            # add text to the bar displaying its length
            ax.text(col, color, MnM.loc[MnM.index[color], MnM.columns[col]] + 1, str(MnM.loc[MnM.index[color], MnM.columns[col]]))
        else:
            # add bar to the graph
            ax.bar3d(col - 0.075, color - 0.25, 1, dx=0.25, dy=0.25, dz=MnM.loc[MnM.index[color], MnM.columns[col]], shade=True, color='Black', alpha=0.8)
            # add text to the bar displaying its length
            ax.text(col, color, MnM.loc[MnM.index[color], MnM.columns[col]] + 1, str(MnM.loc[MnM.index[color], MnM.columns[col]]))

# set labels of x, y, and z axis
ax.set_xlabel('Type')
ax.set_ylabel('Color')
ax.set_zlabel('Amount')

# set names of ticks on x, y, and z planes
ax.set_xticks(range(len(MnM.columns) - 1), MnM.columns.drop('Total'), minor=False)
ax.set_yticks(range(len(MnM.index)), MnM.index, minor=False)
ax.set_zticks(range(1, 21), range(1, 21))

# change viewing angle on the bar chart
ax.view_init(ax.elev + 2, ax.azim + 14)

# show the bar chart
plt.show()
