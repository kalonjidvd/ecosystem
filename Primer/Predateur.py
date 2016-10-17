#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 11:36:25 2016
Last modified on Fri Oct 14 11:09:53 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

class Predateur:

    __espece = None # Doit etre initialisee lors de l'appel du constructeur
    __energie = 60 # initialisation de l'energie dans la définition de la classe

    '''
        Constructeur de la classe Predateur.

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
    def getEnergie(self, ):
        return self.__energie

    '''
        Accesseur en ecriture pour l'attribut prive energie.

        @param energie
    '''
    def setEnergie(self, energie):
        self.__energie = energie

    '''
        Permet l'augmentation de l'energie du predateur de la valeur passee en
        parametre.

        @param energie
    '''
    def augmenterDEnergie(self, energie):
        self.__energie += energie

    '''
        Permet a un predateur d'entrer en interaction avec un objet de type Eau qui
        lui est passe en parametre pour s'abreuver. Ce qui entraine une diminution
        de la quantite de l'eau et une augmentation de l'energie du predateur.

        @param lePointDeau
    '''
    # L'énergie du prédateur ne peut pas dépasser 100 par sa méthode boire
    def boire(self, lePointDeau):
        while self.__energie <= 81:
            if(lePointDeau.getQuantite() > 19):
                lePointDeau.diminuer(20)
                self.augmenterDEnergie(20)

    '''
        Permet a un predateur d'entrer en interaction avec un objet de type Proie qui
        lui est passe en parametre pour se nourrir. Ce qui entraine une diminution
        de l'energie de la proie et une augmentation de l'energie du predateur.

        @param laProie
    '''
    def manger(self, laProie):
        if(laProie.getEnergie() != 0):
            self.augmenterDEnergie(laProie.getEnergie())
            laProie.setEnergie(0)
