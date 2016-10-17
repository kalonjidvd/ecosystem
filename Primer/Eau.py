#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 10:13:39 2016
Last modified on Fri Oct 14 07:02:53 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

class Eau:

    __quantite = 150 # Initialisation de la quantite dans la définition de la classe

    '''
        Constructeur de la classe Eau.
    '''
    def __init__(self):
        pass

    '''
        Accesseur en lecture pour l'attribut prive quantite.
    '''
    def getQuantite(self):
        return self.__quantite

    '''
        Accesseur en ecriture pour l'attribut prive quantite.

        @param quantite
    '''
    def setQuantite(self, quantite):
        self.__quantite = quantite

    '''
        Permet la diminution de la quantite de l'eau de la valeur passee en
        parametre.

        @param decroit
    '''
    def diminuer(self, decroit):
        self.__quantite -= decroit

    '''
        Permet l'evaporation de l'eau par la diminution de sa quantite de 20
        a chaque appel.
    '''
    def evoluer(self):
        self.__quantite -= 20
