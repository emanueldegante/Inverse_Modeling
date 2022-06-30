# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:09:06 2021

@author: Emanuel
"""
import numpy as np
import math
import matplotlib.pyplot as plt

pi=math.pi

M=5.974e24
a=6371e3# Earth radius in meters
c=3485e3# Core Radius in meters
I_n=1.97142e24    #Kg 

#Normalization

Mo=M/1e20
Io=I_n/1e20

d_1=Mo    # Mass of earth
d_2=Io   # Moment of inertia

d=[[d_1],[d_2]]
d=np.array(d)

V1=(((4/3)*pi)*(c**3))
V2=((4/3)*pi)*((a**3)-(c**3))

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

G1=np.dot(G_T,G)

G1_inv= np.linalg.inv(G1) 

G_LSGI=np.dot(G1_inv,G_T)

G_LSGI_inv=np.linalg.inv(G_LSGI)

#Densities
densities_a=np.dot(G_LSGI,d)
density_1=densities_a[0][0]
density_2=densities_a[1][0]

#----------------------------Part B

G2=np.dot(G_T,d)

print('Insert Value of B')
B=float(input())        #Craeates vector 10^-2 to 10^30, 50 points
            
m_1=[[0,0],[0,0]]
m_1=np.array(m_1)

Lm=[]
Le=[]

I=np.eye(2)     #Identity Matrix 2x2

m_1=G1+(B**2*I)
m_inv=np.linalg.inv(m_1)
m=np.dot(m_inv,G2)

e=((np.dot(G,m))-d)*(1e20)

L2m=(np.sum(m**2))**(.5)
L2e=(np.sum(e**2))**(.5)
        

Lm=np.array(Lm)
m_1_1=m[0][0]
m_2_1=m[1][0]
e_1_1=e[0][0]
e_2_1=e[1][0]


p_1=m_1_1
p_2=m_2_1
Mn=M+(e_1_1)
In=I_n+(e_2_1)

#Part C 5 porcent tolerance mass

p_1_change=((density_1-p_1)/(density_1))*100
p_2_change=((density_2-p_2)/(density_2))*100
M_change=((M-Mn)/(M))*100
I_change=((I_n-In)/(I_n))*100

print(f'Porcentage of change in mass',M_change,'% with B =',B)
print(f'density 1 =', density_1 )
print(f'pensity 1 predicted =', p_1)
print(f'density 2 =', density_2)
print(f'density 2 predicted =',p_2 )
