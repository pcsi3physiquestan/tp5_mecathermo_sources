---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  split_at_heading: true
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Travaux pratiques

## Dispositif expérimental

L'appareil utilisé comprend une éprouvette en verre renforcé contenant l'hexafluorure de soufre (SF6), transparent, à étudier. On utilise ce fluide car il est inerte et le gaz se liquéfie à des pressions et températures raisonnables (point critique: $T_c=45,5 ^{\circ}\rm{C}$ et $p_c=37,6 \rm{bar}$).

L'éprouvette est fixée sur une chambre de pression contenant du mercure et fermée par un piston. Le volant situé sous l'appareil agit sur le piston et entraîne le déplacement du mercure dans l'éprouvette, ce qui fait varier le volume de SF6. Un manomètre indique la pression exercée sur le SF6 (en bars, $1 \rm{bar}=10^5 \rm{Pa}$). Les graduations gravées sur l'éprouvette permettent la lecture du volume occupé par le SF6 (en $\rm{cm^3}$).

Une cuve transparente est placée autour de l'éprouvette. De l'eau provenant d'un bain thermostaté circule dans la cuve, permettant ainsi d'ajuster la température de l'éprouvette à celle du bain. Un thermomètre monté sur le bain thermostaté mesure la température du bain (en $^{\circ}\rm{C}$), et donc, lorsque l'équilibre thermique est atteint, celle du fluide étudié. Le réglage de la température se fait en maintenant appuyée la touche $\vartheta$ du bain thermostaté et en réglant la température à la valeur voulue grâce à la molette. Relâcher alors la touche $\vartheta$, l'afficheur indique la température actuelle du bain, qui évoluera vers la valeur demandée.

## Relevé des mesures
Nous allons étudier l'évolution du SF 6 à température T donnée (isothermes), imposée par le bain thermostaté.

````{important}
Il est important de respecté un ordre croissant des températures car il est beaucoup plus simple et rapide de chauffer le bain thermostaté que de le refroidir.

````

Les mesures effectuées par les deux binômes doivent être mises en commun et consignées dans le même fichier Excel dédié: télécharger le fichier correspondant depuis le site et l'enregistrer sous le nouveau nom `NOM1NOM2NOM3NOM4.xls` (où NOMi sont les noms de famille des personnes composant les binômes).

````{attention}
Pour éviter tout risque d'explosion: NE JAMAIS DéPASSER LA PRESSION MAXIMALE DE 37 BAR. Tourner très lentement le volant en vérifiant en permanence l'augmentation de pression, NOTAMMENT lorsque le SF6 est sous forme liquide.

````

````{admonition} Relevé des isothermes
:class: tip
1. Pour chaque température, vous devrez réaliser l'acquisition du volume de sF6 et de la pression associée. Réaliser une compression lente pour rester à l'équilibre, notamment lorsqu'il y a équilibre-vapeur.
2. Observer à chaque fois l'état du fluide et la reporter dans la feuille Excel (G: Gaz, L: Liquide, LG : Liquide-Gaz).
3. Continuer à comprimer le SF6 (ne pas dépasser 37 bars).
````

## Exploitation des résultats
### Isothermes d'Andrews

````{admonition} Exploitation
:class: tip
1. Dans la feuille de calcul d'Excel `` Isothermes '', observer le tracé du réseau des isothermes OBTENUES PAR LES DEUX BINÔMES dans le diagramme de Watt (p en fonction de V).
2. Commenter l'allure du réseau d'isothermes obtenu. Indiquer sur le graphique les différentes phases présentes (gaz, liquide, ou les deux).
3. Comparer les variations de pression avec le volume lorsque le SF 6 est sous forme uniquement liquide et lorsqu'il est sous forme uniquement gazeuse. Proposer une explication.
````

### Pression de vapeur saturante

Lorsque le gaz est en équilibre avec le liquide, on dit que le gaz (ou vapeur) est une vapeur saturante. Sa pression est appelée pression de vapeur saturante, notée $p_{sat} (T)$, pression maximale que peut atteindre une vapeur et qui correspond également à la pression à laquelle s'effectue le changement d'état. La pression de vapeur saturante dépend de la température et suit la loi de RANKINE, où T désigne la température absolue, en kelvins:

$$
p_{sat}=a e^{-bT}
$$


````{admonition} Exploitation
:class: tip
1. Relever la valeur de la pression de vapeur saturante psat pour l'ensemble des 6 isothermes et noter les résultats dans la feuille de calcul `` Psat '' prévue dans le fichier Excel.
2. Sous Excel, tracer $\ln(p_{sat})$ en fonction de T et déterminer si la loi de RANKINE est vérifiée.
````

### Equation d'état du gaz

#### Développement du Viriel

Dans la feuille de calcul Equation d'état, les calculs de pV et de 1/V lorsque le SF 6 est sous forme gazeuse s'effectuent automatiquement. Il faudra néamoins supprimer les parties correspondant au liquide et liquide-gaz.

````{admonition} Exploitation
:class: tip
1. En utilisant les courbes obtenues, préciser si le SF6 peut être modélisé par un gaz parfait.
````
Une modélisation plus fine que celle du gaz parfait permet d'obtenir l'équation d'état suivante, par un développement en séries en 1/V (développement du Viriel) au premier ordre:

$$
pV = nRT (1+\frac{B(T)}{V})
$$

où n est la quantité de matière dans le volume V, R la constante des gaz parfaits ($R=8,314 \rm{J.K^{-1}.mol^{-1}}$), T la température absolue en kelvins et B une fonction de T, dépendant du fluide.

````{admonition} Exploitation
:class: tip
1. Sous Excel, pour chaque isotherme, ajuster les points de mesure par une courbe de tendance linéaire et obtenir l'équation de la droite correspondante (de la forme y=bx+a ou y représente pV et x représente 1/V).
2. Imprimer le graphe de pV en fonction de 1/V contenant les régressions linéaires. Le gaz considéré suit-il l'équation d'état proposée avec le développement du Viriel?
3. Dans la feuille de calcul `` n et rho '' du fichier Excel, Noter les pentes et ordonnées à l'origine. Ne pas oublier de préciser les unités pour chaque colonne. Quelle est la dimension de $B(T)$?
````

#### Quantité de matière
````{admonition} Exploitation
:class: tip
1. Qu'attend-on des valeurs de $n$ trouvées pour chaque isothermes?
2. Déduire des régressions linéaires la quantité de matière n pour chaque isothermes. Recopier les résultats dans le compte-rendu. Les résultats semblent-ils cohérents?
3. Calculer la quantité de matière moyenne nmoy, utiliser les formules du polycopié sur les incertitudes (incertitude de Type A) pour estimer l'incertitude de la quantité de matière.
````

#### Dimension des molécules de SF6.

Pour un gaz donné, le coefficient B dépend de la température T, mais également de la quantité de matière n (on dit qu'il est extensif). Nous allons donc plutôt étudier le coefficient B molaire, $b_{mol} = B/n_{moy}$, ne dépendant plus de n (intensif). On peut montrer que $b_{mol}$ peut s'écrire en première approximation:

\begin{equation}
  b_{mol}(T)=b_0 + b_1 \frac{1}{T}
\end{equation}  

où $b_0$ dépend du "rayon" $\rho$ de la molécule et $b_1$ de l'énergie potentielle d'interaction entre deux molécules.

Dans une modélisation de type "sphères dures" : $b_0 =(2/3) \pi \rho^3 N_A$ avec $N_A$ la constante d'Avogadro.

````{admonition} Exploitation
:class: tip
Pour chaque isotherme, déduire B(T) des droites de régression. Déterminer alors $b_{mol}(T)$. Tracer $b_{mol}$ en fonction de 1/T (avec T en kelvin) et ajuster les points par une droite de régression. En déduire le rayon $\rho$ des molécules de SF6. Comparer avec la valeur tabulée: $6,39.10^{-10}\rm{m}$.