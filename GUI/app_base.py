import TKinterModernThemes
from .functionalities import *
import tkinter as tk
from tkinter import ttk
import sys
import os


class App(TKinterModernThemes.ThemedTKinterFrame):

    @staticmethod
    def resource_path(relative_path):
        # """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def __init__(self, theme, mode, usecommandlineargs=False, usethemeconfigfile=False):

        super().__init__(str("Biwenger Analysis"), theme, mode, usecommandlineargs=usecommandlineargs,
                         useconfigfile=usethemeconfigfile)

        self.panedWindow = self.PanedWindow("Paned Window Test")
        self.pane = self.panedWindow.addWindow()  # pane1 is a widget frame

        self.notebook = self.pane.Notebook("Notebook Test")
        self.home = self.notebook.addTab("Home")
        self.packs = self.notebook.addTab("Packs")
        self.player = self.notebook.addTab("Player Info")

        # HOME #

        self.logo_path = tk.PhotoImage(file=self.resource_path("aux_files/logo.png"))
        self.home.Label("Welcome to Biwenger Analysis")
        self.home.logo = ttk.Label(self.home.master, image=self.logo_path)
        self.home.logo.grid(row=1,
                            column=0)

        # PACKS #

        type_ = tk.StringVar()
        chance = tk.StringVar()

        def pack_chances():
            chance.set(profit_chance(type_.get()))
            self.packs_output.destroy()
            self.packs_output = self.packs.Label(text=chance.get())

        self.pack_pick = self.packs.Combobox(["Gold", "Silver", "Bronze"],
                                             type_)

        self.pack_button = self.packs.Button(text="Calculate Chances", command=pack_chances)
        self.packs_output = self.packs.Label(text=chance.get())

        # PLAYERS #
        player = tk.StringVar()
        performance = tk.StringVar()

        def get_performance():
            try:
                performance.set(player_performance(player.get()))
            except Exception as e:
                performance.set("Please choose a valid Player")
                print(e)
            self.performance_output.destroy()
            self.performance_output = self.player.Label(text=performance.get())

        self.pack_pick = self.player.Combobox(data.data['name'].tolist(),
                                              player)
        self.performance_button = self.player.Button("Get Performance Rate", get_performance)
        self.performance_output = self.player.Label(text=performance.get())

        self.run(
            cleanresize=True, recursiveResize=True
        )
