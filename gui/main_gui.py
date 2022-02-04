import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main_gui.ui"


class MainWindow:
    def __init__(self, master=None):
        # 1: Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('main_gui', master)

        # 4: Connect callbacks
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()
        
    def setGenerateButtonAction(self, action):
        self.generateAction = action
        
    def generate(self):
        self.generateAction()