# Place holder GUI for now, doesn't do anything
from tkinter import *
import numpy as np
root = Tk()

root.title("MotorSim")
root.minsize(width=500, height=300)
root.maxsize(width=1920, height=1080)

# labeling each row
titleRow = ["Grain Type","Grain Length","Grain Diameter","Core Diameter"]
columnLabel = [1,2,3,4]
grainType = [
    "BATES",
    "STAR"
]
type = StringVar(root)
type.set(" ")
gtw = 15 #  width of entry box
i = 0
for titles in titleRow:
    Label(root, text=titleRow[i]).grid(row=0, column=i+1)
    columnLabel[i] = "Grain "+str(i+1)
    Label(root, text=columnLabel[i]).grid(row=i+1, column=0)
    OptionMenu(root, type, *grainType).grid(row=i+1, column=1)
    Entry(root, width=gtw).grid(row=i+1, column=2)
    Entry(root, width=gtw).grid(row=i+1, column=3)
    Entry(root, width=gtw).grid(row=i+1, column=4)
    i += 1

runSim = Button(root, text="Run Simulation")

root.mainloop()







