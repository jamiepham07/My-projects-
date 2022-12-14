# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statistics as stat

file_path = r"C:\Users\nguyen.pham\OneDrive - Ultima Genomics\Desktop\Field Curvature Process\field_curvature.xlsx"

data = pd.read_excel(file_path)

tools = data["tool"].tolist()
lower_spec = 0
upper_spec = 0.5

chuck1cam1 = data["Chuck1cam1"].tolist()
chuck1cam2 = data["Chuck1cam2"].tolist()
chuck2cam1 = data["Chuck2cam1"].tolist()
chuck2cam2 = data["Chuck2cam2"].tolist()


toolNum = []
[toolNum.append(x) for x in tools if x not in toolNum]

def findMeanAndError(data):
    allData = []
    mean = []
    err = []   
    for i in range(len(tools)-1):  
        if (tools[i] == tools[i+1]):
            allData.append(data[i])
        else:
            mean.append(stat.mean(allData))
            err.append(stat.stdev(allData)) 
            allData = []
    return mean,err 
def combine2chucks(list1,list2):
    averageList = []
    for x in range(len(list1)):
        averageList.append((list1[x]+list2[x])/2)
        
    return averageList

mean_chuck1cam1,err_chuck1cam1 = findMeanAndError(chuck1cam1) 
mean_chuck1cam2,err_chuck1cam2 = findMeanAndError(chuck1cam2) 
mean_chuck2cam1,err_chuck2cam1 = findMeanAndError(chuck2cam1) 
mean_chuck2cam2,err_chuck2cam2 = findMeanAndError(chuck2cam2) 

toolNum.pop()

toolNum = X = list(map(str, toolNum))

meanMean = [stat.mean(mean_chuck1cam1),stat.mean(mean_chuck1cam2), stat.mean(mean_chuck2cam1), stat.mean(mean_chuck2cam2)]
averageFC = stat.mean(meanMean)
#plot the data 
"""
fig, ax = plt.subplots(2,2)
ax.bar(toolNum, mean_chuck1cam1, yerr=err_chuck1cam1, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_xticks(toolNum)
ax.set_xticklabels(toolNum)

"""
fig = plt.figure()
ax = fig.add_axes([0,0,1.5,1.5])
ax.bar(toolNum, mean_chuck1cam1, yerr=err_chuck1cam1, capsize=5, ecolor='blue')
ax.bar(toolNum, mean_chuck1cam2, yerr=err_chuck1cam2, capsize=5)
plt.axhline(y = 0.5, color = 'r', linestyle = 'dashed')    
plt.axhline(y = averageFC, color = 'g', linestyle = 'dashed')    

#ax.bar(toolNum, mean_chuck2cam1, yerr=err_chuck2cam1, capsize=5, ecolor='blue')
#ax.bar(toolNum, mean_chuck2cam2, yerr=err_chuck2cam2, capsize=5)


plt.title('Field Curvature on V tools - Chuck 1',fontSize=20)
plt.xlabel("V tool", fontSize=20)
plt.ylabel("Field Curvature (um)", fontSize=20)
plt.legend(['Upper Spec','Fleet Average','Cam 1', 'Cam 2'], fontsize=14)
#plt.tight_layout()
plt.show()



