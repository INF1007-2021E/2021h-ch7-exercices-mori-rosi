#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
from turtle import *
import sys # librairire du système; path: liste qui contient tous les paths du système, recherche dans tous ces chemins
sys.path.insert(0, "C:\\Users\morir\Documents\Polytechnique\Hiver 2021\INF1007_Programmation\Exercices GitHub\\2021h-ch6-1-exercices-mori-rosi")
from _exercice_version_prof_ch6 import frequence

# TODO: Définissez vos fonction ici

#2 Volume et masse d'un ellipsoide

def ellipsoide(a = 2, b = 3, c = 5, m_v = 50):
    V = (4/3) * math.pi * a * b * c
    m = V * m_v
    return V, m

# #3
# # ? Pourquoi meilleur_étudiant c'est en jaune, mais le code fonctionne?
# def meilleur_étudiant(dict_notes): # {nom_étudiant: note}
#     x = lambda dict_notes:
#     print(x(frequence(dict_notes)))
#     sorted_notes = sorted(dict_notes, key=dict_notes.__getitem__, reverse=True) # renvoie une liste des noms des étudiants ordonnée des notes les plus hautes aux plus faibles
#     return sorted_notes[0]
#     # utiliser la fonction lambda: lambda X: for notes in dict_notes.values(): ??



# #4 Récursivité; dessiner un arbre
# # avancer longueur
# # tourner à droite 45/2 °, tourner à gauche 45/2 °
# # avancer 3/4 * longueur
# # couleur = vert
#
# #5 Questions sur une fonction récursive
#     #5 appels
#     # 1 f(3, 5) = 3 + 12 = 15
#     # 2 Cas de base: if b == 1: return a
#     # 3 b va finir par être égal à 1, car il est toujours plus grand que 1 et est un entier
#     # 4 Retourne le produit des 2 nombres
#
#6 chaîne et séquence d'ADN

    # ?expliquer la saisie: générer des caractères aléatoires? longueur aléatoire? ou sasir une portion d'ADN dans une séquence déjà existante? séquence <= ou < chaine

def valide(chaine, sequence):
    chaine_valide = True
    sequence_valide = True
    for char in chaine:
        if char != "a" and char != "t" and char != "g" and char != "c":
            chaine_valide = False
    for char in sequence:
        if char != "a" and char != "t" and char != "g" and char != "c":
            sequence_valide = False
    if chaine_valide and sequence_valide:
        return True
    return False

#def saisie():

# ? proportion = nb occurences (2) / nb de caract (19) * 100 ? -->

#? pourquoi proportion est en jaune, mais le code fonctionne quand même?
def proportion(chaine, sequence):
    if valide(chaine, sequence):
        if sequence in chaine:
            occurences = chaine.count(sequence)
            proportion = occurences / len(chaine) * 100
        return proportion
    return "La chaine ou la sequence n'est pas valide."

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    mass_vol = ellipsoide() #** retester
    print(mass_vol)

    volume, mass = ellipsoide()
    print(volume)
    print(mass)

    ellipsoide()
    ellipsoide(5, m_v=150)
    ellipsoide(1, 6, 15, 14)
    ellipsoide(18, 17)

    print((lambda phrase: sorted(frequence(phrase), key=frequence(phrase).__getitem__)[-1]("bonjour je m'appelle Rosie."))

    # dict_1 = {"Émilie": 80, "Charles": 90}
    # print(f"Le meilleur étudiant est {meilleur_étudiant(dict_1)}.")
    #
    # chaine = "aldjsfnsrigjb"
    # sequence = "ald"
    # print(valide(chaine, sequence))
    # # print(valide("aldjsfnsrigjb", "ald"))
    # print(proportion(chaine, sequence))
    #
    # chaine2 = "atgttcaacgtat"
    # sequence2 = "gt"
    # print(valide(chaine2, sequence2))
    # print(proportion(chaine2, sequence2))