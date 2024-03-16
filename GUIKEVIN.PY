import tkinter as tk
import colorama
import time
import os


os.system("cls||clear")
windows = []
windows.append(tk.Tk())

class windows():
    def __init__(self, mainwin, shortcut):
        self.wins = []
        self.widgets = []
        self.wins_dict = {}
        self.wins.append(mainwin)
        #self.widgets.append(mainwin)
        self.wins_dict.update({str(shortcut): self.wins[len(self.wins) - 2]})
    def get(self, windir):
        return self.wins_dict[str(windir)]
    def create(self, subwin, shortcut):
        self.wins.append(subwin)
        self.widgets.append(list(subwin))
        self.wins_dict.update({str(shortcut): self.wins[len(self.wins) - 2]})
    #Debug Need To Be Fixed
    def debug(self, win):
        return "Window: " + str(self.wins) + " | Wins Dictionary: " + str(self.wins_dict) + " | Output: " + str(self.wins_dict[str(win)] + "\nWidgets: " + str(self.widgets))
    def widget_setup(self, windir, shortcut):
        self.widgets.append({"name": str(windir), "short": str(shortcut)})
    def widget_create(self, createshortcut, widget, windowshortcut):
        for dictionary_ in self.widgets:
            if dictionary_["short"] == str(windowshortcut):
                dictionary_.update({str(createshortcut): widget})
    def widget_get(self, shortcut):
        for dictionary_ in self.widgets:
            if type(dictionary_) == "<class 'dict'>":
                if dictionary_["short"] == shortcut:
                    return dictionary_


guiWindows = windows(tk.Tk(), "main")
guiWindows.widget_setup("main", "m1")
guiWindows.widget_create("label1", tk.Label(text="hi"), "m1")
#guiWindows.debug("main")
print(guiWindows.widget_get("m1"))


