# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:27:12 2021

@author: osman
"""
import json
import datetime as dt
import math



datapath = 'D:\\test_technique\\test_rhobs\\data_rhobs.json'
ct = 'Gay'
slize = 7


def exo_trois(path,slice_sze,cty):
    
    with open(path) as file:        
        data = json.loads(file.read())
    
    pyramid = {}
    tranche_ages =[]
    maxi = math.ceil(150 / slice_sze) # on suppose qu' il n' y a pas de personnes agé de plus 150 ans
    count_ages = [0 for i in range(maxi)] 
    for i in range(maxi):
        if slice_sze *i + 1 == 1:
            born_inf = 0
        else:
            born_inf = slice_sze *i + 1
        
        borne_sup = slice_sze * (i+1)
        
        tranche_ages.append(str(born_inf)+'-'+str(borne_sup))
        
    
    for _,elements in data.items():
        if elements['city'] == cty:
            # determiner l'age
            t_year = dt.date.today().year
            b_year = dt.date.fromisoformat(elements['birthdate']).year
            age =  t_year - b_year
            
            # determiner la position de l'age 
            i = math.ceil(age/slice_sze) - 1
            count_ages[i] +=1
        
    for i in range(maxi):
        cle = tranche_ages[i]
        val = count_ages[i]
        pyramid[cle] = val
        
    return pyramid


print(exo_trois(datapath, slize, ct))