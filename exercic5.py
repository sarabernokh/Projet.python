import sympy as sp
import numpy as np
R = 8.314462618
a = 0.364
b = 4.267e-5
T = 320.0
v = 1.0e-3
# Déclaration des symboles pour SymPy
Rs, Ts, vs, aa, bb = sp.symbols('Rs Ts vs aa bb')
P = Rs*Ts/(vs-bb) - aa/vs**2
dP_dT = sp.diff(P, Ts)
dP_dv = sp.diff(P, vs)
dvdT_P = sp.simplify(-dP_dT/dP_dv)
valeur = dvdT_P.subs({Ts:T, vs:v, Rs:R, aa:a, bb:b})
print("(dv/dT)P :", float(valeur))
print("(dS/dP)T :", -float(valeur))