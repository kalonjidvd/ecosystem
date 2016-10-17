#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 11:22:43 2016
Last modified on Fri Oct 14 10:38:09 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

class Proie:

    __espece = None # Doit etre initialisee lors de l'appel du constructeur
    __energie = 40 # Initialisation de l'energie dans la définition de la classe

    '''
        Constructeur de la classe Proie.

        @param espece
    '''
    def __init__(self, espece):
        self.__espece = espece

    '''
        Accesseur en lecture pour l'attribut prive espece.
    '''
    def getEspece(self, ):
        return self.__espece

    '''
        Accesseur en lecture pour l'attribut prive energie.
    '''
    def getEnergie(self):
        return self.__energie

    '''
        Accesseur en ecriture pour l'attribut prive energie.

        @param energie
    '''
    def setEnergie(self, energie):
        self.__energie = energie

    '''
        Permet l'augmentation de l'energie de la proie de la valeur passee en
        parametre.

        @param energie
    '''
    def augmenterDEnergie(self, energie):
        self.__energie += energie

    '''
        Permet a une proie d'entrer en interaction avec un objet de type Eau qui
        lui est passe en parametre pour s'abreuver. Ce qui entraine une diminution
        de la quantite de l'eau et une augmentation de l'energie de la proie.

        @param lePointDeau
    '''
    # L'énergie de la proie ne peut pas dépasser 100
    def boire(self, lePointDeau):
        while self.__energie <= 81:
            if(lePointDeau.getQuantite() > 19):
                lePointDeau.diminuer(20)
                self.augmenterDEnergie(20)

    '''
        Permet a une proie d'entrer en interaction avec un objet de type Plante qui
        lui est passe en parametre pour se nourrir. Ce qui entraine une diminution
        de la taille de la plante et une augmentation de l'energie de la proie.

        @param laPlante
    '''
    # L'énergie de la proie ne peut pas dépasser 100
    def manger(self, laPlante):
        while self.__energie <= 71:
            if(laPlante.getTaille() > 29):
                laPlante.diminuer(30)
                self.augmenterDEnergie(30)
