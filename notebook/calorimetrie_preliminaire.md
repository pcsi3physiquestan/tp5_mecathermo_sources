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

Dans tout le TP, par calorimètre, on considérera l'enceinte fermée et calorifugée constituée du vase intérieur, des protections plastiques et des accessoires nécessaires aux mesures et à cette expérience (thermomètre, agitateur, thermoplongeur). Le thermomètre utilisé sera une résistance électrique.

## Méthode électrique

Le calorimètre possède une capacité thermique $C_{cal}$, éventuellement non négligeable devant celle du système placé à l'intérieur. Il est donc nécessaire de la mesurer avant toute autre chose. On propose l'utilisation de la méthode électrique. On notera $c_{eau}$ la capacité thermique massique de l'eau liquide.

On place dans le calorimètre une masse $m_{eau}$ connu d'eau et on laisse l'ensemble {calorimètre+eau} établir un équilibre thermique à la température $T_i$. On place alors une résistance R au sein du liquide et on l'alimente pendant un temps $\Delta t$ par une tension U constante. On mesure alors la température finale $T_f$ lorsque celle-ci s'est stabilisée.

Un bilan enthalpique (la transformation est monobare entre deux états d'équilibre) entre l'instant initial $t_i$ et l'instant final $t_f$ permet d'écrire:

\begin{equation}
  (C_{cal}+m_{eau} c_{eau})(T_f-T_i)=\frac{U^2}{R}(t_f-t_i)
\end{equation}

Si le chauffage est suffisamment lent, on peut alors supposer la transformation quasi-statique et la relation précédente sera vraie durant toute la transformation:

\begin{equation}
  (C_{cal}+m_{eau} c_{eau})(T(t) -T_i)=\frac{U^2}{R}(t-t_i) 
\end{equation}

## Méthode des mélanges
Pour mesurer la chaleur latente de fusion de la glace, on va mélanger un système \{eau + calorimètre\} à la température $T_1$ avec une masse $m_{glace}$ de glace à la température de fusion $T_{fus}(Patm)=0^{\circ}\rm{C}$.

En travaillant sur une transformation fictive (fonte isotherme totale des glaçons puis mise à l'équilibre thermique des deux systèmes), le bilan enthalpique s'écrit:

\begin{equation}
  m_{glace} l_{f,glace} + m_{glace} c_{eau} (T_f -T_{fus})+(C_{cal}+c_{eau} m_{eau}) (T_f -T_1)=0
\end{equation}

## Sonde de température
La mesure de la température sera réalisée par une sonde CTN plongée dans l'eau qui peut-être fixée dans le calorimètre. La sonde est une une thermistance, c'est-à-dire une résistance dont la valeur $R(T)$ dépend de la température. L'étude de la thermistance montre que la résistance suit le modèle :

$$
R(T) = R_0 \exp \left(\beta \left(\frac{1}{T} - \frac{1}{T_0}\right)\right)
$$

avec $R_0 = 10 \rm{k\Omega}; \beta = 2836 \rm{K}$ et $T_0 = 323 \rm{K}$.

Le constructeur a déjà monté la thermistance en série avec une résistance $R_1 = 10 \rm{k\Omega}$ formant ainsi un pont diviseur de tension. Le principe d'utilisation de la thermistance consiste à alimenter le pont diviseur avec une tension $E_0$ puis mesurer soit la tension aux bornes de la thermistance, soit la tension aux bornes de $R_1$. Dans le montage réalisé ici, c'est la tension aux bornes de $R_1$ qui est mesurée. Une étude du pont diviseur de tension permet d'obtenir la valeur de $R(T)$ à partir de la valeur mesurée de $u_{R_1}$.

\begin{align*}
u_{R_1} &= \frac{R_1}{R_1 + R(T)} E\\
R(T) &= R_1 \left(\frac{E}{u_{R_1}} - 1\right)
\end{align*}

La température (__en K__)se déduit alors :

$$
T = {\left(\frac{1}{T_0} + \frac{1}{\beta} \ln \frac{R}{R_0}\right)}^{-1}
$$

## Système d'acquisition
Des systèmes d'acquisition complets existent mais nous allons utiliser ici un système "fait maison" pour comprendre les différents éléments d'un système d'acquisition. C'est aussi l'occasion de manipuler un microcontrolleur.

Le système d'acquisition sera séparé en deux parties :
* un [microcontrolleur Arduino](arduino_carte) muni d'un [shield Grove](arduino_grove) pour faciliter le branchement de la sonde. Une fois programmé, le microcontrolleur aura pour rôle :
    * d'alimenter le pont diviseur avec une tension $E_0 = 5V$
    * de mesurer la tension (grandeur analogique) aux bornes de $R_1$ puis la convertir en un nombre (représentation binaire de la tension, c'est une conversion analogique numérique) entre 0 (correspondant à 0V) et 1023 (correspondant à 5V).
    * d'envoyer ce nombre à l'ordinateur (sous forme de chaine de caractère)
* un ordinateur et plus précisément un script Python (à ouvrir avec Pyzo) qui a pour rôle :
    * de récupérer les mesures envoyées par Arduino
    * de calculer la température correspondant à la tension mesurée
    * d'afficher sur un graphique en temps réel l'évolution de T.
    * d'enregistrer à la fin de l'acquisition les données dans un fichier.

````{panels}
```{figure} ./images/arduino_carte.jpg
:name: arduino_carte
:align: center
Carte Arduino
```
---
```{figure} ./images/arduino_grove.jpg
:name: arduino_grove
:align: center
Shield Grove
```
````

(arduino_pres)=
### Utilisation du microcontrolleur
#### Branchements
Les branchements sont simplifiées par l'utilisation du shield Grove.
1. Si ce dernier n'est pas déjà fixé sur la carte Arduino. Placez le shield sur la carte. __Faire attention à ce que les broches soient bien placées au dessus des trous des bornes avant d'enfoncer la carte de manière à ne pas tordre une broche, ce qui conduirait à un disfonctionnement de la carte (fragile).__
2. Le microcontrolleur Arduino peut réaliser deux types de mesures : des mesures logiques (0 ou 1) à l'aide des entrées D1, D2, ... et des mesures analogiques (tension entre 0 et 5V) grâce aux bornes A0, A1, ... On utilisera donc ces dernières. Brancher la connectique de la sonde (appelée connectique Grove) sur l'une des entrées analogiques (PIN) en notant le numéro (A0, A1, ...) correspondant.
3. Installer la sonde dans le montage voulu (ici le montage de calorimétrie) puis brancher la carte Arduino à l'ordinateur. La carte devrait s'allumer signalant qu'elle alimentée.

#### Programmation de la carte
Pour l'instant, le microcontrolleur est alimenté mais il ne remplit pas son rôle, il réalise le dernier programme enregistré qui n'est probablement pas le bon. Il faut _programmer le microcontrolleur_ en _téléversant_ un programme dans sa mémoire.

La syntaxe utilisée par les microcontrolleurs Arduino est un dérivé du C++ et il n'est pas nécessaire de comprendre ce langage pour le TP. Vous devez par contre téléverser le programme dans Arduino.

````{note}
Le logiciel Arduino sera disponible sur les ordinateurs de la salle de TP. Sachez néanmoins qu'il est libre et peut-être [télécharger](https://www.arduino.cc/en/software) sur le site officiel et installé sur votre propre ordinateur.

_Attention, si vous désirez utiliser votre propre ordinateur pour brancher la carte Arduino en TP. Il faudra installer la bibliothèque `pyserial` qui n'est pas installée par défaut par Anaconda._ La procédure d'installation n'est pas donnée ici.
````

1. Sur le [site](https://stanislas.edunao.com/mod/folder/view.php?id=13511&forceview=1), télécharger le dossier complet. Vous y trouvez deux programmes Python sur lesquels nous reviendrons par la suite et un dossier `sonde_ctn` contenant un fichier `.ino` : c'est le programme que vous allez téléverser dans la carte.
2. Ouvrir le logiciel Arduino puis ouvrir le fichier `sonde_ctn.ino` que vous venez de télécharger.
3. Il n'est pas nécessaire de comprendre ce programme, vous devez juste repérer la ligne où est définie le PIN de de branchement de la sonde (A0, A1...). Remplacer le par celui où vous avez branché la sonde.
4. `Vérifier` que le programme est correct (premier bouton de la barre d'outil). S'il n'y a pas de message d'erreur, passez à l'étape suivante, sinon appeler l'enseignant.
5. Dans `Outils > Port`, choisir celui proposé correspondant à la carte Arduino. Notez au passage son nom car vous pourriez en avoir besoin pour la partie Python.
6. `Téléverser` ensuite votre programme dans la carte (deuxième bouton de la barre d'outil). 
7. S'il n'y a pas d'erreur, votre carte a commencé à envoyer les mesures de température ainsi que l'intervalle de temps entre deux mesures. Vous pouvez le vérifier en ouvrant le moniteur série (bouton tout à gauche de la barre d'outil) puis choisir 115200 baud dans le menu en bas à droite. Vous devriez voir s'afficher les mesures de temps et de température.

````{note}
L'acquisition par un microcontrolleur se fait toujours de la même manière :
* Alimention du capteur si nécessaire
* Mesure (analogique ou numérique) de la grandeur voulue
* Traitement de la grandeur si nécessaire (le cas si la mesure est numérique)
* Envoi de la donnée ou utilisation (si le microcontrolleur doit contrôler un actionneur)
````

### Acquisition grâce à Python
On pourrait se limiter au moniteur série pour recueillir la température initiale et finale mais on va faire mieux au moyen de Python : on va afficher en temps réel 

La bibliothèques `pyserial` permet à un script Python de se connecter à un port série (entrée de l'ordinateur pemettant la communication avec un appareil, ici Arduino) pour les données envoyées par le microcontrolleur. On ne présente pas ici le fonctionnement de cette bibliothèque.

Dans le dossier que vous avez téléchargé, vous trouverez deux fichiers Python :
* `scope.py` contient la fonction qui utilise la bibliothèque `pyserial` pour lire les données et un objet Scope qui va gérer l'affichage en temps réel des mesures sur un graphique. Ce fichier __n'est à modifier sous aucun pretexte.__
* `acquisition_duino.py` contient les fonctions permettant d'obtenir la température à partir des données renvoyées puis d'afficher $T(t)$. C'est __ce fichier que vous allez devoir modifier en partie puis exécuter.__

````{attention}
Le fichier que vous exécuterez fait appel au premier. Il __faut donc que les deux fichiers soient bien enregistrés dans le même répertoire.__
````

#### Modification du programme Python
````{important} Environnement python
__Lorsque vous lancez pyzo, allez dans `Shell` puis `Configuration des shells` et dans le menu déroulant `exe`, choisir le chemin vers l'executable python contenant `envprepa`.__ Sans quoi, vous n'aurez pas accès à la bibliothèques `pyserial`.
````

La majeure partie du programme est déjà écrite. Elle est divisée en trois parties :
1. Les fonctions permettant de passer de la représentation binaire à la tension en volt (`CNA`), de la tension $u$ à la résistance $R(T)$ (`Rdiv`) puis de la valeur de la résistance à la température $T$ (`Tth`).
    * Modifier les valeurs numériques des différentes grandeurs en fonction des données précédentes.
    * Modifir la durée d'observation `t_obs` et le nom du fichier `nom_fichier` dans lequel les données seront enregistrées (pensez à modifier ces deux grandeurs pour chaque acquisition pour éviter d'écraser un précédent fichier).
    * Modifier les trois fonctions pour qu'elles renvoient bien ce qu'on attend.
2. Une fonction `read_data` qui va gérer la lecture du port série et le calcul de la température grâce aux fonctions précédentes. Cette partie n'est pas à modifier.
3. Un tracé en temps réel. Cette partie n'est pas non plus à modifier.

````{important}
Une fois l'exécution du script lancé, vous ne pourrez plus modifié les paramètres et l'acquisition est longue donc vérifiez que tout est bon avant de lancer le programme.
````

#### Test

````{important} Test du programme
Avant de réaliser l'acquisition de 15 minutes comme demandé dans le TP, lancer une acquisition de quelques secondes une fois le montage réalisé pour vérifier que le programme fonctionne correctement.

````