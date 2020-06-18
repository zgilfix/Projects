# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 08:22:59 2020

@author: zgilf
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import time
import imageio

df = pd.read_csv("C:/Users/zgilf/Documents/Projects/batches.csv")


#Plotting Function: Get counts up to batch # and plot top 15
#To do: Remove axes labels and put into graph
def draw_barchart(batch):
    fig, ax = plt.subplots(figsize=(15, 8))
    df2=df[df["Batch"]<=batch]
    df3=df2.groupby(['Site'])['Site'].count().reset_index(name ='Count')
    dff = df3.sort_values(by='Count', ascending=True).tail(15)
    ax.clear
    ax.barh(dff['Site'], dff['Count'], color="orange")
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(.8, .2, batch, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Articles', transform=ax.transAxes, size=12, color='#777777')
    ax.text(0, 1.12, 'Most Read Batch Sites',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    dx = dff['Count'].max() / 200
    for i, (count, site) in enumerate(zip(dff['Count'], dff['Site'])):
        ax.text(count-dx, i-.2, site, size=14, weight=600, ha='right', va='bottom')
        ax.text(count+dx, i,     f'{count:,.0f}',  size=14, ha='left',  va='center')
    plt.box(False)
    

images = []
for i in range(1,75):
    draw_barchart(i)
    plt.savefig('C:/Users/zgilf/Documents/Projects/Batch/batch' + str(i) + '.png')
    images.append(imageio.imread('C:/Users/zgilf/Documents/Projects/Batch/batch' + str(i) + '.png'))

imageio.mimsave('C:/Users/zgilf/Documents/Projects/Batch/batch_slow.gif', images,duration=.9)
imageio.mimsave('C:/Users/zgilf/Documents/Projects/Batch/batch_fast.gif', images)


#record above, crop, slow down, save as gif
  

#fig, ax = plt.subplots(figsize=(15, 8))
#animator = animation.FuncAnimation(fig, draw_barchart, frames=range(3,7))
#plt.show()
#animator.save("C:/Users/zgilf/Documents/Projects/batches_plot.mp4")





