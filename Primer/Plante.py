#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 10:57:14 2016
Last modified on Fri Oct 14 10:02:53 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

class Plante:

    __espece = None # Doit etre initialisee lors de l'appel du constructeur
    __taille = 150 # Initialisation de la taille dans la définition de la classe

    '''
        Constructeur de la classe Plante.

        @param espece
    '''
    def __init__(self, espece):
        self.__espece = espece

    '''
        Accesseur en lecture pour l'attribut prive taille.
    '''
    def getTaille(self):
        return self.__taille

    '''
        Accesseur en ecriture pour l'attribut prive taille.

        @param taille
    '''
    def setTaille(self, taille):
        self.__taille = taille

    '''
        Permet la diminution de la taille de la plante de la valeur passee en
        parametre.

        @param decroit
    '''
    def diminuer(self, decroit):
        self.__taille -= decroit

    '''
        Permet la croissance de la plante par l'augmentation de sa taille de 20
        a chaque appel.
    '''
    def evoluer(self):
        self.__taille += 20
