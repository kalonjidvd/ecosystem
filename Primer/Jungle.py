#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 12:12:54 2016
Last modified on Mon Oct 17 11:56:54 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

# Importation de tous les membres des classes de la simulation
from Eau import Eau
from Plante import Plante
from Proie import Proie
from Predateur import Predateur

# Fonction principale
def main():
    '''
        Instanciation des objets de la simulation La propriété privée __quantite
         de l'objet Eau est initialisée par défaut dans la définition de la
         classe. Mêmement pour la propriété __quantite de l'objet de type Plante.
    '''
    lePointDeau = Eau()
    laPlante = Plante("Manguier")
    laProie = Proie("Singe")
    lePredateur = Predateur("Lion")

    print("\n\nECOSYSTEM SIMULATION...\n")

    print("\nla proie boit de l'eau...\n")
    laProie.boire(lePointDeau)

    print("la quantité de l'eau est : %d" % lePointDeau.getQuantite())
    print("L'énergie de la proie est : %d\n" % laProie.getEnergie())

    print("le prédateur boit de l'eau...\n")
    lePredateur.boire(lePointDeau)

    print("la quantité de l'eau est : %d" % lePointDeau.getQuantite())
    print("L'énergie du prédateur est : %d\n" % lePredateur.getEnergie())

    print("la proie mange la plante...\n")
    laProie.manger(laPlante)

    print("la taille de la plante est : %d" % laPlante.getTaille())
    print("L'énergie de la proie est : %d\n" % laProie.getEnergie())

    print("le prédateur mange la proie...\n")
    lePredateur.manger(laProie)

    print("l'énergie de la proie est : %d" % laProie.getEnergie())
    print("l'énergie du prédateur est : %d\n" % lePredateur.getEnergie())

    print("L'eau s'evapore...")
    lePointDeau.evoluer()
    print("La plante croit...\n")
    laPlante.evoluer()

    print("la quantité de l'eau est : %d" % lePointDeau.getQuantite())
    print("la taille de la plante est : %d" % laPlante.getTaille())


if __name__ == '__main__':
    main()
