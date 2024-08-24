from tkinter import *
from tkinter import messagebox
import requests, os, jsonpath
from tkinter import Text

url = "https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8"


class GenshinApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        # create a label
        self.label1 = Label(self, text="游戏版本:", font=20, padx=10, pady=10)
        self.label1.grid(row=0, column=0)
        # create a input
        self.entry1 = Entry(self, font=20)
        self.entry1.grid(
            row=0,
            column=1,
        )
        # create a button
        self.btn01 = Button(self, text="确定")
        self.btn01.grid(row=0, column=2)
        self.btn01["command"] = self.showlinks

    def requestlinks(self):
        self.res = requests.get(url)
        self.resdata = jsonpath.jsonpath(self.res.json(), "$..game_packages..url")
        self.resdata = str(self.resdata).replace(",", "\n")
        self.resdata = self.resdata.replace("[", "")
        self.resdata = self.resdata.replace("]", "")
        self.resdata = self.resdata.replace("'", "")
        fp = open("./resdata.txt", "w")
        fp.write(self.resdata)
        fp.close()

    def showlinks(self):
        self.links = ""
        if self.entry1.get():
            self.requestlinks()
            fp = open("./resdata.txt", "r")
            for line in fp.readlines():
                if self.entry1.get() in line:
                    self.links = self.links + line
            if self.links:
                lastversion = open("./lastversion.txt", "w")
                lastversion.write(self.links)
                lastversion.close()
            else:
                self.links = "There is no " + self.entry1.get() + " version !!!"
                lastversion = open("./lastversion.txt", "w")
                lastversion.write("")
                lastversion.write(self.links)
                lastversion.close()
        else:
            print("error")


root = Tk()
root.title("GenshinTools")
root.geometry("800x600")
app = GenshinApplication(root)

root.mainloop()
