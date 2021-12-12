# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:55:38 2021

@author: jtman
"""

import os
import numpy as np

os.chdir("C:/Users/rlach/Documents/Rice/Junior/Semester 1/LING 401/Final Project/Confusion matrix csvs")  #0) Change folder name

filename = 'gage.csv' #1) change file name if needed
numofsounds = 6  # number of columns in spreadsheet
new_array = np.zeros((numofsounds-1,numofsounds-1), dtype = float)
values = np.genfromtxt(filename,delimiter=',',skip_header=1, usecols=range(1,numofsounds))  
for x in range (0,numofsounds-1):
    for y in range (0,numofsounds-1):
        distance = (1 - (values[x][y] + values[y][x]) / (values[x][x] + values[y][y])) * 100
        new_array[x][y] = distance
 
np.savetxt("../Distance matrix csvs/" + filename, new_array, delimiter=",", fmt="%.3f", header="c,k,t͡ʃ,ʃ,t", encoding="utf-8-sig")   #2)  Change output file name if needed