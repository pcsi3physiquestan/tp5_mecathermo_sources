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
    def __init__(self, ax, maxt=10000, refresh=False):
        self.ax = ax
        self.refresh = refresh
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata, marker='+', linestyle='', label='Température')
        self.ax.add_line(self.line)
        self.ax.set_ylim(0, 40)
        self.ax.set_xlim(0, maxt)
        self.ax.legend()

    def update(self, y):
        if len(y) == 2:
            t = y[0]
            if t < self.maxt:
                self.tdata.append(t)
                self.ydata.append(y[1])
            elif self.refresh:  # reset the arrays
                    self.tdata = [self.tdata[-1]]
                    self.ydata = [self.ydata[-1]]
                    self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                    self.ax.figure.canvas.draw()
                    self.tdata.append(t)
                    self.ydata.append(y[1])
            self.line.set_data(self.tdata, self.ydata)
        return self.line,


def get_port():
    """Détection du port série
    """
    ports = serial.tools.list_ports.comports(include_links=False)
    if (len(ports) != 0):
        if (len(ports) > 1):
            print(str(len(ports)) + "ports actifs ont ete trouves")
            ligne = 1
            for port in ports:
                print(str(ligne) + ':' + port.device)
                ligne = ligne + 1
            portChoisi = input('Ecrivez le numero du port desire')
        else:
            print("1 port actif a ete trouve")
            print(ports[0].device)
            portChoisi = 1

        nom_port = ports[portChoisi - 1].device # A modifier suivant le branchement de l'arduino

        """Données pour la connexion série"""
        vitesse_baud = 115220  # Doit être le même que dans le programme Arduino
        read_timeout = 1
        write_timeout = 1
        port_serie = Serial(port=nom_port, baudrate=vitesse_baud, timeout=read_timeout, writeTimeout=write_timeout)
        return port_serie
    else:
        raise ValueError("Aucun port serie n'a ete trouve. Verifier les branchements.'")

# def Rdiv(U):
#     """Renvoie Rth connaissant la tension aux bornes de Rpont"""
#     return Rpont * (Vcc / U - 1)
#
# def Tth(R):
#     """Renvoie T (en degré) connaissant Rth"""
#     return (1 / (np.log(R / R0) / beta + 1 / T0)) - 273.15