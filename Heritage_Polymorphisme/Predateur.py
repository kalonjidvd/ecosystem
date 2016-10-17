#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 19:14:54 2016
Last modified on Sat Oct 15 12:04:08 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

'''
    Cette declaration permet d'importer tout les membres publics du type de
    base Faune
'''
from Faune import Faune

'''
    Type derive (ou sous-classes, ou sous-type) de Faune. Declaration
    de l'heritage
'''
class Predateur(Faune):

    '''
        Constructeur de la classe Proie.
        En Python, tout les membres déclarés dans les types de base seront
        appelés comme des membres des types derives grace au self.
        A part le constructeur du type de base qui doit etre appelé de
        maniere explicite.

        @param espece
        @param energie
    '''
    def __init__(self, espece, energie):
        # appel du constructeur du type de base
        Faune.__init__(self, espece, energie)

    '''
        Implementation de la methode abstraite manger() herite du type de
        base Faune qui met en interaction des predateurs avec des proies
        pour permettre aux predateurs de se ressourcer.

        @param laPlante
    '''
    def manger(self, laProie):
        if(laProie.getEnergie() != 0):
            self.augmenterDEnergie(laProie.getEnergie())
            laProie.setEnergie(0)
