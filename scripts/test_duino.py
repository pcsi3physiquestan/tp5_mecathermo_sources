# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from serial import *
# %matplotlib inline

"""Données pour la connexion série
"""
nom_port = "/dev/ttyACM0" # A modifier suivant le branchement de l'arduino
vitesse_baud = 115220  # Doit être le même que dans le programme Arduino
read_timeout = 1
write_timeout = 1

"""Données sur la sonde CTN"""
beta = 3924  # Beta de la relation Rth(T)
T0 = 25+273.15  # T0  de la relation Rth(T)
R0 = 10 # R0  de la relation Rth(T)
Rpont = 10  # R du pont diviseur
Vcc = 5  # Tension du pont

def Tth(R, beta, R0, T0):
    """Renvoie T connaissant Rth"""
    return (1 / (np.log(R / R0) / beta + 1 / T0)) - 273.15

def Rdiv(U, Rpont, Vcc):
    """Renvoie Rth connaissant la tension aux bornes de Rpont"""
    return Rpont * (Vcc / U - 1)

t_obs = 60000 * 0.1  # Durée d'observation en ms
temperatures = []
temps = []
plt.ion()
f, ax  = plt.subplots()
ax.set_xlim(0, t_obs)
ax.set_ylim(0, 40)
line, = ax.plot(temps, temperatures)
plt.show()
t_in = 0  # Temps
with Serial(port=nom_port, baudrate=vitesse_baud, timeout=read_timeout, writeTimeout=write_timeout) as port_serie:
    time.sleep(2)  # Un temps de latence est nécessaire au démarrage de la communication série
    if port_serie.isOpen():
        port_serie.flush()
        while t_in < t_obs:
            toread = port_serie.readline()
            toread = toread.decode("utf-8").split(",")
            if len(toread) == 2:
                t_in = t_in + int(toread[0])
                us = int(toread[1]) / 1023 * 5
                temp = Tth(Rdiv(us, Rpont, Vcc), beta, R0, T0)
                temperatures.append(temp)
                temps.append(t_in)
                print(t_in, ":", temp)
                line.set_data(temps, temperatures)
                f.canvas.draw()


