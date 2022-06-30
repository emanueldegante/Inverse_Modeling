# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:29:35 2021

@author: Emanuel
"""
#Assigment 1, Resistivity, Archies Law and Current Densities

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('4512_lab_1.csv')
y_2=dataset.iloc[:,1].values             #  Resistivity of Samples
x_1=dataset.iloc[:,2].values             #  porosities
p_w=float(input())                       #  p_w = ohm-m
print("Resistivity of Water", p_w)
y_1=y_2/p_w                              #  Formation Factor

#=================================================Linear Regression Manually
x=np.log10(x_1)                          #  log
x_ave=np.mean(x)
x_dif=x-x_ave
x_dif_sq=(x_dif**2)
x_sum=np.sum(x_dif_sq)

y=np.log10(y_1)
y_ave=np.mean(y)
y_dif=y-y_ave
y_dif_sq=(y_dif**2)
y_sum=np.sum(y_dif_sq)

#Pearsons Correlation Coefficient.
xy_dif=(x_dif)*(y_dif)
sum_xy_dif=np.sum(xy_dif)
r=(sum_xy_dif)/(((x_sum)*(y_sum))**.5)

n=len(x)                       # Number of values
sy=(y_sum/(n-1))**.5
sx=(x_sum/(n-1))**.5

b=r*sy/sx
m=b                            #    Slope
a=y_ave-b*x_ave
a_cart=10**a                   #    Y intersection

#=====================Log_log-Plot
x_plot=10**x
y_plot=10**y
plt.scatter(x_plot, y_plot, color= 'red' )     # Plot
plt.yscale('log')
plt.xscale('log')
plt.title("Archie's Law")
plt.xlabel('Log Porosity')
plt.ylabel('Log F')
plt.grid(True)
plt.xlim([.001,10])
plt.ylim([.1,1000])
plt.show()
#==========================Draw Slope
por=np.arange(0.01,1.01,.01)
log_a=np.log10(a_cart)
log_por=np.log10(por)
flog=log_a+(b*log_por)
f=10**flog

#===================Predicted Plot
plt.scatter(x_plot, y_plot, color= 'red', s=100, label="Scattered Data" )     # Plot
plt.plot(por,f,color='blue', label='Predicted regression')
plt.yscale('log')
plt.xscale('log')
plt.title("Archie's Law")
plt.xlabel('Log Porosity')
plt.ylabel('Log F')
plt.grid(True)
plt.xlim([.001,10])
plt.ylim([.1,1000])
plt.legend()
plt.show()

#How to calculate porosity, From Archies law
print("Input New Resistivity")
prn=int(input())
print("Input new water Resistivity")
pwn=int(input())
por=((prn/pwn)/a_cart)**(1/(b))
print("predicted Porosity", por)
