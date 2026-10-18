import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
# --- 1. Définition des paramètres (Données du problème) ---
a = 0.364 # Constante de Van der Waals (Pa.m^6/mol^2)
b = 4.267e-5 # Covolume de Van der Waals (m^3/mol)
R = 8.314462618 # Constante des gaz parfaits (J/(mol.K))
T = 320.0 # Température (K)
v = 1.0e-3 # Volume molaire (m^3/mol)
#Calcule la différence Cp - Cv pour un gaz de Van der Waals en utilisant la relation de Mayer généralisée.
#Prend en entrée la température T (en K) et le volume molaire v (en m3/mol).
def cp_moins_cv_vdw(T, v):
    # 1. Dérivée partielle de P par rapport à T à v constant : (dP/dT)_v
    # D'après l'équation de Van der Waals, cette dérivée vaut R/(v-b)
    dpdt = R/(v-b)
    # 2. Dérivée partielle de P par rapport à v à T constant : (dP/dv)_T
    # La formule (donnée dans l'énoncé) est : -RT/(v-b)^2 + 2a/v^3
    dpdv = -R*T/(v-b)**2 + 2*a/v**3
    # 3. Sécurité : Vérification de la singularité (division par zéro)
    # Si dpdv est très proche de zéro (à 10^-12 près), la fraction va exploser.
    # np.isclose vérifie si la valeur est quasi-nulle.
    if np.any(np.isclose(dpdv, 0, atol=1e-12)):
        raise ValueError("Derivee en volume proche de zero")
    # 4. Application de la formule de Mayer généralisée
    # Formule : Cp - Cv = -T * ( (dP/dT)_v )^2 / (dP/dv)_T
    return -T*dpdt**2/dpdv
# On affiche la valeur théorique pour le gaz parfait (qui est simplement R)
print("Cp-Cv ideal :", R)
# On calcule et affiche la valeur pour le gaz de Van der Waals à T=320K et v=1e-3
print("Cp-Cv VdW :", cp_moins_cv_vdw(T,v))

# --- 2. Création des données pour le graphique ---
# On prend des volumes allant de 1.5 * b (pour éviter v=b) jusqu'à 5e-3
v_min = 1.5 * b 
v_max = 5.0e-3
volumes = np.linspace(v_min, v_max, 500)

# Calcul de Cp - Cv pour chaque volume
# On utilise une liste en compréhension pour gérer les éventuels "NaN"
cp_moins_cv = np.array([cp_moins_cv_vdw(T, v) for v in volumes])

# Valeur pour le gaz parfait (constante R)
cp_moins_cv_ideal = np.full_like(volumes, R)

# --- 3. Tracé du graphique ---
plt.figure(figsize=(8, 5))

# Courbe Van der Waals
plt.plot(volumes, cp_moins_cv, label="Van der Waals", color="blue")

# Ligne horizontale pour le gaz parfait
plt.plot(volumes, cp_moins_cv_ideal, label="Gaz parfait (R)", color="red", linestyle="--")

# Mise en forme
plt.xlabel("Volume molaire v (m³/mol)")
plt.ylabel("Cp - Cv (J/(mol.K))")
plt.title(f"Cp - Cv en fonction du volume à T = {T} K")
plt.ylim(0, 3 * R) # On limite l'axe Y pour ne pas être écrasé par les singularités
plt.xlim(v_min, v_max)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()