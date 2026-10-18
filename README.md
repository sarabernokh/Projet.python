# Travail Rendu : Équations d'état et Isotherme (Gaz Parfait vs Van der Waals)
# Partie 1 — Construire les deux équations d’état
## 1. Objectif du projet
Ce script Python a pour but de modéliser et de comparer le comportement d'une mole de dioxyde de carbone (CO2) en utilisant deux modèles thermodynamiques :
- Le modèle du Gaz Parfait (GP)
- Le modèle de Van der Waals (VdW)

L'étude se concentre sur une isotherme à T = 320 K pour un volume molaire variant de 5e-4 à 5e-3 m3/mol.

## 2. Description du Code
Le script est structuré en plusieurs étapes logiques :

### A. Importation des bibliothèques et constantes
Nous utilisons numpy pour les calculs numériques (vecteurs) et matplotlib.pyplot pour le tracé graphique.
Les constantes spécifiques au CO2 fournies dans l'énoncé ont été définies :
- R = 8.314462618 J/(mol.K)
- a = 0.364 Pa.m6/mol2
- b = 4.267e-5 m3/mol

### B. Définition des fonctions d'état
Nous avons créé deux fonctions prenant en argument la température T et le volume molaire v :

1. p_ideal(T, v) : Calcule la pression via la loi des gaz parfaits P = RT/v.
2. p_vdw(T, v) : Calcule la pression via l'équation de Van der Waals P = RT/(v-b) - a/v^2.
   - Sécurité : Une vérification (if statement) a été ajoutée pour s'assurer que le volume v reste strictement supérieur à b (covolume), afin d'éviter une division par zéro.

### C. Calculs et Vérifications
Le script effectue un calcul pour une valeur spécifique : v = 1.00e-3 m3/mol à T = 320 K.
Il affiche les résultats en Pascals (Pa) convertis en bar (1 bar = 10^5 Pa) pour les deux modèles.

### D. Tracé Graphique
Nous générons un vecteur de volumes (linspace) allant de 5e-4 à 5e-3.
Le graphique superpose les deux courbes :
- Axe X : Volume molaire (m3/mol)
- Axe Y : Pression (bar)
Le graphique inclut une grille, une légende et des titres conformes aux consignes.

## 3. Interprétation des Résultats

- À grand volume (v élevé) : Les deux courbes se superposent. L'effet du volume des molécules (b) et des forces attractives (a) devient négligeable devant le volume total. Le gaz réel se comporte comme un gaz parfait.
- À faible volume (v proche de b) : Les courbes divergent fortement. La pression calculée par Van der Waals devient beaucoup plus grande que celle du gaz parfait (voire tend vers l'infini). Cela s'explique par le terme répulsif RT/(v-b) qui modélise le fait que les molécules ne peuvent pas s'interpénétrer (volume minimal b).

## 4. Fichiers fournis
Le code source complet de ce projet se trouve dans le fichier séparé nommé *exercic1.py*

Pour exécuter le programme et générer le graphique, il suffit de lancer la commande :
python exercic1.py

# Étape 3 — Dérivation symbolique et vérification numérique

Ce document explique la démarche pour vérifier la relation de Maxwell issue de l'énergie libre de Helmholtz (\(F\)) :
\[
 \left(\frac{\partial S}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v 
\]

## 1. Démonstration Analytique

Nous cherchons à démontrer les dérivées théoriques de la pression par rapport à la température à volume constant \((\partial P/\partial T)_v\) pour deux modèles de gaz.

### A. Gaz Parfait
L'équation d'état est :
\[
 P = \frac{RT}{v} 
\]
En dérivant par rapport à \(T\) (en gardant \(v\) constant) :
\[
 \left(\frac{\partial P}{\partial T}\right)_v = \frac{\partial}{\partial T}\left(\frac{RT}{v}\right) = \frac{R}{v} 
\]
**Résultat :** \(\frac{R}{v}\)

### B. Gaz de Van der Waals
L'équation d'état est :
\[
 P = \frac{RT}{v - b} - \frac{a}{v^2} 
\]
En dérivant par rapport à \(T\) (les termes \(a\) et \(b\) sont des constantes, donc la dérivée du terme \(-a/v^2\) est nulle) :
\[
 \left(\frac{\partial P}{\partial T}\right)_v = \frac{\partial}{\partial T}\left(\frac{RT}{v - b}\right) = \frac{R}{v - b} 
\]
**Résultat :** \(\frac{R}{v - b}\)

## 2. Analyse Dimensionnelle (Unités)

Quelle est l'unité de \((\partial P/\partial T)_v\) ?

*   La pression \(P\) s'exprime en **Pascals (Pa)** ou \(N/m^2\).
*   La température \(T\) s'exprime en **Kelvin (K)**.

L'unité de la dérivée est donc le **Pa/K** (Pascal par Kelvin) ou \(N \cdot m^{-2} \cdot K^{-1}\).

**Cohérence avec l'entropie :**
La relation de Maxwell stipule que \((\partial S/\partial v)_T = (\partial P/\partial T)_v\).
*   \(S\) (entropie) est en \(J/K\).
*   \(v\) (volume massique ou molaire) est en \(m^3/mol\) ou \(m^3/kg\).
*   L'unité de \((\partial S/\partial v)_T\) est donc \(\frac{J/K}{m^3} = J \cdot K^{-1} \cdot m^{-3}\).
*   Or, \(1 \, J = 1 \, N \cdot m\). Donc \(J \cdot m^{-3} = N \cdot m \cdot m^{-3} = N \cdot m^{-2} = Pa\).
*   Les deux membres ont bien la dimension **Pa/K**.

## 3. Vérification Numérique (Python)

Nous avons utilisé deux méthodes pour valider ces dérivées :

1.  **Calcul Formel (SymPy) :** Le script Python utilise `sp.diff(P, Ts)` pour dériver symboliquement l'équation d'état de Van der Waals. Cela confirme le résultat analytique : `R/(v-b)`
2.  **Différences Finies Centrées :** Pour vérifier numériquement, nous approximons la dérivée par :
    \[
 \left(\frac{\partial P}{\partial T}\right)_v \approx \frac{P(T+h, v) - P(T-h, v)}{2h} 
\]
    Avec un pas \(h = 0.01\) K.

### Comparaison des résultats
*   **Analytique :** \(\frac{R}{v-b}\)
*   **SymPy :** Retourne exactement la même expression.
*   **Numérique :** La valeur calculée par différence finie est très proche de la valeur exacte (l'erreur relative est infime).

## 4. Discussion sur le pas \(h\) (Différences Finies)

L'explication de l'erreur observée lors de la variation du pas \(h\) est cruciale :

*   **Si \(h\) est trop grand :** L'approximation de la tangente par une corde est mauvaise. L'erreur de troncature (erreur mathématique due à l'approximation) augmente. On s'éloigne de la vraie dérivée.
*   **Si \(h\) est trop petit :** On est confronté aux erreurs d'arrondi de la machine (précision flottante). La soustraction \(P(T+h) - P(T-h)\) implique de soustraire deux nombres très proches, ce qui amplifie les erreurs numériques (perte de chiffres significatifs).
*   **Compromis :** Il existe un \(h\) optimal (souvent autour de \(10^{-5}\) à \(10^{-8}\) selon l'échelle) qui minimise l'erreur totale (troncature + arrondi). Ici, \(h=0.01\) est un choix raisonnable pour observer la convergence.

## 5. Fichiers fournis
Le code source complet de ce projet se trouve dans le fichier séparé nommé *exercic2.py*

Pour exécuter le programme et générer le graphique, il suffit de lancer la commande :
python exercic2.py