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
__Le téléchargement de ce notebook n'est pas nécessaire.__

# Travaux pratiques

## Mise en garde

````{attention} 
LES RÉSISTANCES CHAUFFANTES SONT TRÈS FRAGILES:
* les manipuler avec soin
* ne pas les poser n'importe comment sur la paillasse
* NE LES ALIMENTER QUE SI ELLES PLONGENT DANS L'EAU
* Mesurer au multimètre la résistance avant de procéder aux branchements (la mesure au multimèrte ne nécessite pas qu'elles soient plongées dans l'eau).
````

````{important} 
Chaque manipulations dure au moins 15 minutes en plus de la mise en place et l'eau va changer de tempérarure. Il est donc délicat de refaire les manipulations s'il y a eu erreur.

__Il est donc important de bien lire l'ensemble de la manipulation à réaliser AVANT de commencer pour ne pas se tromper.__
````
## Mesure de la capacité thermique du calorimètre.

Le calorimètre possède une capacité thermique $C_{cal}$, éventuellement non négligeable devant celle du système placé à l'intérieur. Il est donc nécessaire de la mesurer avant toute autre chose. On propose l'utilisation de la méthode des mélanges. On notera $c_{eau}$ la capacité thermique massique de l'eau liquide.

> Mise en place du dispositif :
> 1. Mise en place du dispositif: Introduire dans le calorimètre une masse de 700g d'eau environ (la peser précisément au moyen d'une balance). Fermer le calorimètre avec le couvercle constitué de plusieurs résistances chauffantes. Placer la sonde de température dans le trou prévu à cet effet et le brancher sur le microcontrolleur et relier ce dernier à l'ordinateur. S'assurer à la fermeture que le thermocouple est bien plongé dans l'eau et ne touche ni les résistances, ni l'agitateur lors de son mouvement.
> 2. Procéder comme présenté [précédemment](arduino_pres) pour programmer le microcontrolleur
> 3. Mise en place de l'alimentation: Brancher, __générateur éteint__, l'alimentation stabilisée à disposition entre les bornes correspondant à la résistance de $4 \Omega$ (Vérifier sa valeur à l'Ohmmètre, utiliser celle de $2 \Omega$ sinon). Tourner au maximum la molette de réglage de l'intensité pour que le générateur fonctionne comme une source idéale de tension. Tourner au minimum la molette de réglage de tension.

````{attention}
On sera très prudent lors de la manipulation du circuit car les courants qui circulent sont important et on est en présence d'eau. __TOUTE MANIPULATION DU DISPOSITIF (autre que l'utilisation de l'ordinateur) DEVRA SE FAIRE ALIMENTATION ETEINTE.__
````

L'acquisition va se faire en 3 étapes :
1. Mesure de la température de l'eau pendant 2 minutes sans allumer l'alimentation.
2. Allumage de l'alimentation pour délivrer une tension de 10V environ (utiliser la molette de réglage de tension). __Ne pas dépasser 12V.__ Noter alors les valeurs de tension et d'intensité pour le calcul de puissance.  _Noter précisément le temps d'allumage (qui s'affiche dans la console Python)_
3. Au bout de 10 minutes, extinction de l'alimentation. On laisse encore l'acquisition tourner jusqu'à un total de 15 minutes pour être sûr que l'équilibre thermique est réalisé. _Noter précisément le temps d'extinction (qui s'affiche dans la console Python)_

> Acquisition (__bien suivre les réglages de l'étude préliminaire__):
> 1. Modifier la durée d'observation `t_obs` (15 minutes, attention, la durée est en millisecondes) et le nom du fichier d'enregistrement dans le programme Python.
> 2. Lancer le programme Python pour lancer l'acquisition. _Si on vous demande dans la console le port correspondant à Arduino, chosir le numéro correspondant au nom du port que vous avez noté en programmant la carte._
> 3. Au bout de 2 minutes, allumer l'alimentation. Vous pouvez agiter doucement de temps en temps.
> 4. Au bout de 10 minute, éteindre l'alimentation puis laisser l'acquisition aller à son terme.

````{admonition} Exploitation des résultats
:class: tip
1. Observation l'allure de $T(t)$. Peut-on supposer que la transformation a été quasi-statique?
2. Déterminer à partir du fichier de données la capacités thermique du calorimètre. On estimera les sources d'incertitudes ainsi que leur expressions puis on calculera l'incertitude sur $C_{cal}$ par __propagation des variances__.
````

## Mesure de la chaleur latente de fusion de la glace

On désire mesurer la chaleur latente massique de fusion de la glace à pression atmosphérique $l_{f, glace}$. On rappelle que cette grandeur correspond à l'enthalpie libérée par le système lors d'un changement d'état isobare (et donc isotherme). On utilise la méthode des mélanges.

__L'introduction de la glace devra être rapide. Il est donc conseillé de bien maîtriser la procédure avant de la réaliser. Tout élève pris entrain de s'amuser avec la glace sera expulsé du TP.__

> 1. On va refaire une acquisition de 15 minutes. __PENSEZ A CHANGER LE NOM DU FICHIER DANS LE SCRIPT POUR NE PAS EFFACER VOS DONNEES PRECEDENTES.__
> 2. Garder le dispositif précédent. Lancer une acquisition de 15 minutes. Au bout de 2 minutes, poser une casserole sur une balance et la tarer. Sortir les glaçons, les piler puis les placer dans la casserole pour environ 200g (la mesure précise sera faite à la fin). Les mettre dans le calorimètre (sans que ça déborde) __Cette manipulation doit être rapide.__
> 3. Mélanger doucement de temps en temps pour accélérer la mise à l'équilibre. Lorsque l'acquisition est terminée, vérifier que l'équilibre thermique a été atteint.
> 4. __NE PAS JETER l'eau.__ Peser le contenu du calorimètre. En retranchant la quantité d'eau initialement dans le calorimètre, vous aurez une pesez précise des glaçons.

````{admonition} Exploitation des résultats
:class: tip
1. Observation l'allure de $T(t)$. Peut-on supposer que la transformation a été quasi-statique?
2. Déterminer à partir du fichier de données l'enthalpie massique de fusion de l'eau. On estimera les sources d'incertitudes ainsi que leur expressions puis on calculera l'incertitude sur $L_{f, glace}$ par __propagation des variances__.
3. Comparer à la valeur tabulée.
````
