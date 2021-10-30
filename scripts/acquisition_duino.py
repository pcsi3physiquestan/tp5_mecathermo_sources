"""
Lecture de la température
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scope import Scope, get_port

"""Données sur la sonde CTN et l'acquisition. A modifier en conséquence"""
t_obs = 60000 * 0.1  # Durée d'observation en ms
nom_fichier = "nom_eleves.txt"  # Nom du fichier à modifier où seront enregistrées les données
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



port_serie=get_port()  # Objet contenant les données de la liaison ordinateur-Arduino

f_data = open(nom_fichier, 'w')  # Ouverture du fichier pour enregistrement. ATTENTION, si le fichier existe, son contenu est effacé.
f_data.write("t(ms), T(C)")

def read_data():
    """Fonction qui acquiert les données depuis Arduino et
    les traite. Sa compréhension n'est pas nécessaire."""
    global f_data
    t_in = 0
    while t_in <= t_obs:
        if port_serie.isOpen():  # Vérification de la connection
            toread = port_serie.readline()  # Lecture d'une ligne de mesure
            toread = toread.decode("utf-8").split(",")  # Séparation Delta t et Tension
            if len(toread) == 2:
                t_in = t_in + int(toread[0])  # Nouveau temps
		Ubinaire = int(toread[1])
                us =  CNA(Ubinaire)  # Conversion Nbit vers Tension
                temp = Tth(Rdiv(us))  # Convertion vers temperature
                print("Temps : ", t_in, "; Température : ", temp)
                f_data.write(str(t_in) + "," + str(temp))
                yield [t_in, temp]
            else:
                print("RAS")
                yield []
        else:
            print("Port serie ferme. Acquisition impossible.")
            yield []


"""Tracé en temps réel"""
fig, ax = plt.subplots()
fig.suptitle("Calorimétrie. Acquisition")
ax.set_xlabel("t(ms)")
ax.set_ylabel("T(C)")

"""Les lignes ci-dessous ne sont pas à comprendre"""
scope = Scope(ax, maxt=t_obs)  # scope est un objet qui va gérer la mise à jour du tracé

# Animation qui va créer le graphique en temps réel
ani = animation.FuncAnimation(fig, scope.update, read_data, interval=50,
                            blit=True, repeat=False)

plt.show()
