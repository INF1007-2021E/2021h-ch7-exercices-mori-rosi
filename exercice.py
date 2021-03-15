#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math

from turtle import *

import sys # librairire du système; path: liste qui contient tous les paths du système, recherche dans tous ces chemins
sys.path.insert(0, "C:\\Users\morir\Documents\Polytechnique\Hiver 2021\INF1007_Programmation\Exercices GitHub\\2021h-ch6-1-exercices-mori-rosi")
from _exercice_version_prof_ch6 import frequence

# TODO: Définissez vos fonction ici

#1 Volume et masse d'un ellipsoide

def ellipsoide(a = 2, b = 3, c = 5, m_v = 50):
    V = (4/3) * math.pi * a * b * c
    m = V * m_v
    return V, m

#2 Ne pas définir une fonction, seulement print(lambda --> voir main)
# ? Pourquoi meilleur_étudiant c'est en jaune, mais le code fonctionne?
def meilleur_étudiant(dict_notes): # {nom_étudiant: note}
    x = lambda dict_notes:
    print(x(frequence(dict_notes)))
    sorted_notes = sorted(dict_notes, key=dict_notes.__getitem__, reverse=True) # renvoie une liste des noms des étudiants ordonnée des notes les plus hautes aux plus faibles
    return sorted_notes[0]
    # utiliser la fonction lambda: lambda X: for notes in dict_notes.values(): ??



#3 Récursivité; dessiner un arbre
avancer longueur
tourner à droite 45/2 °, tourner à gauche 45/2 °
avancer 3/4 * longueur
reculer et faire les branches à gauche

couleur = vert
forward
right angle droite
backward reculer
pensize épaisseur des traits

def draw_branch(branch_len, pen_size, angle): #--> récursive, else: rien faire donc else absent
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)

        right(angle)
        backward(branch_len)

    if  x<7   :
        begin_fill()
        forward(x)
        right(45/2)

    end_fill()
    return draw_branch(0.75*x)

def draw_tree(): # appelle draw tree --> couleur
    setheading(90) # faire pointer vers le haut
    color("green")
    draw_branch(70, 7, 35)


# #Questions sur une fonction récursive
#     #5 appels
#     # 1 f(3, 5) = 3 + 12 = 15
#     # 2 Cas de base: if b == 1: return a
#     # 3 b va finir par être égal à 1, car il est toujours plus grand que 1 et est un entier
#     # 4 Retourne le produit des 2 nombres


#4 chaîne et séquence d'ADN

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

def saisie():
    chaine = input("Entrez une chaine d'ADN:\n")
    sequence = input("Entrez une sequence d'ADN:\n")

    return chaine, sequence

# ? proportion = nb occurences (2) / nb de caract (19) * 100 ? -->

#? pourquoi proportion est en jaune, mais le code fonctionne quand même?
def proportion(chaine, sequence):

    if valide(chaine, sequence):
        if sequence in chaine:
            occurences = chaine.count(sequence)
            prop = occurences / len(chaine) * 100
        return "La sequence n'est pas incluse dans la chaine."

    else:
        return "La chaine ou la sequence n'est pas valide."

    return prop

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

#1
    mass_vol = ellipsoide() #** retester
    print(mass_vol)

    volume, mass = ellipsoide()
    print(volume)
    print(mass)

    ellipsoide()
    ellipsoide(5, m_v=150)
    ellipsoide(1, 6, 15, 14)
    ellipsoide(18, 17)

#2
    print((lambda phrase: sorted(frequence(phrase), key=frequence(phrase).__getitem__)[-1])("bonjour je m'appelle Rosie."))

    dict_1 = {"Émilie": 80, "Charles": 90}
    print(f"Le meilleur étudiant est {meilleur_étudiant(dict_1)}.")

# 3
    draw_tree()

#4
    chaine = "aldjsfnsrigjb"
    sequence = "ald"
    print(valide(chaine, sequence))
    # print(valide("aldjsfnsrigjb", "ald"))
    print(proportion(chaine, sequence))

    chaine2 = "atgttcaacgtat"
    sequence2 = "gt"
    print(valide(chaine2, sequence2))
    print(proportion(chaine2, sequence2))