###################
# VERSION 1.00.00 #
###################
Version = "1.00.00"
upDate = "10 May 2026"
versionString = "Version " + Version + " -  Last Updated " + upDate

from tkinter import *
from fractions import Fraction

def calculate(*args):
    try:
        # Retrieve input and calculate

        chanceFraction = float(Fraction(mainTextChanceX.get("1.0",'end-1c')))
        lessChance = (1 - chanceFraction)
        killsPerformed = int((mainTextKillsY.get("1.0",'end-1c')))
        result = round(100*(1 - lessChance**killsPerformed), 2)
        # Update result label
        result_label.config(text=f"Chance = {result}%")
    except ValueError:
        # Handle non-numeric input
        result_label.config(text="Result: Invalid Input")

########################
# VARIABLE DEFINITIONS #
########################




##################
# GUI GEOMETRIES #
##################

#DISPLAY DIMENSIONS
root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.destroy()

#WINDOW GEOMETRIES
mainWidth = 300
mainHeight = 120

#WINDOW POSITIONING
mainCornerX = (screenWidth - mainWidth) / 2
mainCornerY = (screenHeight - mainHeight) / 2

#############
# MAIN MENU #
#############

#INITIALIZING AND CONFIGURING
mainWindow = Tk()
mainWindow.geometry('%dx%d+%d+%d' % (mainWidth, mainHeight, mainCornerX, mainCornerY))
mainWindow.resizable(False, False)
mainWindow.title("Chance to Kill")

mainLabelInputX = Label(mainWindow, text="Input chance of drop in format a/b")
mainTextChanceX = Text(mainWindow, width=10, height=1)

mainLabelInputY = Label(mainWindow, text="Input number of kills performed")
mainTextKillsY = Text(mainWindow, width=10, height=1)

mainLabelInputX.pack()
mainTextChanceX.pack()
mainTextChanceX.bind('<KeyRelease>', calculate)

mainLabelInputY.pack()
mainTextKillsY.pack()
mainTextKillsY.bind('<KeyRelease>', calculate)

result_label = Label(mainWindow, text="Chance = ")
result_label.config(fg='blue')
result_label.pack()

mainWindow.mainloop()
