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

## Présentation du dispositif

```{figure} ./images/Mecanique_Pendule.jpg
:name: parametrage
:align: center
Paramétrage du pendule
```

Le pendule utilisé est constitué d'un cylindre de masse M, pouvant coulisser sur une tige métallique de masse m. Le pendule est libre de tourner autour d'un axe horizontal (Ox). On notera J le moment d'inertie du pendule par rapport à (Ox).

````{note} 
Un contre-poids est réalisé par un prolongement de la tige de l'autre côté du pivot, d'une longueur $l_1$. Une masse $M_1$ est placée en contre poids à une distance $L_1$.

````

L'état du pendule est entièrement défini par la donnée de $\theta(t)$ (angle entre la verticale et la tige) et de sa dérivée par rapport au temps $\dot \theta(t)$ (vitesse angulaire). Les angles seront repérés à partir de la verticale: $\theta=0$ correspond à la position la plus basse du pendule.

Il est possible d'exercer des frottements solides au niveau de l'axe de rotation du pendule, à l'aide d'une vis/un serre-joint venant appuyer une lame/un disque métallique sur l'axe de rotation. L'étude des frottements fluides sera quant à elle menée par freinage de l'extrémité du pendule dans de l'eau (utiliser les bacs à cet effet).

## Système de mesure
La position $\theta(t)$ du pendule au cours du temps sera acquise automatiquement à l'aide d'un potentiomètre annulaire (voir figure \cref{fig_pendule_potar}).

Le potentiomètre doit être alimenté par un signal continu (0 V/5 V). Le  point milieu du potentiomètre est solidaire de la tige du pendule. Ainsi, on peut relever la tension $u(t)$ entre le point milieu et la borne reliée à 0 V, tension qui évolue linéairement avec $\theta(t)$.

```{figure} ./images/Mecanique_Pendule_Potentiometre.jpg
:name: potar
:align: center
Système de mesure
```

```{note}
La position correspondant à 0V n'est pas la position la plus basse. La relation $theta(u)$ est donc affine et nécessitera un étalonnage par deux points au moins.

```

## Mise en équation du pendule

### Cas sans frottements
On note M la masse à l'extrémité, m la masse de la tige, l la longueur de la tige et L la distance entre l'axe de rotation et la masse M. 

Côté contre poids, on note les grandeur analogues $M_1, l_1, L_1$.

Le moment d'inertie du pendule par rapport à son axe de rotation (Ox) s'écrit alors:

$$
  J=\frac{\lambda l^3}{3}+ML^2 + \frac{\lambda l_1^3}{3}+M_1 L_1^2
$$

où $\lambda$ est la masse linéique de la tige.

Considérons les conditions initiales $\theta(0)=\theta_0$ et $\dot \theta(0)=\dot \theta_0$. En l'absence de frottements, le pendule suit l'équation suivante:

\begin{equation}
  J \ddot{\theta}=(-(\lambda \frac{l^2}{2} + ML) + (\lambda \frac{l_1^2}{2} + M_1 L_1))g \sin \theta
\end{equation}

soit:

\begin{equation}
  \ddot{\theta}+\omega_0^2 \theta = 0
\end{equation}
avec  

$$
\omega_0 = \sqrt{\frac{\lambda l^2/2+ML - \lambda l_1^2/2+M_1 L_1}{\lambda l^3/3 + ML^2 + \lambda l_1^3/3 + M_1 L_1^2}}
$$

Au petites oscillations, le système se comporte comme un oscillateur harmonique et est isochrone. Ce n'est plus le cas aux fortes oscillations.

### Cas avec frottements fluides
Si l'on suppose les frottements fluides linéaires, on peut leur associer un couple suivant l'axe de rotation: $\Gamma_f =-\Lambda \dot \theta$. L'équation du mouvement devient alors:

\begin{equation}
  \ddot{\theta}+2 \sigma \dot \theta +\omega_0^2 \theta = 0
\end{equation}

avec $\sigma = \frac{\Lambda}{2J}$.

Pour de petites oscillations, on retrouve l'équation d'un oscillateur amorti classique. $\sigma$ étant le coefficient d'amortissement. Dans le cas d'un régime pseudo-périodique, on peut alors relier la pseudo-période et le décrément logarithmique (cf. cours) à la pulsation propre et au coefficient d'amortissement.

### Cas avec frottements solides
Dans le cas de frottements solides sur l'axe de rotation, la force de frottements est indépendante de la norme de la vitesse, et son sens, toujours opposé au vecteur vitesse. Appliquée sur l'axe du pendule, elle exerce sur celui-ci un couple de freinage: $\Gamma_s=-\epsilon \Gamma \overrightarrow{u_x}$ où $\epsilon$ vaut $\pm 1$ suivant le signe de la vitesse, de manière à ce que le couple soit toujours résistant.

L'équation du mouvement devient alors:

\begin{equation}
  \ddot{\theta}+\omega_0^2 \theta = -\epsilon A \theta_0^2
\end{equation}

avec $A=\frac{\Gamma}{J \omega_0^2}$.

Une étude complète (cf. TD) montre qu'on observe alors des oscillations de pseudo-période égale à la période propre et d'amplitude décroissante. La décroissance est linéaire et l'écart entre deux maxima positifs successives vaut: $\Delta\theta=-4A$. Le mouvement se poursuit jusqu'à l'arrêt du pendule.