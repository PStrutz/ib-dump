# This is a scaffolding for a possible implementation of the 4 colour theorem
# for any map that is coded as a textfile and given as an input option

import tkinter
from tkinter import *
import random
import os

os.chdir("/Users/patriciastrutz/OneDrive - Munich International School/Grade 11/Computer Science")
random.seed()

# defining a tuple with colours - fill in your favourite colours as strings
#colors = ( , , , )

#dictionaries to store information on neighboring regions and region index
border = {}
state = {}

assigned_colors = []
colors = ("red", "green", "blue", "yellow")
tries = 1000

def readBorders():
    ''' the functions reads data from a file and creates a dictionary
with a region as a key and the list  of its neighbours as its value.
It returns a number of regions in a map'''
    file = open(mapname, "r", encoding = "utf-8")
    nr_regions = 0
    for line in file:
        terms = line.strip().split(",")
        border[terms[0]] = terms[1::]
        state[terms[0]] = nr_regions
        nr_regions += 1
    for i in range(0, nr_regions):
        assigned_colors.append("")
    #print(state)
    return nr_regions

# defining auxillary functions
def randomColors(choices):
    """ choices is an integer parameter, being equal to 4 or 3,
the functions assignes 4 (or 3) random colors to all the regions"""
    for index in state.values():
        assigned_colors[index] = colors[random.randint(0,choices-1)]


def checkColors():
    """ the function checks whether all colors have been assigned correctly,
it return True of False correpondingly"""
    for key in border:
        for neighbor in border[key]:
            if assigned_colors[state[key]] == assigned_colors[state[neighbor]]:
                return False
    return True
                

# The functions prints all he regions with the corresponding colors
def listColors():
    for key in state:
        result = key, " = ", assigned_colors[state[key]]
        #print(result)
        results["text"] = results["text"] + "\n" + ''.join(result)

# This is the core function, that implements all the logic
# and calls readBorders(), randomColors(), and checkColors
def main(choices):
    """ the int choices parameter assumes values 4 or 3,
the return value of True ot False depending on whether a successful
coloring has been found"""
    
    for i in range(tries):   
        randomColors(choices)
        result = checkColors()
        if result == True:
            results["text"] = results["text"] + "\n Number of attempts: " + str(i)
            break
    return result

def start():
    """ running main for 4 or 3 choices"""
    results["text"] = " "
    global mapname
    #mapname = input("enter the name of the txt file storing the map coding ")
    #mapname = "CANADA.txt"
    mapname = map_name.get()
    #print("MAP = ", mapname)
    readBorders()
    #for key, value in border.items():
        #print(key, value)
    result = False
    while not result:
        result = main(3)
        if result == True:
            results["text"] += "\n Completed with 3 colors."
        if result == False:
            result = main(4)
            results["text"] += "\n Completed with 4 colors."
            if result == False:
                results["text"]=("No proper map has been found. Try again by pressing Enter.")
                
    listColors()
 


#start()



root = Tk()
root.title("Map Colorer")
head = Label(root, text = "Enter the name of the file which you would like to use:")
head.pack()
map_name = Entry(root)
map_name.pack()
enterBtn = Button(root, text = "Enter", command = start)
enterBtn.pack()
results = Label(root, text = "Results: \n")
results.pack()
