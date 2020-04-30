#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:45:53 2020

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
    gamma=0.1
    return [xprime, -np.sin(x)-gamma*xprime] #pendule simple amorti



#Conditions initiales (sous la forme [x, \dot(x)])
y0 = [[-np.pi/8.0,0]]#,[-np.pi/8,0.30],[-3/4*np.pi,0],[-np.pi+0.001,0.0],[-np.pi/8,1.0]]

solution = []
for ci in y0:
    solution.append(inte.odeint(sys,ci,t))

for sol in solution: # tracé du portrait de phase
    plt.plot(sol[:,0],sol[:,1])
#plt.axis()
plt.axis([-1/2*np.pi, 1/2*np.pi, -0.3, 0.3])
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\dot\theta/\omega_0$')
plt.legend(y0)
plt.savefig('portrait_phase_amortit.pdf') 
