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

# Préliminaires
````{attention} 
Au cours de cette séance de 4h, vous effectuerez deux TP différents de 1h30: 2 binômes travailleront sur [la chute d'une bille dans un fluide](chute) et 2 binômes sur les oscillations mécaniques forcées. Vous devez échanger de postes au bout de 1h30. La dernière heure permettra de mettre en commun et exploiter les résultats.

````

## Dispositif expérimental
On dispose d'un ressort à suspendre verticalement sur un support comportant une poulie. Un jeu de masses peut être suspendu à l'extrémité inférieure du ressort. Les masses peuvent éventuellement être mises à osciller dans un tube rempli d'eau, appliquant des frottements fluides au dispositif. Des palettes circulaires de rayon plus ou moins important augmentent encore l'effet des frottements.

L'extrémité supérieure du ressort est attachée à un fil inextensible relié à un moteur qui permet de générer une force quasi-sinusoïdale sur le dispositif (fréquences réglables de 0,1 Hz à 3,0 Hz), contrecarrant la perte énergétique due aux frottements. L'oscillateur fonctionne alors en régime sinusoïdal forcé. Pour les mesures de longueurs du ressort, une réglette graduée s'aimante sur le support et peut être positionnée à l'emplacement souhaité.

## Rappel théorique

### Mise en équation
D'après le PFD appliqué à la masse {m} suspendue au ressort de constante de raideur k et de longueur à vide $l_0$, dans le référentiel terrestre considéré galiléen:
\begin{equation}
  m \ddot{x} = mg - kx - \lambda \dot{x} +kx_A \cos \omega t
\end{equation}
soit
\begin{equation}
  \ddot{X}+\frac{\lambda}{m} \dot{X} + \frac{k}{m} X = \frac{k}{m} x_A \cos \omega t
\end{equation}
où $x(t)$ désigne l'allongement du ressort, $X(t)$ la longueur du ressort rapportée à sa longueur d'équilibre $l_{eq}$, $\lambda$ le coefficient de frottements fluides et $x_A \cos(\omega t)$ l'amplitude de vibration de l'autre extrémité du ressort, imposé par le moteur.

### Réponse en amplitude
En régime sinusoïdale forcé, on a, en introduisant les notations complexes:

\begin{equation}
  \underline{X} = \frac{F/(m \omega_0^2)}{1- {(\frac{\omega}{\omega_0})}^2+j \frac{\omega}{\omega_0 Q}}
\end{equation}

en posant $\omega_0^2 = \frac{k}{m}$ la pulsation propre de l'oscillateur et $Q = \frac{1}{\lambda} \sqrt{km}$ le facteur de qualité. Pour des facteurs de qualité supérieure à $\frac{1}{ \sqrt{2}}$ on observe un phénomène de résonance à la pulsation: $\omega_r = \omega_0 \sqrt{1- \frac{1}{2Q^2}}$.

### Réponse en vitesse
La réponse en vitesse s'obtient en remarquant que: $\underline{V}= j \omega \overline{X}$. On observe alors systématiquement une résonance à la pulsation $\omega = \omega_0$.