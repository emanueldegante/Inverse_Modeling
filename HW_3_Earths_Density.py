# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:48:39 2021

@author: Emanuel
"""
import math
import numpy as np

pi=math.pi

M=5.974e24
a=6371e3# Earth radius in meters
c=3485e3# Core Radius in meters

#I/a**2= 1.97142e24 kg where a is the earth's radius

I_n=1.97142e24    #Kg 

#Normalization

Mo=M/1e20
Io=I_n/1e20

d_1=Mo    # Mass of earth
d_2=Io   # Moment of inertia

d=[[d_1],[d_2]]
d=np.array(d)

G_1_1=(((4/3)*pi)*(c**3))
G_1_2=((4/3)*pi)*((a**3)-(c**3))
G_2_1=(((8/15)*pi)*(c**5))/(a**2)
G_2_2=((8/15)*pi)*((a**5)-(c**5))/(a**2)

G = [[G_1_1, G_1_2], 
    [G_2_1, G_2_2]]

G=np.array(G)

G=G/(1e20)

#Transpose of a Matrix using Numpy
G_T=G.transpose()

#Least Squares Generalized Inverse
G1=np.dot(G_T,G)

G1_inv= np.linalg.inv(G1) 

G_LSGI=np.dot(G1_inv,G_T)

G_LSGI_inv=np.linalg.inv(G_LSGI)


X=np.dot(G_LSGI,d)
print(X)

