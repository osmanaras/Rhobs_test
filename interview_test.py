"""
# -*- coding: utf-8 -*-

Created on Sat May  1 11:40:06 2021

@author: osman
"""

import pandas as pd
#import numpy as np
#import json
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import math

import argparse

# Loading data 

# exercice 1 : nombre d'ecouteur par genre musicale
def exo_un(data):
    
    nbMusic = {}
    for liste in data['music']: # recuperation de la liste de music
        for music in liste: # parcours de la liste de music
            if music in nbMusic.keys():# ajout du music dans le dictionaire
                nbMusic[music] += 1
            else:
                nbMusic[music] = 1
    
    return nbMusic


# exercice 2 : age moyen par genre musicale

def exo_deux(data):
    listeners = exo_un(data) # nombre de personne par music
    ageMusic = {} # age des personne par music
    
    for index in range(data.shape[0]):
        liste = data['music'][index] # la 6eme colonne correspond à la colonne music
        assert type(liste) == list
        for music in liste:
            if music in ageMusic.keys():
                ageMusic[music] += data['age'][index] # la 7eme colonne correspond à la colonne age
            else:
                ageMusic[music] = data['age'][index]
    
    for music in ageMusic.keys():
        ageMusic[music] = int(ageMusic[music] / listeners[music])
    
    return ageMusic


# Exercice 3 :Pyramide des ages

def exo_trois(data,cty,slice_size):
    pyramid = {} 
    slice_size = int(slice_size) # transformation en int du slice
    city_data = data[data['city'] == cty] # filtrage par ville
    city_data = city_data.reset_index(drop=True) # reinitialisation de l'index
    maxi = math.ceil(city_data.age.max() / slice_size)  # determine le range de i 
    
    tranches_ages= []
    
    for i in range(maxi):
        # initialisation des bornes
        # inferieur
        if slice_size*i+1 == 1 :
            borneInf = 0 
        else:
            borneInf = slice_size*i+1
        # superieur
        borneSup = slice_size*(i+1)
        
        # ajout de la tranche dans le dictionaire
        tranches_ages.append( str(borneInf)+'-'+str(borneSup))
    
    
    population_par_tranches_ages = [0 for i in range(maxi)]
    
    # determiner la position 
    for age in city_data['age']:
        if age == 0:
            population_par_tranches_ages[0] +=1
        else:
            indice = math.ceil(age/slice_size) - 1
            population_par_tranches_ages[indice] +=1
    
    
    
    pyramid['Age'] = tranches_ages
    pyramid['Pop'] = population_par_tranches_ages
    return pyramid

def run_exo1(df):
    
    print("Exercice 1 : The number of listeners by music.\n")
    print("Result :")
    print(exo_un(df))

def run_exo2(df):
    print("Exercice 2 : The average age by music.\n")
    print("Result :")
    print(exo_deux(df))


def run_exo3(df, city, slice_size):
    print("Exercice 3 : The pyramid age: the function should take 2 parameters a city and slice size. Compute the pyramid only for that city. The slice size is the number of years by which you aggregate people\n")
    test = exo_trois(df, city, slice_size)
    print("Result :")
    print(test)

    # creation d'un mini dataframe a partir du dictionnaire des pyramide des ages
    mini_data = pd.DataFrame.from_dict(test)
    #mini_data['negPop'] = mini_data.Pop * (-1)
    mini_data.head()
    
    # affichage du pyramide des ages
    bar_plot = sns.barplot(x='Pop', y='Age', data=mini_data,order=mini_data['Age'][::-1],lw=0)
    #bar_plot = sns.barplot(x='negPop', y='Age', data=mini_data,order=mini_data['Age'][::-1],lw=0)
    plt.show()



if __name__ == "__main__":
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--run', help="execute un exercice")
    parser.add_argument('--dataPath', help="path to the data")
    parser.add_argument('--city', help="specifie la ville",default='Gay')
    parser.add_argument('--slice', help="specifie le slice",default=10)
    
    args = parser.parse_args()
    
    df = pd.read_json(args.dataPath)
    df = df.transpose()
    df = df.reset_index().rename(columns={"index":"Nom"})
    
    df['birthdate'] = df.birthdate.apply(lambda x: dt.date.fromisoformat(x))
    df['age'] = df.birthdate.apply(lambda x: dt.date.today().year - x.year)

    if args.run == "exo1":
        run_exo1(df)
    elif args.run == "exo2":
        run_exo2(df)
    elif args.run == "exo3":
        run_exo3(df, args.city, int(args.slice))
    elif args.run == "all":
        run_exo1(df)
        print("\n")
        run_exo2(df)
        print("\n")
        run_exo3(df, args.city, int(args.slice))
        print("\n")
    else:
        print(args.run + ' not exist')
    
