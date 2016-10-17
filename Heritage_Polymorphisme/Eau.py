#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 17:37:20 2016
Last modified on Sat Oct 15 10:36:47 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

'''
    Cette declaration permet d'importer tout les membres publics du type de base
    Ressource
'''
from Ressource import Ressource

'''
    Type derive (ou sous-classes, ou sous-type) de Ressource. Declaration
    de l'heritage
'''
class Eau(Ressource):

    '''
        Constructeur de la classe Eau.
        En Python, tout les membres déclarés dans les superclasses seront
        appelés comme des membres des sous-classes grace au self.
        A part le constructeur de la superclasse qui doit etre appelé de
        maniere explicite.

        @param quantite
    '''
    def __init__(self, quantite):
        # appel du constructeur de la superclasse
        Ressource.__init__(self, quantite)

    '''
        Implementation de la methode abstraite evoluer() herite du type de
        base Ressource pour permettre l'evolution de l'etat de l'eau par l'
        evaporation en diminuant sa quantite de 20 a chaque appel.
    '''
    def evoluer(self):
        self.diminuerDeQuantite(20)
