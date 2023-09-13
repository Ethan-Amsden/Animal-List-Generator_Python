import tkinter as tk
import customtkinter as CTk
from tkinter import *
import model.AnimalModule as MAD

# global variables for GUI interface
global entryList
global error
global optList
global optVal

# set a couple global varibales for all functions use as needed
error = "Please select a number to generate a list"
optList = ['1','2','3','4','5']

# retrive the selected dropdown menu value and set it to global variable 'optVal'
def setOptVal(selection):
    global optVal

    try:
        optVal = int(selection)
        #optVal = selection
    except:
        print("Error: " + selection + " is not of type, int")

# control function for generating and displaying animal list
def generate(optVal, entryList):

    param = int(optVal)

    entryList.set(MAD.buildAnimalList(param))

# main window of the app
def mainWindow(main):

    # Variables for the GUI
    global optList
    global optVal
    #optVal = IntVar()
    optVal = optList[1]
    entryList = StringVar()

    CTk.set_appearance_mode("System")  # Modes: system (default), light, dark
    CTk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    # Create Main Frame
    MFrame = CTk.CTkFrame(main)
    MFrame.grid(row=0, column=0, padx=25, pady=35, sticky="nsew")

    # add a label with its string variable
    instructions = "Pick the number of animals for the list then click generate."
    descript = CTk.CTkLabel(MFrame, text=instructions)
    descript.pack()

    # a dropdown list
    optionmenu = CTk.CTkOptionMenu(MFrame, values=optList, command=setOptVal)
    optionmenu.pack()
    optionmenu.set(2)

    # add an entry box to display the animal list
    aniList = CTk.CTkEntry(MFrame, textvariable=entryList, width=350)
    aniList.pack(pady=5)

    # add a button to start the generate button
    gen = CTk.CTkButton(MFrame, text="Generate", command=lambda: generate(optVal, entryList))
    gen.pack()

    # MAIN LOOP
    #main.mainloop()

# Future form window for adding & deleting qlite DB records
def AddUpdateFormWindow(main):

    # create Form window
    #Form = CTk.CTk()
    #Form.title('Animal List Generator')
    #Form.geometry("400x400")

    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")

    # Create Form Frame
    formFrame = CTk.CTkFrame(main)
    formFrame.grid(row=0, column=0, sticky="nsew")

    # a dropdown list that displays the tables of the DB
    optionmenu = CTk.CTkOptionMenu(formFrame, values=["Tables not integrated","tables"])
    optionmenu.pack()
    optionmenu.set("1")

    # Entry Field for getting animal's name
    AnimalEntry = CTk.CTkEntry(formFrame, placeholder_text="Animal Name Here")
    AnimalEntry.pack()

    # Entry Field for getting animal's description
    AnimalDescript = CTk.CTkTextbox(formFrame)
    AnimalDescript.pack()

    # Form LOOP
    #Form.mainloop()
