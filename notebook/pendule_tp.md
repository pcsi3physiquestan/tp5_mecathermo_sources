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
_Note : Pour ce TP, on n'étudiera pas les incertitudes de mesure. Le but est d'observer les caractéristiques d'un oscillateur ainsi que les méthodes expérimentales et numériques permettant de remonter à ses caractéristiques._

__Il est inutile de télécharger le notebook. Les exploitations qui ne peuvent être réalisées dans l'Atelier scientifique devront être réalisées sous Excel.__

## Étalonnage du dispositif de mesure

On pourra acquérir la tension $u(t)$ à l'aide d'une console d'acquisition numérique et le signal sera alors traité avec le logiciel `Atelier Scientifique`.
* Installer l'alimentation du potentiomètre et brancher la borne de mesure (avec sa référence) sur la console d'acquisition.
* La relation entre la tension $u(t)$ et l'angle $\theta(t)$ est affine. Grâce à deux mesures conjointes de l'angle et de la tension, déterminer la relation entre les deux grandeurs.
* Créer une grandeur correspondant à l'angle dans le logiciel (`Traitement des données`).

````{note}
Une partie du traitement numérique se fera directement dans l'Atelier scientifique. Ainsi, après la première acquisition de $u(t)$ (en régime harmonique) et le calcul de $\theta(t)$, il faudra :
* réaliser le lissage de la grandeur (créer une grandeur `thetal` dans `Traitement des données - Lissage`. On choisira la méthode BSPLine en ajustant le degré des polynômes à l'oeil.)
* calculer la dérivée numérique (`Traitement des données - Dérivation`)

__Après chaque nouvelle acquisition, il n'est pas nécessaire de reconfigurer les grandeurs mais il faudra relancer manuellement le calcul (`Traitement des données`).__

````

## Etude sans frottements

Dans cette partie on n'imposera aucun frottement (ni solide, ni fluide). Les choix des paramètres d'acquisition sont laissés libres. Il est juste conseillé de ne pas prendre une fréquence d'échantillonnage trop grande pour éviter les bruits électromagnétiques.

### Cas harmonique
````{admonition} Manipulation
:class: tip
1. Réaliser l'acquisition de $\theta(t)$ pour le pendule sans frottements avec une amplitude d'oscillations faible (environ 10 à $20^{\circ}$). On placer la masse à l'extrémité du pendule – veillez à bien la fixer et on mesurera précisément sa position.
2. Vérifier sur l'allure temporelle (lissée) de l'angle et de la vitesse angulaire que l'hypothèse harmonique est acceptable visuellement.

````

````{admonition} Influence du moment d'inertie
:class: tip
Proposer un protocole expérimental permettant de vérifier la relation entre la période et le moment d'inertie donné dans l'étude préliminaire. Procéder à la vérification de cette relation.

__La masse linéaire n'étant pas connue, il faudra réaliser une mesure préliminaire statique de $\lambda$.__
````
```{margin}
Les incertitudes n'étant pas demandée, la vérification restera sommaire. On rappelle néamoins que le seul modèle graphique qu'on peut valider à l'oeil est la droite.
```

````{admonition} Etude de l'harmonicité du système
:class: tip
Un modèle un peu plus complet propose une relation entre l'amplitude des oscillations et la période:

\begin{align}
	T =T_0 ( 1+ \frac{\theta_0^2}{16})& &\textrm{(formule de Borda) }
\end{align}

où $T_0$ est la période isochrone.

1. Procéder à la mesure de la période des oscillations pour des amplitudes grandissantes jusqu'à $90^{\circ}$ à moment d'inertie constant (placer le masse au milieu de la tige et vérifier qu'elle est bien fixée). Observe-t-on un isochronisme des oscillations ?
2. Vérifier si la loi de Borda est conforme aux mesures.
````
```{margin}
Les incertitudes n'étant pas demandée, la vérification restera sommaire. On rappelle néamoins que le seul modèle graphique qu'on peut valider à l'oeil est la droite.
```

### Cas d'un amortissement fluide

On réalisera un amortissement fluide en remplissant grâce à un système magnétique qui, part induction (cf. cours) occasionne un couple assimilable à des frottements fluides linéaires.

````{admonition} Etude du tracé temporel
 :class: tip
1. Obtenir l'évolution temporelle de l'angle et de la vitesse angulaire et l'analyser. On déterminera, au moyen de méthode qu'on précisera la pseudo-période et le décrément logarithmique associé à ce régime.
2. Déduire des mesures précédentes la pulsation propre et le coefficient d'amortissement du système. Comparer ces résultats au cas sans frottement.
 
 ````

### Cas d'un amortissement solide

Retirer les aimants et serrer la vis permettant la mise en place des frottements solides. On réglera ces frottements de manière à pouvoir observer plusieurs oscillations. On continuera à observer des oscillations aux petits mouvements.

````{admonition} Etude du mouvement
:class: tip
1. Obtenir l'évolution temporelle du système. Observe-t-on les caractéristiques attendues? Mettre en évidence les différences fondamentales avec le cas de frottements fluides.
2. Par une méthode qu'on précisera, remonter au couple de frottements solides.

````
