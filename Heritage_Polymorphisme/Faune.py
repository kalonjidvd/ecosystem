#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on Wed Aug 31 18:46:59 2016
Last modified on Sat Oct 15 11:07:56 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

'''
    Type de base (ou surtype, ou superclasse)
'''
class Faune:

    '''
        Les attribut de la superclasse doivent etre declares public pour
        etre accessibles dans les sous-classes. Absence des deux underscore
        devant les noms des attributs.
    '''
    energie = None
    espece = None

    '''
        Constructeur de la classe Faune. Type de base abstrait (ou classe
        abstraite) a cause de la methode abstraite manger().

        @param espece
        @param energie
    '''
    def __init__(self, espece, energie):
        self.espece = espece
        self.energie = energie


    '''
        Accesseur en lecture pour l'attribut publique energie.
    '''
    def getEnergie(self):
        return self.energie

    '''
        Accesseur en ecriture pour l'attribut publique energie.

        @param energie
    '''
    def setEnergie(self, energie):
        self.energie = energie

    '''
        Accesseur en lecture pour l'attribut publique espece.
    '''
    def getEspece(self):
        return self.espece

    '''
        Permet l'augmentation de l'energie des objets Faune de la valeur
        passee en parametre.

        @param energie
    '''
    def augmenterDEnergie(self, energie):
        self.energie += energie

    '''
        Permet aux faunes d'entrer en interaction avec un objet de type Eau
        qui lui est passe en parametre pour s'abreuver. Ce qui entraine une
        diminution de la quantite de l'eau et une augmentation de l'energie
        des objets Faune.

        @param lePointDeau
    '''
    def boire(self, lePointDeau):
        while self.energie <= 81:
            if(lePointDeau.getQuantite() > 19):
                lePointDeau.diminuerDeQuantite(20)
                self.energie += 20

    '''
        Methode abstraite (sans Implementation, sans corps) a implementer
        dans les types derives (ou sous-classes, ou sous-types).

        @param objetConsommable
    '''
    def manger(self, objetConsommable):
        return NotImplemented
