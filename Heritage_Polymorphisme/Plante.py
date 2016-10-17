#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 17:55:43 2016
Last modified on Sat Oct 15 10:48:26 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

'''
    Cette declaration permet d'importer tout les membres publics du type de
    base Ressource
'''
from Ressource import Ressource

'''
    Type derive (ou sous-classes, ou sous-type) de Ressource. Declaration
    de l'heritage
'''
class Plante(Ressource):

    __espece = None

    '''
        Constructeur de la classe Plante.
        En Python, tout les membres declares dans les superclasses seront
        appelés comme des membres des sous-classes grace au self.
        A part le constructeur de la superclasse qui doit etre appelé de
        maniere explicite.

        @param quantite
        @param espece
    '''
    def __init__(self, quantite, espece):
        # appel du constructeur de la superclasse
        Ressource.__init__(self, quantite)
        # initialisation de l'attribut prive espece
        self.__espece = espece

    '''
        Accesseur en lecture pour l'attribut prive espece.
    '''
    def getEspece(self):
        return self.__espece

    '''
        Permet la croissance de la plante par l'augmentation de sa taille de
        20 a chaque appel.
    '''
    def croitre(self, quantite):
        self.quantite += quantite

    '''
        Implementation de la methode abstraite evoluer() herite du type de
        base Ressource pour permettre l'evaporation de l'eau par la
        diminution de sa quantite de 20 a chaque appel.
    '''
    def evoluer(self):
        self.croitre(20)
