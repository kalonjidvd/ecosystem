#!/usr/bin/python
#-*- coding: utf-8 -*-


"""
Created on Wed Aug 31 17:13:39 2016
Last modified on Sat Oct 15 10:02:53 2016

@author: david KALONJi
@email : kalonjidvd@gmail.com
"""

'''
    Type de base (ou surtype, ou superclasse)
'''
class Ressource:

    '''
        L'attribut de la superclasse doit etre declare public pour etre
        accessible dans les sous-classes. Absence des deux underscore devant
        le nom des attributs.
    '''
    quantite = None

    '''
        Constructeur de la classe Ressource. Type de base abstrait (ou classe
        abstraite) a cause de la methode abstraite evoluer().

        @param quantite
    '''
    def __init__(self, quantite):
        self.quantite = quantite

    '''
        Accesseur en lecture pour l'attribut publique quantite.
    '''
    def getQuantite(self):
        return self.quantite

    '''
        Accesseur en ecriture pour l'attribut publique quantite.
    '''
    def setQuantite(self, quantite):
        self.quantite = quantite

    '''
        Permet la diminution de la quantite des ressources de la valeur
        passee en parametre.

        @param quantite
    '''
    def diminuerDeQuantite(self, quantite):
        self.quantite -= quantite

    '''
        Methode abstraite (sans Implementation, sans corps) a implementer
        dans les types derives (ou sous-classes, ou sous-types).
    '''
    def evoluer(self):
        return NotImplemented
