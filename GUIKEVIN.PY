from colorama import Fore, Back, Style
import tkinter as tk
import time
import os


os.system("cls||clear")
windows = []
windows.append(tk.Tk())

class redditInfo():
    def __init__(self):
        with open("GUIinfo.txt", "r") as infoFile:
            self.info = {}
            iteration = 1
            for line in infoFile.readlines():
                self.info.update({iteration: line})
                iteration += 1
    def updateInfo(self):
        with open("GUIinfo.txt", "r") as infoFile:
            self.info = {}
            iteration = 1
            for line in infoFile.readlines():
                self.info.update({iteration: line})
                iteration += 1
    def getInfoLine(self, linenum):
        return self.info[linenum]

class windows():
    def __init__(self, mainwin, shortcut):
        self.wins = []
        self.widgets = []
        self.wins_dict = {}
        self.wins.append(mainwin)
        #self.widgets.append(mainwin)
        self.wins_dict.update({str(shortcut): self.wins[len(self.wins) - 2]})
        print(Back.RED + "Initialised:")
        print(self.wins_dict)
    def get(self, windir):
        return self.wins_dict[str(windir)]
    def create(self, subwin, shortcut):
        print(self.wins)
        print(self.widgets)
        self.wins.append(subwin)
        #self.widgets.append(subwin)
        self.wins_dict.update({str(shortcut): self.wins[len(self.wins) - 2]})
        print(Back.YELLOW + "Window created:")
        print(self.wins_dict)
    #Debug Need To Be Fixed
    def debug(self, win):
        return "Window: " + str(self.wins) + " | Wins Dictionary: " + str(self.wins_dict) + " | Output: " + str(self.wins_dict[str(win)] + "\nWidgets: " + str(self.widgets))
    def widget_setup(self, windir, shortcut):
        print(Back.BLUE + "Before:")
        print(self.widgets)
        print("After:")
        self.widgets.append({"name": str(windir), "short": str(shortcut)})
        print(self.widgets)
    def widget_create(self, createshortcut, widget, windowshortcut):
        for dictionary_ in self.widgets:
            print(Back.CYAN + "\nDictionary:")
            print(dictionary_)
            print("Shortcut:")
            print(dictionary_['short'])
            if dictionary_["short"] == str(windowshortcut):
                dictionary_.update({len(dictionary_.keys()): str(createshortcut)})
                dictionary_.update({str(createshortcut): widget})
        print(Back.LIGHTMAGENTA_EX)
        print(self.widgets)
    def widget_get(self, shortcut):
        for dictionary_ in self.widgets:
            if type(dictionary_) == "<class 'dict'>":
                return dictionary_[shortcut]
    def widgets_pack(self, winshortcut):
        for dictionary_ in self.widgets:
            if dictionary_["short"] == str(winshortcut):
                iteration = 2
                for keys in range(0, int((len(dictionary_.keys()) - 2) / 2)):
                    dictionary_[dictionary_[iteration]].pack()
                    iteration += 2
    def widget_root(self, widgetshortcut):
        for dictionary_ in self.widgets:
            try:
                if dictionary_[str(widgetshortcut)] != 0:
                    return dictionary_["shortcut"]
            except:
                pass
    def mainloop(self):
        for window in self.wins:
            window.mainloop()


guiInfo = redditInfo()
guiWindows = windows(tk.Tk(), "main")

guiWindows.widget_setup("main", "m1")
guiWindows.widget_create("label1", tk.Label(   guiWindows.widget_get("label1"),   text="hi"), "m1")
#guiWindows.debug("main")
#CREATING SCREENSHOT WINDOW
guiWindows.create(tk.Tk(), "screenShotWindow")
guiWindows.widget_setup("screenShotWindow", "screenShotWidgets")
guiWindows.widget_create("header", tk.Label(guiWindows.widget_get("header"), text="Downloading Screenshots..."), "screenShotWidgets")

#PACKING WIDGETS
guiWindows.widgets_pack("screenShotWidgets")

#RUNNING WINDOWS
guiWindows.mainloop()

print(Back.RESET)