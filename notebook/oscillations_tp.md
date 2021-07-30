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

## Etude statique
On rappelle que la loi de Hooke prévoit que l'allongement du ressort (écart à la longueur à vide du ressort) est proportionnel à la force appliquée à ses extrémités. La constante k de proportionnalité est appelée constante de raideur du ressort.

````{admonition} Manipulatino
:class: tip
1. Proposer une étude statique permettant de vérifier la validité de la loi de Hooke puis, le cas échéant de remonter à la constante de raideur k et à la valeur de la longueur à vide. Procéder alors à la mesure des deux caractéristiques du ressort.
````

## Oscillations forcées

````{admonition} Etude de la réponse fréquentielle
:class: tip
1. Accrocher la tige au ressort et enfiler (dans cet ordre) le couvercle du tube à remplir d'eau, deux masses, la palette moyenne et visser le boulon d'arrêt. Remplir le tube d'eau et installer les masses dedans. Fermer le couvercle du tube et faire attention à la verticalité de l'ensemble, afin d'éviter les frottements solides. Lancer l'oscillateur à la main et vérifier qu'il s'amortit rapidement. La masse ne doit pas sortir de l'eau.
2. Déterminer la réponse en amplitude du système pour la gamme de fréquence accessible par le moteur. On représentera le diagramme de Bode en gain associée (tracé grâce au tableur demandé, non à la main).
3. Analyser le diagramme de Bode pour remonter au facteur de qualité du système (on pourra remarquer qu'on dispose déjà de la pulsation propre du système).
4. Comment obtenir, sans mesure supplémentaire, les amplitudes des réponses en vitesse? En déduire le tracé du diagramme de Bode de la réponse en vitesse puis l'analyser.
````