#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
#Author : OGC
#Creation Date : 04-Oct-2019
#Last Update Date : 04-Oct-2019
#Modificacion : File creation
##

#Function for easy tokenzation. Allow duplicate values
def tokenizator (s : str ) -> list :
    return [i.upper() for i in s]

#Function for histrogram generator, we need to give it a dictionary
def w_histogramd(l: list) -> dict:
    d = {}
    for i in l:
        if i in d.keys():
            d.update({i: d.get(i) + 1})
        else:
            d[i] = 1   
    return d

#Function for histrogam generator, use a wrapper, so we can give a list :D
def histogramd(s : str) -> dict:
    return w_histogramd(tokenizator(s))
#Funition that give us a pseudo graphic histogram, we can pass a pure string or fixed dictionary
#I ignore the fixed string, has no sense !

def histrogam_format(inp):
    if type(inp) == type({}):
        for i in inp.keys(): 
            print(i + " "+ inp.get(i)* "X")

    elif type(inp) == type(''): 
        d = w_histogramd(tokenizator(inp))
        for i in d.keys():
            print(i + " "+ d.get(i)* "X")

    else:
        print("I can't handle this")
        print("Given object " + str(type(inp)))

#Function for compression ratio, just an informative feature
def compressionRatio(sizeBeforeCompresion : int, sizeAfterCompression : int) -> float :
    return sizeBeforeCompresion/sizeAfterCompression

#Function for saving percentage ratio, just an informative feature
def savingPercentage(sizeBeforeCompresion : int, sizeAfterCompression : int) -> str  :
    return str((sizeBeforeCompresion - sizeAfterCompression)/sizeBeforeCompresion *100) + "%"

#####################################################
#Usage examples                                     #
#tokenizator('abbcccdddd')                          #
###########################                         #
#histogramd('abbcccdddd')                           #
#####################################################
#histrogam_format('abbcccdddd')                     #
#histrogam_format({'A': 1, 'B': 2, 'C': 3, 'D': 4}) #
#####################################################
#compressionRatio(1,0.5)                            #
#####################################################
#savingPercentage(1,0.5)                            #
#####################################################








