import matplotlib.pyplot as plt
import numpy as np
# --- 1. Définition des paramètres (Données du problème) ---
a = 0.364
T = 320.0
v1 = 1.0e-3
v2 = 2.0e-3
# --- 2. Calcul manuel
# Calcul de Delta U pour Van der Waals
delta_U_vdw = a*(1/v1 - 1/v2)
# Calcul de Delta U pour le gaz parfait
delta_U_ideal = 0.0
# Affichage des resultats
print("Delta U Van der Waals (J/mol) :", delta_U_vdw)
print("Delta U Gaz Parfait (J/mol) :", delta_U_ideal)
# --- 3. Création des données ---
# Tableau des volumes v2 allant de v1 à 5e-3 (comme demandé dans l'énoncé)
# On crée un tableau de volumes allant de v1 à 5e-3
volumes = np.linspace(v1, 5e-3, 250)
# On calcule delta U pour TOUT le tableau 'volumes' (et non plus avec v2)
delta_U_vdw = a * (1/v1 - 1/volumes)
# Pour le gaz parfait, c'est un tableau de zéros de la même taille
delta_U_ideal = np.zeros_like(volumes)
# --- 4. Tracé du graphique
plt.plot(volumes, delta_U_vdw, label="Van der Waals")
plt.plot(volumes, delta_U_ideal, label="Gaz parfait", linestyle="--") 
plt.xlabel("Volume molaire v2 (m3/mol)")
plt.ylabel("Delta U (J/mol)")
plt.title(f"Détente isotherme a T = {T} K")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()