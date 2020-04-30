#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:01:04 2020

@author: nicolas
"""


import numpy as np
import matplotlib.pyplot as plt 
import scipy.integrate as inte
plt.rcParams['text.usetex'] = True

#Discrétisation du temps


nombre_pas = 20000
t_final = 300
t = np.linspace(-2*np.pi,t_final,num=nombre_pas)


def sys(y,t):
     x, xprime = y
     epsilon=0.1
     return [xprime, (epsilon-x**2)*xprime -x]
 
    
#Conditions initiales (sous la forme [x, \dot(x)])
y0 = [[0.001,0], [np.pi/2, 0.7]]

solution = []
for ci in y0:
    solution.append(inte.odeint(sys,ci,t))

for sol in solution: # tracé du portrait de phase
    plt.plot(sol[:,0],sol[:,1])
plt.axis('equal')
plt.xlim(-2*np.pi, 2*np.pi)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\theta/\omega_0$')
plt.legend(y0)
plt.savefig('portrait_phase_van_der_pol.pdf')  

