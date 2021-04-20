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


#2 Ne pas définir une fonction, utiliser une fonction lambda -> seulement print(lambda...) --> voir main


# 3 Récursivité; dessiner un arbre

# avancer longueur
# tourner à droite 45/2 °
# avancer 3/4 * longueur
# reculer
# tourne angle * 2
# avance

# couleur = vert
# forward
# right angle droite
# backward reculer
# pensize épaisseur des traits

def draw_branch(branch_len, pen_size, angle): # voir le pattern qui se répète (fonction récursive)
    if branch_len > 0 and pen_size > 0: # on arrête d'appeler la fct si 1 des 3 attributs est inexistant (==0).
                                        # on diminue les 3 arguments à mesure qu'on avance dans la récursivité
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


    # angle change aussi
    # critère d'arrêt -> si la condition n'est pas respectée
    # cas de base -> ne rien faire, ne pas dessiner (n'apparaît pas dans le code)

def draw_tree():
    setheading(90) # faire pointer vers le haut, pointe vers la droite par défaut
    color("green")
    draw_branch(70, 7, 35)


#4 chaîne et séquence d'ADN
def valide(chaine, sequence):
    chaine_valide = True
    sequence_valide = True
    for char in chaine:
        if (char != "a" and char != "t" and char != "g" and char != "c") or len(chaine) == 0:
            chaine_valide = False
    for char in sequence:
        if (char != "a" and char != "t" and char != "g" and char != "c") or len(sequence) == 0:
            sequence_valide = False
    if chaine_valide and sequence_valide:
        return True
    return False


def saisie():
    chain = input("Entrez une chaine d'ADN valide:")
    sequence = input("Entrez une sequence d'ADN valide:")
    if valide(chain, sequence):
        if sequence in chain:
            return f"chaîne: {chain}\nséquence: {sequence}\nIl y a {proportion(chain, sequence)}% de '{sequence}'."
        return "La sequence n'est pas incluse dans la chaine."
    return "Votre chaine ou votre sequence n'est pas valide."


def proportion(chaine, sequence):

    if sequence in chaine:
        occurences = chaine.count(sequence)
        prop = occurences / len(chaine) * 100
        return round(prop, 2)
    return "Erreur"


#5: Questions sur une fonction récursive
    #5 appels
    # 1 f(3, 5) = 3 + 12 = 15
    # 2 Cas de base: if b == 1: return a
    # 3 b va finir par être égal à 1, car il est toujours plus grand que 1 et est un entier
    # 4 Retourne le produit des 2 nombres

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    volume, mass = ellipsoide()
    print(volume)
    print(mass)

    print(ellipsoide())
    print(ellipsoide(5, m_v=150))
    print(ellipsoide(1, 6, 15, 14))
    print(ellipsoide(18, 17))

    # TODO: Pas utile (#2)
    # ma_sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    # x = lambda sentence: list(frequence(ma_sentence).keys())[0]
    # print(x)

    # TODO: Solution (#2)
    ma_sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-2])(ma_sentence))
    # on peut aussi mettre reverse=True dans le sorted et prendre [0]

    # draw_tree()

    ma_chaine = "gctatcttctcga"
    ma_sequence = "agc"
    #print(saisie())
    print(proportion(ma_chaine, ma_sequence))

