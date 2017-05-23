#!/usr/bin/env python

# import standard libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from scipy.stats import beta
from scipy.special import gamma, binom
import scipy.integrate as integrate

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.zeros(0)
y = np.zeros(0)
z = np.zeros(0)
x =  np.concatenate((np.ones(167), np.zeros(167), np.random.rand(167*2), 
    np.random.rand(167*2)), axis=0)
y =  np.concatenate((np.random.rand(167*2), np.zeros(167), np.ones(167), 
    np.random.rand(167*2)), axis=0)
z =  np.concatenate((np.random.rand(167*2), np.random.rand(167*2), 
    np.ones(167), np.zeros(167)), axis=0)
ax.scatter(x[0:1000],y[0:1000],z[0:1000])
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
phi = (np.random.rand(1000)-0.5)*2*np.pi
theta = np.random.rand(1000)*np.pi
r = np.ones(1000)
x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)
ax.scatter(x,y,z)
plt.show()

plt.plot(r*np.cos(theta)*np.cos(phi), r*np.cos(theta)*np.sin(phi))
plt.show()


# Problem 4 Supernovae


rho = np.arange(0,1,0.01)
m = 10
n = 4

def probdata(rho,m,n):
    return (rho**n)*(1-rho)**(m-n) * 
        ((gamma(m-n+1)*gamma(n+1))/(gamma(m+2)))**(-1)

def probdata2(rho,m,n):
    return beta.pdf(rho, n+1, m-n+1)

plt.figure()
plt.plot(probdata(rho,10,4))
plt.plot(probdata(rho,10,5))
plt.show()

# not sure about part c)