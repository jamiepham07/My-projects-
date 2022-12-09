# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:25:25 2022

@author: jamie.pham
"""
#for low iq ppl 

import math as math
import numpy as np

    
def getShimCombo(total):
    shimCombo=[]
    for i in range(len(availableShims)):
        if total // availableShims[i]>=1:
            shimCombo.append(np.floor(total/availableShims[i]))
        else:
            shimCombo.append(0)
        total -= np.multiply(shimCombo[i],availableShims[i])
        if (total <= 0):
            break
    return shimCombo                  

#shim addition as suggested by tip/tilt script 
shimToAdd = np.array([float(input("Enter additional shim thickness suggested, in microns: "))])

#shim stack already present
shimCurrent = np.array([float(input("Enter existing shim stack thickness, in microns: "))])

newStack = np.add(shimToAdd,shimCurrent)

#available shim thickness in inches
availableShims = np.array([0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02])
availableShims = availableShims[::-1]

#converting inches to um
availableShims *= 25400

#find combos of shims needed
neededShims = getShimCombo(shimToAdd)
currentShims = getShimCombo(shimCurrent)

#suggestions to add to existing stack 
print("Suggestion for theta shimming, V Product")
print("            If only adding to existing stack: ")

for i in range(len(neededShims)):
    if neededShims[i]!=0:
       print(f"Add {int(neededShims[i])} of {round(availableShims[i],1)} um")
    
#find combos of shims now 
for i in range(len(availableShims)):
    if shimCurrent // availableShims[i]>=1:
        currentShims.append(np.floor(shimCurrent/availableShims[i]))
    else:
        currentShims.append(0)
    shimCurrent -= np.multiply(currentShims[i],availableShims[i])
    if (shimCurrent <= 0):
        break
    

print("            If subtracting some from existing stack & adding some: ")

#shim differential
shimDiff = [neededShims - currentShims for neededShims,currentShims in zip(neededShims,currentShims)]

for i,count in zip(shimDiff,range(len(shimDiff))):  
    if i == 0 and currentShims[count] != 0:
        print(f"Keep {int(currentShims[count])} of {round(availableShims[count],1)} um shims from current stack")
    elif i < 0:
        print(f"Subtract {-int(shimDiff[count])} of {round(availableShims[count],1)} in um")
    elif i > 0: 
        print(f"Add {int(shimDiff[count])} of {round(availableShims[count],1)} in um")
    
print(f"Please make sure that the new total stack equals {round(newStack[0],1)} um before installing on tool!")