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

(chute)=
# Préliminaires

```{attention}
Au cours de cette séance de 4h, vous effectuerez deux TP différents de 1h30: 2 binômes travailleront sur la chute d'une bille dans un fluide et 2 binômes sur les oscillations mécaniques forcées (\cref{cha_oscillations_forc_es}).

Vous devez échanger de postes au bout de 1h30. La dernière heure permettra de mettre en commun et exploiter les résultats. L'organisation du TP doit être prévue à l'avance. Chaque binôme étudiera la chute de 3 billes (sur 5) dans le même tube. Il faut que les deux binômes travaillant le même poste se répartissent les billes de manière à avoir des résultats pour toutes les billes.

```

## Position du problème
Nous allons étudier les mouvements de chute dans un fluide (eau) de billes en acier de différents diamètres. La chute étant trop rapide pour être étudiée à l'oeil ou avec une caméra classique (24 images/s), l'enregistrement vidéo se fera à l'aide d'une caméra rapide (400 images/s). L'utilisation du logiciel de traitement CINERIS est expliqué au [ici](cineris). 

Nous pourrons alors analyser finement les différentes étapes du mouvement des billes et de quantifier les frottements auquel elles sont soumises. On mettra en commun les résultats des deux binômes, obtenus pour des rayons de billes différents. Les deux binômes devront se mettre d'accord sur le choix des billes utilisés.

## Modélisation théorique

### Effets de la viscosité du fluide
Les mouvements dans les fluides peuvent être caractérisés par un nombre sans dimension, appelée nombre de REYNOLDS, indiquant si le mouvement est dominé par des effets convectifs ou de diffusion visqueuse. Ce nombre compare la vitesse du mobile à une vitesse caractéristique liée aux effets de viscosité:

\begin{equation}
  Re = \frac{vD}{\eta/\rho_f}
\end{equation}

où D est une longueur caractéristique du mobile (on peut choisir ici le diamètre de la bille), v sa vitesse, $\rho_f$ la masse volumique du fluide environnant (pour l'eau $\rho_f=10^3 kg.m^{-3}$ ) et $\eta$ sa viscosité (1mPl pour l'eau ou Pl est le Poiseuille, unité SI de la viscosité).

### Force visqueuse et coefficient de trainée Cx

La valeur du nombre de Reynolds permet de déterminer si:

* le mouvement dans le fluide est dominé par les forces visqueuses (pour Re<1): les frottements fluides linéaires sont alors en vitesse: $\overrightarrow{F}=-6 \pi \eta r \overrightarrow{v}$ (loi de Stokes) avec r le rayon de la bille.
* ou si au contraire ce sont les effets convectifs qui dominent (pour Re>1000): les frottements fluides sont alors quadratiques en vitesse: $\overrightarrow{F}=-[\frac{1}{2}\rho_f (\pi r^2)C_x]v \overrightarrow{v}$ où $C_x$ est un coefficient sans dimension appelé coefficient de trainée.

````{margin} 
Ces formules ne sont évidemment valables que pour une bille.

````

En régime permanent, les deux autres forces (le poids et la poussée d'Archimède) compensent la force de frottement fluides et on observe une vitesse limite.

* Cas linéaires: $6\pi \eta r v_{lim}=4\pi r^3 \rho_f g(1- \frac{1}{d})$.
* Cas quadratiques: $[\frac{1}{2}\rho_f (\pi r^2)C_x ]v_{lim}^2 =4\pi r^3 \rho_f g(1- \frac{1}{d})$

On peut trouver dans la littérature des études sur le coefficient de trainée en fonction du nombre de Reynolds (noté $C_D$ en anglais). En [voici](reynolds) une utile pour nous.

```{figure} ./images/Mecanique_Bille_Cx.jpg
:name: reynolds
:align: center
Etude du coefficient de trainée
```