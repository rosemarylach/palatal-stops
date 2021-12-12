# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:44:02 2020

@author: jtman
"""


import os, random, subprocess, time, re #reading in modules to be used
import tkinter as tk
from playsound import playsound
from tkinter import filedialog


def WriteData(variable, cons, var2, cont):
    v = cons.get()
    if v == variable:
        corr = "Y"
    else:
        corr = "N"
    printline = variable + '\t' + v + '\t' + cont + '\t' + corr + '\n'
    var2.set(1)
    resultsfile = open(results_file, "a")
    resultsfile.write(printline)
    resultsfile.close()
    return printline


    
def Experiment():  #this is the main function in the code, activated when clicking the "Record" button
    begin.destroy()
    question = tk.Label(root, text = "The consonant you heard is closest to the initial consonant in which of the following words?",font = ("Arial", 20)) 
    question.place(x=100, y=100)
    resultsfile = open(results_file, "w")
    printline = 'Stimulus Consonant'+ '\t' + 'Response Consonant' + '\t' + 'Context' + '\t' + 'Correct' + '\n'
    resultsfile.write(printline)
    resultsfile.close()
    
    listofwords = {}  # a blank dictionary which will be filled with text widgets for each word
    #Change button names below
    conslist = [("key", "C"), ("car", "K"), ("chat", "CH"), ("ship", "SH"), ("tap", "T"), ("???","??")]  
    
    x = 0
     
    for item in listofwavs:
        x += 1
        tempitem = item[:len(item)-4]
        cons = re.sub('[^A-Z]', '', tempitem)
        vowel = re.sub('[^a-z]', '', tempitem)
        
        var = tk.StringVar()
        var.set("IY")
        R1 = {}
        xvar = 0
        num = 1
        numcount = 0
        for word, v in conslist:
            xvar += 200
            numcount += 1
            if numcount > 4:
                num += 1
                numcount = 1
                xvar = 200
            R1[word] = tk.Radiobutton(root, text=word, font=("Arial",20), height = 3, width = 6, relief=tk.RAISED, variable = var, value=v)
            R1[word].place(x=xvar,y=num*100 + 100)
            R1[word].update_idletasks()
        playsound(item)
        #play = subprocess.Popen(["C:/Program Files (x86)/sox-14-4-1/sox", item, "-d"],shell=False)   #4)  Change sox location
        #play.wait()
        
        var2= tk.IntVar()
        cont = vowel
        select = tk.Button(root, text = "submit", command=lambda cons=cons, var=var, var2=var2, cont=cont: WriteData(cons, var, var2,cont) )
        select.pack()   #places "begin" button widget in window
        
        select.wait_variable(var2)
        
        for item in R1:
            R1[item].destroy()
        select.destroy()
        
    root.destroy()
    
root = tk.Tk()   #this block pulls up a window for the words to be displayed in
root.geometry('1200x800')   #size of window
root.attributes("-topmost", True)  #keeps window on top
w = tk.Label(root, text="Phoneme Confusion Experiment")  #a widget which displays text
w.pack()    #places the widget in the window


folder = filedialog.askdirectory() #"D:/confusion/"  #1) Change folder
results_file = "../results.txt"
os.chdir(folder) 

files = os.listdir(folder)

listofwavs = []

for item in files:
    if item.endswith(".wav"):
        listofwavs.append(item)


random.shuffle(listofwavs)  #the list "words" is shuffled randomly
    
begin = tk.Button(root, text = "Begin experiment", command=Experiment)   #widget which is the command button--- when clicked it runs the function "Record," (look for def Record() above)
begin.pack()   #places "begin" button widget in window
   
root.mainloop()   #this line keeps the window open throughout the duration