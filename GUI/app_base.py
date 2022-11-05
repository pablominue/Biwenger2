import TKinterModernThemes as TKMT
from .functionalities import *
import tkinter as tk
from tkinter import ttk
import sys, os
from PIL import Image, ImageTk

class App(TKMT.ThemedTKinterFrame):

    @staticmethod
    def resource_path(relative_path):
        # """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def __init__(self, theme, mode, usecommandlineargs=False, usethemeconfigfile=False):

        super().__init__(str("Biwenger Analysis"), theme, mode, usecommandlineargs = usecommandlineargs,
                         useconfigfile = usethemeconfigfile)


        self.panedWindow = self.PanedWindow("Paned Window Test")
        self.pane = self.panedWindow.addWindow()  # pane1 is a widget frame

        self.notebook = self.pane.Notebook("Notebook Test")
        self.home = self.notebook.addTab("Home")  # tab1 is a widget frame
        self.packs = self.notebook.addTab("Packs")

        ###### HOME ######
        print(self.resource_path("aux_files/logo.png"))
        self.homeframe = self.addFrame("logo")
        self.logo_path = tk.PhotoImage(self.resource_path("aux_files/logo.png"))
        self.home.Label("Welcome to Biwenger Analysis")
        self.home.logo = ttk.Label(self.home.master, image=self.logo_path)
        self.home.logo.grid(row = 3,
                            column=0)

        ###### PACKS ######
        type = tk.StringVar()
        chance = tk.StringVar()
        def pack_chances():
            chance.set(profit_chance(type.get()))
            self.packs_output.destroy()
            self.packs_output = self.packs.Label(text=chance.get())

        self. pack_pick = self.packs.Combobox(["Gold","Silver","Bronze"],
                                              type)

        self.pack_button = self.packs.Button(text="Calculate Chances",command=pack_chances)
        self.packs_output = self.packs.Label(text = chance.get())

        self.run(
            cleanresize=True,recursiveResize=True
        )