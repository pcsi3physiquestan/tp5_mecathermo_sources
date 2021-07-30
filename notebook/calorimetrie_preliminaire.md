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
Ce TP comporte deux parties: d'une part l'étude du changement d'état liquide-vapeur du SF6 et d'autre part de la calorimétrie. L'organisation globale du TP nécessite une mise en commun. Faire deux groupes de deux binômes (=groupe de deux élèves). Dans chaque groupe, décidez quel binôme commence par la calorimétrie, et quel binôme commence par les changements d'état. La calorimétrie sera traitée identiquement par les deux groupes.

La première partie du TP durera 1h30 puis inversion des binômes. La seconde durera aussi 1h30. La dernière heure devra servir à la mise en commun et à l'exploitation des résultats.

## Description générale
Pour l'ensemble du TP, les mesures seront effectuées au sein d'un calorimètre: dispositif permettant d'isoler thermiquement de l'extérieur ce qui est placé à l'intérieur. Il est constitué d'un vase en verre double paroi brillantée sous vide d'air, recouvert d'une enveloppe extérieure en plastique (NE PAS RETIRER L'ENVELOPPE PLASTIQUE!) et d'un couvercle de fermeture. Le couvercle dispose d'un petit trou pour pouvoir y glisser une sonde de température. L'ensemble est également muni d'un agitateur permettant d'homogénéiser les fluides introduis dans le calorimètre. Enfin, un dispositif de thermoplongeurs (résistances plongeantes ne devant fonctionner que sous l'eau) peut être installé sur le couvercle.

Dans tout le TP, par calorimètre, on considérera l'enceinte fermée et calorifugée constituée du vase intérieur, des protections plastiques et des accessoires nécessaires aux mesures et à cette expérience (thermomètre, agitateur, thermoplongeur). Le thermomètre utilisé sera une sonde thermocouple.

## Méthode électrique

Le calorimètre possède une capacité thermique $C_{cal}$, éventuellement non négligeable devant celle du système placé à l'intérieur. Il est donc nécessaire de la mesurer avant toute autre chose. On propose l'utilisation de la méthode électrique. On notera $c_{eau}$ la capacité thermique massique de l'eau liquide.

On place dans le calorimètre une masse meau connu d'eau et on laisse l'ensemble {calorimètre+eau} établir un équilibre thermique à la température $T_i$. On place alors une résistance R au sein du liquide et on l'alimente pendant un temps $\Delta t$ par une tension U constante. On mesure alors la température finale $T_f$ lorsque celle-ci s'est stabilisée.

Un bilan enthalpique (la transformation est monobare entre deux états d'équilibre) entre l'instant initial $t_i$ et l'instant final $t_f$ permet d'écrire:

\begin{equation}
  (C_{cal}+m_{eau} c_{eau})(T_f-T_i)=\frac{U^2}{R}(t_f-t_i)
\end{equation}

Si le chauffage est suffisamment lent, on peut alors supposer la transformation quasi-statique et la relation précédente sera vraie durant toute la transformation:

\begin{equation}
  (C_{cal}+m_{eau} c_{eau})(T(t) -T_i)=\frac{U^2}{R}(t-t_i) 
\end{equation}

## Méthode des mélanges
Pour mesurer la chaleur latente de fusion de la glace, on va mélanger un système \{masse meau d'eau + calorimètre\} à la température $T_1$ avec une masse $m_{glace}$ de glace à la température de fusion $T_{fus}(Patm)=0^{\circ}\rm{C}$.

En travaillant sur une transformation fictive (fonte isotherme totale des glaçons puis mise à l'équilibre thermique des deux systèmes), le bilan enthalpique s'écrit:

\begin{equation}
  m_{glace} l_{f,glace} + m_{glace} (T_f -T_{fus})+(C_{cal}+c_{eau} m_{eau}) (T_f -T_1)=0
\end{equation}