#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, "C:\\Users\\69juj\\Google Drive\\Sauvegarde PC\\Cours\\Polytech\\2021 TRIM-3\\INF1007\\Exercice dossier git\\2021a-c01-ch6-1-exercices-Julien9969")
sys.path.insert(0, "C:\\Google drive\\Sauvegarde PC\\Cours\\Polytech\\2021 TRIM-3\INF1007\Exercice dossier git\\2021a-c01-ch6-1-exercices-Julien9969")

from exercice_chap6 import get_recipes, print_recipe

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import csv
import os


# TODO: Définissez vos fonction ici

def comparefiles():
    with open("fichier1.txt", "r") as f_1, open("fichier2.txt", "r") as f_2:
        # ligne_f1 = f_1.readlines()
        # ligne_f2 = f_2.readlines()

        ligne_f1 = f_1.read()
        ligne_f2 = f_2.read()

    # for line in ligne_f1:
    #     if len(ligne_f1) != len(ligne_f2):

    #     for ligne_2 in ligne_f2:

    #         if ligne_2 != line:

    if ligne_f2 == ligne_f1:
        return "les fichiers sont identique"
    else: 
        for i in range(min(len(ligne_f2),len(ligne_f1))):
            if ligne_f1[i] != ligne_f2[i]:
                return f"les fichiers sont different a la position {i} à cette endroit f1 est {ligne_f1[i]} et f2 est {ligne_f2[i]}"

    a = min(len(ligne_f2),len(ligne_f1)) 

    if a == len(ligne_f2):
        return f"les fichiers sont different a la position {a} à cette endroit f2 est vide et f2 est {ligne_f1[a]}"

    if a == len(ligne_f1):
        return f"les fichiers sont different a la position {a} à cette endroit f1 est {ligne_f2[a]} et f1 est vide "



def triple_space():
    texte_reco = str()
    with open("ficher_a_recopier.txt", "r") as f_a_recopier, open("fichier_recopier", "w") as recop:
        texte = f_a_recopier.read()

        recop.write(f_a_recopier.read().replace(" ", "   "))
        # list_text = texte.split(" ")
        
        # for word in list_text:
        #     texte_reco += word +"   "
        
        # recop.write(texte_reco)


def percent_to_letter(PERCENTAGE_TO_LETTER):

    with open("notes.txt", "r") as note, open("note_to_letter.txt", "w") as note_letter :
        lines = note.read()

        lines = lines.split("\n")
        for notes in lines:
            for keys in PERCENTAGE_TO_LETTER:
                if int(notes) in range(PERCENTAGE_TO_LETTER[keys][0], PERCENTAGE_TO_LETTER[keys][1]):
                    txt = notes + "-->" + keys + "\n"
                    note_letter.write(txt)

def interface_recettte():
    option = "abcde"

    x = input("Choisir une option : \n\t\t a) Ajouter une recette \n\t\t b) modifier une recette \n\t\t c) Supprimer une rectte \n\t\t d) Afficher une rectte \n\t\t e) quitter le programme \n\t\t Choix :  ")

    while x not in option:
        x = input("Choisir une option : \n\t\t a) Ajouter une recette \n\t\t b) modifier une recette \n\t\t c) Supprimer une rectte \n\t\t d) Afficher une rectte \n\t\t e) quitter le programme \n\t\t Choix :  ")

    if x == "a":
        recette_ajout()
        interface_recettte()
    elif x == "b":
        to_modifie = input("Recette à modifier :")
        recette_modifier(to_modifie)
        interface_recettte()
    elif x == "c":
        to_delete = input("Recette à supprimer :")
        delete_recette(to_delete)
        interface_recettte()

    elif x == "d":
        to_print = input("Recette à afficher :")
        affiche_recette(to_print)
        interface_recettte()
        
    elif x == "e":
        return print("fin")


def recette_ajout():
    file_path = "recette.csv"
    les_ingredient = str()

    with open("Recette.csv", mode="a+") as livre_recette:
        recette_writer = csv.writer(livre_recette, delimiter=',', lineterminator = '\n')
        if os.stat(file_path).st_size == 0:
            recette_writer.writerow(["Nom de la Recette", "Ingredient de la recette"])

        recette = get_recipes()
        recette = list(recette.items())

        for recipe in recette:
            les_ingredient = str()
            nom_de_recette = recipe[0]
            for ingredient in recipe[1]:
                les_ingredient +=ingredient+"\t"

            recette_writer.writerow([nom_de_recette,les_ingredient])

def recette_modifier(to_modifie):

    with open("Recette.csv", "r") as livre_recette:
        ligne_recette = livre_recette.readlines()
        for index, line in enumerate(ligne_recette):
            if to_modifie in line:
                indice_recette = index

    with open("Recette.csv", "w") as livre_recette:
        recette_a_modif = ligne_recette[indice_recette]
        del ligne_recette[indice_recette]
        print(recette_a_modif)
        
        while True:
            modif = input("quelle ingredient modifier ou q pour quitter: ")
            if modif == "q":
                break
            nouveau = input("quelle est l'ingredient : ")
            recette_a_modif = recette_a_modif.replace(modif, nouveau)

        ligne_recette.insert(indice_recette, recette_a_modif)
        for line in ligne_recette:
            livre_recette.write(line)




        # del ligne_recette[indice_recette]
        # del recette_a_modif[1:]
        # ingredient = input("saisir tout les ingredients ou q pour quitter : ")

        # while ingredient != "q":
        #     recette_a_modif.append(ingredient)
        #     ingredient = input("saisir tout les ingredients ou q pour quitter: ")
        
def delete_recette(to_delete):
    with open("Recette.csv", "r") as livre_recette:
        ligne_recette = livre_recette.readlines()
        for index, line in enumerate(ligne_recette):
            if to_delete in line:
                indice_recette = index

    with open("Recette.csv", "w") as livre_recette:
        del ligne_recette[indice_recette]

        for line in ligne_recette:
            livre_recette.write(line)

def affiche_recette(to_print):
    with open("Recette.csv", "r") as livre_recette:
        ligne_recette = livre_recette.readlines()
        for index, line in enumerate(ligne_recette):
            if to_print in line:
                indice_recette = index

        print(ligne_recette[index])

    
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(comparefiles())

    triple_space()

    percent_to_letter(PERCENTAGE_TO_LETTER)

    interface_recettte()

