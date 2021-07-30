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
Pour ce TP, on va réaliser le traitement par Excel et non Python. On ne s'intéressera pas aux incertitudes de mesure.

## Mise en place du dispositif.
_Essayer d'éclairer au mieux le tube et placer un fond sombre derrière le tube pour améliorer la qualitée de l'image et ainsi mieux repérer la bille._

````{admonition} Mise en place
:class: tip

1. Préparer le dispositif pour la réalisation de chutes de billes d'acier dans de l'eau et leur visualisation à la caméra rapide. Remplir le tube de manière à pouvoir lâcher les billes à fleur d'eau à la main.
2. Placer la caméra à une distance adaptée pour que le tube soit dans son champ de vision. (_Le haut du tube n'est pas forcément utile puisqu'on s'intéresse au régime stationnaire._)
3. Régler la focale de la caméra (l'objectif se tourne) pour obtenir des images nettes de la chute des billes (et pas du panneau au fond par exemple!).
4. Pour l'enregistrement des vidéos, pensez à choisir des noms clairs au cas où vous devriez les réutiliser ensuite : y mettre le nom des binômes ainsi que le diamètre de la bille. L'arrêt de l'enregistrement se fait avec la touche ESC.
````

## Etude de la chute des billes

````{admonition} Manipulation
:class: tip
1. Pour chaque bille, réaliser l'acquition vidéo puis déterminer l'évolution de l'altitude $z(t)$ par relevé manuel.
2. Vérifier sur l'Atelier scientifique que le relevé est cohérent (qu'on atteint notamment un régime stationnaire) puis copier-coller les résultats expérimentaux sur une Feuille Excel.
3. Réaliser une régression linéaire sur $z(t)$ pour chaque bille pour obtenir la vitesse limite pour chaque diamètre. La fonction `DROITEREG(y, x)` renvoie la pente estimée par méthode des moindres carrés. Puisqu'on ne s'intéresse pas aux incertitudes graphiques, on ne réalisera qu'une vérification graphique sommaire.

````

````{admonition} Exploitation des résultats
:class: tip
1. Proposer une étude graphique (ou deux) permettant de valider l'un ou l'autre des modèles pour l'action de l'eau. Comparer les résultats obtenus à ceux attendu en calculant le nombre de Reynolds.
2. Si le modèle de frottements linéaires est validé: proposer une méthode basée sur le graphique précédent permettant de déterminer le coefficient de viscosité dynamique proposée. Le comparer à la valeur proposée.
3. Si le modèle de frottements quadratique n'est pas validé : proposer une méthode permettant de remonter au coefficient de trainée $C_x$. Le comparer aux valeurs lues sur le graphiques en [Annexe](chute).
````