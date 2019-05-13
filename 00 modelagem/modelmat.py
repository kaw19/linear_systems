# -*- coding: utf-8 -*-
""" File...: .py
    Do.....:
    Date...: Sat May 11 19:05:27 2019
    @Author: kaw """

from numpy import arange
from pylab import plot, title, ylim, show, grid
from scipy.signal import lsim, lti

m = 1000.; ks = 2000.; kd = 500.
a1 = kd/m; a0 = ks/m; b1 = kd/m; b0 = ks/m
t = arange(0,10,0.1)
x = (t >= 1.) * 1.            # sinal de entrada: lombada de 1m de altura!
#plot(t,x,linewidth=2); title('Entrada: $x(t)$'); ylim((-0.2,1.2))

a = [1., a1, a0]   # coef.s do lado esquerdo (saída)
b = [b1, b0]       # coef.s do lado direito (entrada)
slit = lti(b,a)
y = lsim(slit, x, t)[1]
plot(t,y); grid(True)
show()
