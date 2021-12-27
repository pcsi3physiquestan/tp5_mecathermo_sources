"""
Lecture de la température
"""

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial.tools.list_ports
from serial import *

class Scope:
    """Objet qui va afficher le graphique"""
    def __init__(self, ax, ylim=[0, 30],  maxt=10000):
        self.ax = ax
        self.maxt = maxt
        self.ax.set_xlabel(labels[0])
        self.ax.set_xlabel(labels[1])
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata, marker='+', linestyle='', label='Température')
        self.ax.add_line(self.line)
        self.ax.set_ylim(ylim[0], ylim[1])
        self.ax.set_xlim(0, maxt * 1.1)
        self.ax.legend()

    def update(self, y):
        """Fonction qui sera appelé par l'animation"""
        if len(y) == 2:  # Seulement tracé d'une courbe ici
            t = y[0]
            if t < self.maxt:
                self.tdata.append(t)  # Abscisse
                self.ydata.append(y[1])  # Ordonnées
            self.line.set_data(self.tdata, self.ydata)  # Actualisation de la liste
        return self.line,


class Communication:
    """Objet qui va gérer la communication avec Arduino"""
    def __init__(self, nom_fichier, f_traitement, tobs, titre="T(K)"):
        self.nom_fichier = nom_fichier  # Fichier d'enregistrement
        self.f_traitement = f_traitement  # Fonction pour obtenir les grandeurs voulues
        self.t_obs = tobs  # Durée d'observation
        self.titre = titre # En-tête pour le fichier de données

    def get_port(self):
        """Détection et choix du port série
        Le nom du port série à choisir s'obtient lorsqu'on téléverse
        le programme dans le micro controlleur dans le logiciel
        Arduino.
        """
        ports = serial.tools.list_ports.comports(include_links=False)  # Liste des ports actifs
        if (len(ports) != 0):
            if (len(ports) > 1):
                print(str(len(ports)) + "ports actifs ont ete trouves")
                ligne = 1
                for port in ports:
                    print(str(ligne) + ':' + port.device)
                    ligne = ligne + 1
                portChoisi = int(input('Ecrivez le numero du port desire'))  # On demande le choix du port
            else:
                print("1 port actif a ete trouve")
                print(ports[0].device)
                portChoisi = 1

            nom_port = ports[portChoisi - 1].device

            """Données pour la connexion série"""
            vitesse_baud = 115220  # Doit être le même que dans le programme Arduino
            read_timeout = 1
            write_timeout = 1
            port_serie = Serial(port=nom_port, baudrate=vitesse_baud, timeout=read_timeout, writeTimeout=write_timeout)
            return port_serie
        else:  # Aucun port série
            raise ValueError("Aucun port serie n'a ete trouve. Verifier les branchements.'")

    def read_data(self):
        """Fonction qui acquiert les données depuis Arduino et
        les traite. Sa compréhension n'est pas nécessaire."""
        port_serie = self.get_port()  # Création de la liaison avec Arduino
        with open(self.nom_fichier, 'w') as f_data: # Ouverture du fichier pour enregistrement.
            f_data.write("t(ms)," + self.titre)
            t_in = 0
            while t_in <= self.t_obs:
                if port_serie.isOpen():  # Vérification de la connection
                    toread = port_serie.readline()  # Lecture d'une ligne de mesure
                    toread = toread.decode("utf-8").split(",")  # Séparation Delta t et Tension
                    if len(toread) == 2:
                        t_in = t_in + int(toread[0])  # Nouveau temps
                        data_y = self.f_traitement(int(toread[1]))
                        print("t(ms) : ", t_in, "; ",self.titre," : ", data_y)  # A changer pour être plus général
                        f_data.write(str(t_in) + "," + str(data_y))
                        yield [t_in, data_y]  # Comme return mais la fonction continue a être exécutée
                    else:
                        print("RAS")
                        yield []
                else:
                    print("Port serie ferme. Acquisition impossible.")
                    yield []
            print("Fin")
            port_serie.close()


# def CNA(Ubinaire):
#     """ Fonction qui calculer la tension comprise entre 0 et 5V (flottant) à partir
#     de sa représentation binaire (un nombre entier compris entre 0 et 1023)
#     """
#     U = float(Ubinaire) / 1024 * 5
#     return U
#
# def Rdiv(U):
#     """Renvoie Rth connaissant la tension aux bornes de Rpont"""
#     return Rpont * (Vcc / U - 1)
#
# def Tth(R):
#     """Renvoie T (en degré) connaissant Rth"""
#     return (1 / (np.log(R / R0) / beta + 1 / T0)) - 273.15