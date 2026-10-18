# Importation de la bibliothèque numpy pour les calculs numériques (tableaux, fonctions mathématiques)
import numpy as np
# --- DÉFINITION DES CONSTANTES ET DONNÉES ---
# Constante des gaz parfaits en J/(mol.K)
R = 8.314462618
# Paramètre a de l'équation de Van der Waals pour le CO2 en Pa.m^6/mol^2 (forces d'attraction)
a = 0.364
b = 4.267e-5
# Paramètre b de l'équation de Van der Waals pour le CO2 en m^3/mol (volume propre des molécules)
# --- DÉFINITION DES FONCTIONS D'ÉTAT ---
# Fonction calculant la pression pour un gaz parfait : P = RT/v
def p_ideal(T, v):
    # Retourne la pression en Pascal (Pa)
    return R*T/v
# Fonction calculant la pression pour un gaz de Van der Waals : P = RT/(v-b) - a/v^2
def p_vdw(T, v):
    # Vérification de sécurité : le volume molaire v doit être strictement supérieur au covolume b
    if np.any(np.asarray(v) <= b):
        # Si la condition n'est pas respectée, on lève une erreur pour arrêter le programme
        raise ValueError("Le volume doit etre superieur a b")
     # Retourne la pression calculée en Pascal (Pa)
    return R*T/(v-b) - a/v**2
# Définition de la température d'étude en Kelvin
T = 320.0
# Définition du volume molaire d'étude en m^3/mol (soit 1.00e-3)
v = 1.0e-3
# Calcul et affichage de la pression du gaz parfait
# On divise par 1e5 pour convertir les Pascals (Pa) en bars (bar)
print("Gaz parfait (bar) :", p_ideal(T,v)/1e5)
# Calcul et affichage de la pression du gaz de Van der Waals
# On divise également par 1e5 pour obtenir le résultat en bars
print("Van der Waals (bar) :", p_vdw(T,v)/1e5)  
# Importation de matplotlib.pyplot pour créer et afficher des graphiques
import matplotlib.pyplot as plt
# Création d'un tableau de 250 valeurs de volumes molaire allant de 5e-4 à 5e-3 m³/mol
# np.linspace(début, fin, nombre_de_points) génère des valeurs régulièrement espacées
volumes = np.linspace(5e-4, 5e-3, 250)
# Tracé de la courbe du gaz parfait
# En abscisse : les volumes. En ordonnée : la pression convertie en bar (/1e5)
# label="..." définit le nom qui apparaîtra dans la légende
plt.plot(volumes, p_ideal(T,volumes)/1e5, label="Gaz parfait")
# Tracé de la courbe de Van der Waals sur le même graphique avec les mêmes conversions
plt.plot(volumes, p_vdw(T,volumes)/1e5, label="Van der Waals")
# Ajout du titre de l'axe des abscisses (X) avec son unité
plt.xlabel("Volume molaire (m3/mol)")
# Ajout du titre de l'axe des ordonnées (Y) avec son unité
plt.ylabel("Pression (bar)")
# Ajout du titre principal du graphique, indiquant la condition d'étude (isotherme à T=320K)
plt.title("Isotherme à T = 320 K")
# Activation de la grille pour faciliter la lecture des valeurs sur le graphique
plt.grid(True)
# Affichage de la légende (qui reprend les textes définis dans les fonctions plt.plot)
plt.legend()
# Ajuste automatiquement les marges pour que les titres et les labels ne soient pas coupés
plt.tight_layout()
# Commande finale qui ouvre la fenêtre affichant le graphique
plt.show()