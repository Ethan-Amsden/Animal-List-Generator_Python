#import subprocess
import tkinter as tk
import customtkinter as CTk
from tkinter import *
import view.AnimalListGUI as VALGUI

"""
Author: Ethan Amsden
Date: 09/13/2023
"""

# START the GUI---------
# create window
main = CTk.CTk()
main.title('Animal List Generator')
main.geometry("400x400")

VALGUI.mainWindow(main)

# MAIN LOOP
main.mainloop()