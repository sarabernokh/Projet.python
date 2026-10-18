import sympy as sp
import numpy as np
# PARTIE 1 : CONSTANTES ET FONCTION (Issue de l'étape 1)
# Définition des constantes du CO2 et des conditions de l'étude
R = 8.314462618
a = 0.364
b = 4.267e-5
T = 320.0
v = 1.0e-3
# Définition de la fonction p_vdw qui calcule la pression de Van der Waals
def p_vdw(T, v):
    return (R * T) / (v - b) - a / (v**2)
# PARTIE 2 : CALCUL FORMEL AVEC SYMPY
# On déclare T, v, R, a, b comme des symboles mathématiques (des lettres)
Ts, vs, Rs, aa, bb = sp.symbols("T v R a b", positive=True)
# On écrit l'équation de Van der Waals avec ces symboles
P = Rs*Ts/(vs-bb) - aa/vs**2
# SymPy calcule la dérivée partielle de P par rapport à T, puis par rapport à v
dP_dT = sp.diff(P, Ts)
dP_dv = sp.diff(P, vs)
# On affiche les résultats simplifiés à l'écran
print("dP/dT =", sp.simplify(dP_dT))
print("dP/dv =", sp.simplify(dP_dv))
# PARTIE 3 : CALCUL NUMÉRIQUE (Différence finie centrée)
# On choisit le pas h = 0.01 K
h = 0.01
# Calcul de la dérivée numérique : (P(T+h) - P(T-h)) / (2*h)
dP_dT_num = (p_vdw(T+h,v)-p_vdw(T-h,v))/(2*h)
# Calcul de la dérivée exacte en utilisant la formule théorique R/(v-b)
dP_dT_exact = R/(v-b)
# Calcul de l'erreur relative entre la méthode numérique et la méthode exacte
erreur = abs(dP_dT_num-dP_dT_exact)/abs(dP_dT_exact)
# Affichage des résultats
print("Derivee numerique :", dP_dT_num)
print("Erreur relative :", erreur)