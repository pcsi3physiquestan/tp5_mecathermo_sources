"""
Lecture de la température
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scope import Scope, Communication

"""-----------------------PARTIE A MODIFIER----------------------------------------"""
"""Données sur la sonde CTN et l'acquisition. A modifier en conséquence"""
t_obs = 10000  # Durée d'observation en ms
Tmin, Tmax = 0, 1024  # Gamme de température en Kelvin pour le tracé graphique
nom_fichier = "nom_eleves.txt"  # Nom du fichier à modifier où seront enregistrées les données.
# PENSEZ A CHANGER LE NOM DU FICHIER ENTRE DEUX ACQUISITIONS SOUS PEINE D'EFFACEMENT DES DONNEES.
Rpont = 10  # R1 (en kOhm) du pont diviseur
Vcc = 5  # Tension (en V) du pont
R0 = 10 # R0 (en kOhm) de la relation Rth(T)
beta = 3924  # Beta (en K) de la relation Rth(T)
T0 = 25+273.15  # T0 (en K) de la relation Rth(T)


def CNA(Ubinaire):
    """ Fonction qui calculer la tension comprise entre 0 et 5V (flottant) à partir
    de sa représentation binaire (un nombre entier compris entre 0 et 1023)
    """
    U = Ubinaire
    return U


def Rdiv(U):
    """Renvoie Rth connaissant la tension aux bornes de Rpont"""
    R = U  # Modifier cette ligne en fonction du modèle
    return R


def Tth(R):
    """Renvoie T (en degré) connaissant Rth"""
    T = R  # Modifier cette ligne en fonction du modèle
    return T
"""--------------------------FIN DE LA PARTIE A MODIFIER---------------------------------"""

"""------------------------ GESTION DE LA COMMUNICATION ARDUINO PYTHON ------------------"""
def f_traitement(Ubinaire):
    """Cette fonction reprend simplement les fonctions que vous avez écrites pour calculer T"""
    return Tth(Rdiv(CNA(Ubinaire)))

com_arduino = Communication(nom_fichier, f_traitement, t_obs, titre="T(K)")  # Objet qui va gérer l'échange avec Arduino

"""------------------------ GESTION DU TRACE GRAPHIQUE ------------------"""
"""Légende du graphique"""
fig, ax = plt.subplots()
fig.suptitle("Calorimétrie. Acquisition")
ax.set_xlabel("t(ms)")
ax.set_ylabel("T(C)")

"""Les lignes ci-dessous ne sont pas à comprendre"""
scope = Scope(ax, ylim=[Tmin, Tmax], maxt=t_obs)  # scope est un objet qui va gérer la mise à jour du tracé

# Animation qui va créer le graphique en temps réel
ani = animation.FuncAnimation(fig, scope.update, com_arduino.read_data, interval=50,
                            blit=True, repeat=False)

plt.show()