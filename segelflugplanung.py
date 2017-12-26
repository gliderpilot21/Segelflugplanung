# -*- coding: utf-8 -*-
from __future__ import division
import math

# TODO: clean code for input
# TODO: consider object oriented programming


# Haupt- bzw. Koordinierungsfunktion
def main():
    # Willkommensnachrichten
    print ("Herzlich Willkommen beim elektronischen Zentralformblatt")
    print ("Derzeit nur 1 Schenkel")

    # Abfrage der nötigen Variablen vom Nutzer
    winddir = input("Windrichtung in °: ")                              # Windrichtung
    vw = input("Windgeschwindigkeit in km/h: ")                         # Windgeschwindigkeit
    rwk = input("Rechtsweisender Kartenkurs (rwK) in °: ")              # rechtsweisender Kurs rwK
    var = input("Ortsmisswisung in ° (Ost + , West -): ")               # Ortsmissweisung
    dev = input("Deviation in °: ")                                     # Deviation --> Kompassfehler
    s = input("Distanz laut Karte in km: ")                             # Distanz laut Karte
    ve = input("Eigengeschwindigkeit in km/h: ")                        # Eigengeschwindigkeit

    # Berechnung der Hilfsgrößen wca und vg
    wca = calcwca(vw, ve, winddir, rwk)                                 # Luvwinkel bzw. Wind Correction Angle (WCA)
    vg = calcvg(ve, wca, winddir, rwk)                                  # Grundgeschwindigkeit

    # Berechnung der Endgrößen
    ksk = calcksk(rwk, wca, var, dev)                                   # Kompasssteuerkurs (KSK)
    t = calctime(s, vg) * 60                                            # Flugdauer in min

    # Ausgabe der Ergebnisse
    print ("Luvwinkel (L / WCA): %.1f" % wca)
    print ("Kompasssteuerkurs (KSK): %.1f°" % ksk)
    print ("Geschwindigkeit über Grund vg: %.1f km/h" % vg)
    print ("Flugdauer: %.1f min" % t)


# vg berechnen
def calcvg(ve, wca, winddir, rwk):
    return ve * math.sin(math.radians((winddir - rwk) - wca)) / math.sin(math.radians(winddir - rwk))


# wca berechnen
def calcwca(vw, ve, winddir, rwk):
    return math.degrees(math.asin(vw / ve * math.sin(math.radians(winddir - rwk))))


# ksk berechnen
def calcksk(rwk, wca, var, dev):
    return rwk + wca - var - dev


# t berechnen
def calctime(s, vg):
    return s / vg


main()

