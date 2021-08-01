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

(cineris)=
# Utilisation du logiciel CINERIS

````{admonition} Manipulation préliminaire
:class: tip
Brancher la webcam sur un port USB de l'ordinateur puis lancer le logiciel CINERIS. Se rendre sur l'onglet Vidéo d'Atelier Scientifique, ou utiliser l'icône de caméra.
````

## Acquisition Vidéo

_Il n'est pas nécessaire de modifier le répertoire d'enregistrement des vidéos mais sachez que celle-ci ne seront pas disponibles après la séances._ Vous pouvez garder l'acquisition rapide et choisir une durée d'acquisition suffisante grande, la vidéo sera coupée par la suite. Le bouton en bas à droite de l'onglet permet de lancer l'acquisition quand voûs êtes prêt.

```{figure} ./images/Mecanique_Cineris_Acquisition.jpg
:name: cineris_a
:align: center
Acquisition
```

## Montage
````{panels}
```{figure} ./images/Mecanique_Cineris_Montage.jpg
:name: cineris_m
:align: center
```

---
1. Charge le fichier à traiter.
2. Zoom la séquence vidéo dans la fenêtre de travail
3. Boutons permettant le retour à la 1ère image, le recul image par image, la pause, la lecture, et l'avance image par image. Il est également possible de se déplacer dans le fichier à l'aide de l'ascenseur sous les boutons.
4. Permet de sélectionner une partie du fichier ouvert en à l'aide des boutons précédent, on se positionne d'abord sur la 1ère image du montage et on coupe avec Début, puis on se positionne sur la dernière image et on coupe avec Fin.
5.  Peu utile (ne pas choisir de format compressé).
6.  Enregistre la séquence vidéo définie en au format AVI. 

__Utilisez le montage pour ne travailler que sur la partie de la vidéo où l'on voit la bille tomber.__
````

## Relevé automatique des points
La qualité du contraste est telle qu'on ne réalisera pasd d'acquisition automatique mais uniquement des acquisitions manuelles.

## Relevé manuel
_Pensez à vous placer à la première image où l'on voit la bille._

### Etalonnage
````{panels} 

```{figure} ./images/Mecanique_Cineris_Etallonnage.jpg
:name: cineris_e
:align: center
Etalonnage
```
---
1. 8: Fixe l'origine du repère. Si l'on souhaite que l'origine coïncide avec une position particulière du mobile, choisir la bonne image et cliquer sur la position.
2. 9: Fixe l'échelle des axes Ox et Oy par cliquer-glisser (jusqu'au bout de la flèche). Il est obligatoire d'avoir sur la séquence vidéo une référence des distances. Par défaut, le déplacement est soit horizontal, soit vertical, mais un appui sur la touche CTRL permet un déplacement dans toutes les directions.

````

### Relevé des points
````{panels}
1. Lancer le démarrage de l'acquisition grâce au bouton vert (5).
2. Pour chaque image, cliquer sur la position de la bille. Le passage à l'image suivante est alors automatique.
---
```{figure} ./images/Mecanique_Cineris_Lancement.jpg
:name: cineris_l
:align: center
Lancement
```
````