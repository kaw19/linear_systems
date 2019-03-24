# -*- coding: utf-8 -*-
""" File...: ampop2.py
    Do.....: Traça o lugar das raízes do circ. com ampop do Roteiro 03-EDLCCs  
    Date...: Sun Mar 24 07:15:13 2019
    @Author: kaw """

# Solução do item 2
import numpy as np; import pylab as plt
rc = []
a = 1.
for r in range(1,10001,100):
  R = np.ones(3)*r*10e3
  for c in range(1,10001,100):
    C = np.ones(3)*c*1e-6
    b = (1./R[0] + 1./R[1] + 1./R[2])/C[1]
    c = 1./(R[0] * R[1] * C[0] * C[1])
    PC = np.array([a, b, c])                       # polinômio característico 
    rc.append(np.complex(np.roots(PC)[0]))         # raízes características
    rc.append(np.complex(np.roots(PC)[1]))         # raízes características
  print '.',
x = np.array(np.real(rc))
y = np.array(np.imag(rc))
plt.plot(x,y)
plt.show()