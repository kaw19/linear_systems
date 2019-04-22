# -*- coding: utf-8 -*-
""" File...: .py
    Do.....:   
    Date...: Sun Mar 24 07:15:13 2019
    @Author: kaw """

# Solução do item 2
import numpy as np
# Entrada de dados via teclado
R = input('Valor para os Resistores (kOhm): '); R = np.ones(3)*R*10e3
C = input('Valor para os Capacitores  (uF): '); C = np.ones(3)*C*1e-6

# cálculo dos coef.s da E.C.
a = 1.
b = (1./R[0] + 1./R[1] + 1./R[2])/C[1]         # b = 3/(RC)   para R1=R2=R3 e C1=C2
c = 1./(R[0] * R[1] * C[0] * C[1])             # c = 1/(RC)^2 para R1=R2=R3 e C1=C2
PC = np.array([a, b, c])                       # polinômio característico 
print PC

# cálculo das raízes do P.C.
rc = np.roots(PC)                              # raízes características
print rc,
if np.real(rc[0]) < 0 and np.real(rc[1]) < 0:  # raízes no SPE --> Ex.: 1k e 5uF
    print "SLITC estável."                     # b^2 > 4ac e -b > sqrt(discriminante)
elif any(np.real(rc)>0) or rc[0]==rc[1]:       # raízes no SPD ou raízes repetidas 
    print "SLITC instável."                    # -b > sqrt(discr.) ou b^2 = 4ac 
else:
    print "SLITC marginalmente estável."       # raízes distintas no eixo vertical
    