#!/usr/bin/env python
import numpy as np

def sigma(x):
    return 1./(1+np.exp(-x))
   


z0 = Wxh*x[0] + Bh
h0 = sigma(z0)

z1 = Wxh * x[1] + Whh*h0 + Bh
h1 = sigma(z1)

z2 = Wxh * x[2] + Whh*h1 + Bh
h2 = sigma(z2)

h2
