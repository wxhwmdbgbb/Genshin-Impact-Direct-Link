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
        self.resok = False
        self.showtext = Text(self.master, autoseparators=False, exportselection=True)
        self.showtext.place(anchor="center", width=800, height=480, relx=0.5, rely=0.5)

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
        output = open("./output.txt", "w")
        if self.entry1.get():
            self.requestlinks()
            fp = open("./resdata.txt", "r")
            for line in fp.readlines():
                if self.entry1.get() in line:
                    self.links = self.links + line
            fp.close()
            if self.links:
                output.write(self.links)
                output.close()
            else:
                self.links = "There is no " + self.entry1.get() + " version !!!"
                output.write("")
                output.write(self.links)
                output.close()

        else:
            output.write("error")
            output.close()
        output = open("./output.txt", "r")
        self.showtext.delete("1.0", END)
        self.showtext.insert("insert", output.read())
        print(output.read())
        output.close()


if __name__ == "__main__":
    root = Tk()
    root.title("GenshinTools")
    root.geometry("800x600")
    app = GenshinApplication(root)
    root.mainloop()
