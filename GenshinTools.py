from tkinter import *
import requests, jsonpath
from tkinter import Text
from tkinter import Tk
from tkinter import messagebox

url = "https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8"


# creat a class to get links
class GenshinDirectLink(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setui()

    # create a ui
    def setui(self):
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
        # create a text box
        self.showtext = Text(self.master, autoseparators=False, exportselection=True)
        self.menu = Menu(self.master, tearoff=False)
        self.menu.add_command(label="复制", command=self.copytext)
        self.master.bind("<Configure>", self.onresize)
        self.showtext.bind("<Button-3>", self.showmenu)
        self.entry1.bind("<Return>", self.pressenter)

    # Send a GET request to get the data
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

    # Read the file and display it
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
            output.write("Error!!!Please enter the game version!")
            output.close()
        output = open("./output.txt", "r")
        self.showtext.delete("1.0", END)
        self.showtext.insert("insert", output.read())
        output.close()

    # When the window size changes the text box is redrawn
    def onresize(self, event=None):
        if event:
            self.showtext_width = self.master.winfo_width()
            self.showtext_height = self.master.winfo_height()
            self.showtext.place(
                anchor="center",
                width=self.showtext_width,
                height=self.showtext_height,
                relx=0.5,
                rely=0.58,
            )

    def copytext(self):
        try:
            self.showtext.clipboard_clear()
            copytext = self.showtext.get(SEL_FIRST, SEL_LAST)
            self.showtext.clipboard_append(copytext)
            messagebox.showinfo("Tips", "复制成功！")
        except TclError:
            messagebox.showerror("Error", "没有选中内容！")

    def showmenu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def pressenter(self, event=None):
        if event:
            self.showlinks()


# create a mainwindow class
class mainwindow(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("GenshinTools")
        self.width = int(self.winfo_screenwidth() / 2)
        self.height = int(self.winfo_screenheight() / 2)
        window_size = "{}x{}".format(self.width, self.height)
        self.geometry(window_size)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.minsize(self.width, self.height)
        self.bind("<Configure>", self.windowresize)

    def windowresize(self, event=None):
        if event:
            self.width = self.winfo_width()
            self.height = self.winfo_height()


if __name__ == "__main__":
    root = mainwindow()
    app = GenshinDirectLink(root)

    root.mainloop()
