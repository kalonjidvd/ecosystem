# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 06:52:30 2016
Last modified on Mon Oct 17 11:49:21 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

# Déclaration des dictionnaires de données dans la portée globale de l'application

# Le dictionnaire Eau
lePointDeau = {'type' : 'Eau', 'quantite' : 150}

# Le dicionnaire Plante
laPlante = {'type' : 'Plante', 'espece' : 'Manguier', 'taille' : 150}

# Le dictionnaire Proie
laProie = {'type' : 'Proie', 'espece' : 'Singe', 'energie' : 40}

# Le dictionnaire Predateur
lePredateur = {'type' : 'Predateur', 'espece' : 'Lion', 'energie' : 60}


# Déclaration et implémentation des fonctions de l'application


''' Diminue la quantité de la plante ou de l'eau selon la quantité passée en
paramètre.
@param laRessource
@param decroit
 '''
def diminuer(laRessource, decroit):
    if(laRessource['type'] == 'Eau'):
        if(laRessource['quantite'] > decroit):
            laRessource['quantite'] -= decroit

    elif(laRessource['type'] == 'Plante'):
        if(laRessource['taille'] > decroit):
            laRessource['taille'] -= decroit





''' Permet au prédateur et à la proie de s'abreuver au point d'eau.
Elle décrémente la quantité de l'eau pour incrémenter l'energie de l'animal
qui boit '''
def boire(laFaune):
    if(laFaune['type'] == 'Proie'):
        while laFaune['energie'] <= 81:
            if(lePointDeau['quantite'] > 19):
                diminuer(lePointDeau, 20)
                laProie['energie'] += 20
    elif(laFaune['type'] == 'Predateur'):
        while laFaune['energie'] <= 81:
            if(lePointDeau['quantite'] > 19):
                diminuer(lePointDeau, 20)
                lePredateur['energie'] += 20



''' Permet au prédateur de manger la proie et à la proie de maner la plante.
Entraine une décrémentation de la ressource (proie y compris) pour incrémenter
l'energie de l'animal qui mange. '''
def manger(laFaune, laRessource):
    if(laFaune['type'] == 'Proie' and laRessource['type'] == 'Plante'):
        while laFaune['energie'] <= 71:
            if(laRessource['taille'] > 29):
                diminuer(laRessource, 30)
                laFaune['energie'] += 30
    elif(laFaune['type'] == 'Predateur' and laRessource['type'] == 'Proie'):
        if(laRessource['energie'] != 0):
            laFaune['energie'] += laRessource['energie']
            laRessource['energie'] = 0




''' Permet à la Jungle de faire évoluer les ressources : la plante pousse,
tandis que l'eau s'évapore '''
def evoluer():
    lePointDeau['quantite'] -= 20
    laPlante['taille'] += 20

# Point d'entrée de l'application.
def main():

    print("\nla proie boit de l'eau...\n")
    boire(laProie)

    print("La quantite de l'eau est : %d" % lePointDeau['quantite'])
    print("L'énergie de la proie est : %d\n" % laProie['energie'])

    print("le prédateur boit de l'eau...\n")
    boire(lePredateur)

    print("La quantite de l'eau est : %d" % lePointDeau['quantite'])
    print("L'énergie du prédateur est : %d\n" % lePredateur['energie'])

    print("la proie mange la plante...\n")
    manger(laProie, laPlante)

    print("La taille de la plante est : %d" % laPlante['taille'])
    print("L'énergie de la proie est : %d\n" % laProie['energie'])

    print("le prédateur mange la proie...\n")
    manger(lePredateur, laProie)

    print("L'énergie de la proie est : %d" % laProie['energie'])
    print("L'énergie du prédateur est : %d\n" % lePredateur['energie'])

    print("Les ressources evoluent...\n")
    evoluer()

    print("La quantite de l'eau est : %d" % lePointDeau['quantite'])
    print("La taille de la plante est %d\n" % laPlante['taille'])


if __name__ == '__main__':
    main()
