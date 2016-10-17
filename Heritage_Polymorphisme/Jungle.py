#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 20:52:30 2016
Last modified on Mon Oct 17 11:50:33 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

# Importations des membres des types derives concrets
from Plante import Plante
from Eau import Eau
from Proie import Proie
from Predateur import Predateur

# Fonction principale
def main():

    '''
        Instanciation des objets des types concrets par l'appel des
        constructeurs.
    '''
    lePointDeau = Eau(150)
    laPlante = Plante(150, "Manguier")
    laProie = Proie("Singe", 40)
    lePredateur = Predateur("Lion", 60)

    '''
        Creation d'une liste lesRessources a l'aide des curly braces pour contenir
        les objets Ressource qui seront sujets au polymorphisme.
    '''
    lesRessources = {}
    lesRessources[0] = lePointDeau
    lesRessources[1] = laPlante

    print("\n\nECOSYSTEM SIMULATION...\n")

    print("\nlaPlante : quantite = %d, type = %s\n"
        % (laPlante.getQuantite(), laPlante.getEspece()))

    print("lePointDeau : quantite = %d\n"
        % (lePointDeau.getQuantite()))

    print("laProie : espece = %s, energie = %d\n"
        % (laProie.getEspece(), laProie.getEnergie()))

    print("lePredateur : espece = %s, energie = %d\n"
        % (lePredateur.getEspece(), lePredateur.getEnergie()))

    print("\nla proie boit de l'eau...\n")
    laProie.boire(lePointDeau)

    print("la quantité de l'eau est : %d"
        % (lePointDeau.getQuantite()))
    print("L'énergie de la proie est : %d\n"
        % (laProie.getEnergie()))

    print("le prédateur boit de l'eau...\n")
    lePredateur.boire(lePointDeau)

    print("la quantité de l'eau est : %d"
        % lePointDeau.getQuantite())
    print("L'énergie du prédateur est : %d\n"
        % lePredateur.getEnergie())

    print("la proie mange la plante...\n")
    laProie.manger(laPlante)

    print("la quantite de la plante est : %d"
        % laPlante.getQuantite())
    print("L'énergie de la proie est : %d\n"
        % laProie.getEnergie())

    print("le prédateur mange la proie...\n")
    lePredateur.manger(laProie)

    print("l'énergie de la proie est : %d"
        % laProie.getEnergie())
    print("l'énergie du prédateur est : %d\n"
        % lePredateur.getEnergie())

    print("Les ressources evoluent...\n")
    # Mise en oeuvre du Polymorphisme
    i = 0
    while i < len(lesRessources):
        lesRessources[i].evoluer()
        i += 1

    print("la quantité de l'eau est : %d"
        % lePointDeau.getQuantite())
    print("la quantite de la plante est : %d"
        % laPlante.getQuantite())


if __name__ == '__main__':
    main()
