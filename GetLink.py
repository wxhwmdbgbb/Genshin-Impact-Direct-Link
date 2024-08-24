import requests, jsonpath, os, tkinter

url = "https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8"


# save links
def save_links(filename, data, version):
    # split strings
    data = str(data).replace(",", "\n")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace("'", "")
    tempfile = open("tempfile.txt", "w")
    tempfile.write(data)
    tempfile.close()
    tempfile = open("tempfile.txt", "r")
    file = open(filename, "w")
    datalink = 0
    for line in tempfile.readlines():
        if version in line:
            # remove strip
            line.rstrip()
            file.write(line)
            datalink = datalink + 1
            # print(line)
    if datalink == 0:
        # print("There is no " + version + " version!!!")
        file.write("There is no " + version + " version!!!")
        tempfile.close()
        file.close()
        # delete temporary file
        os.remove("./tempfile.txt")
        return False
    tempfile.close()
    file.close()
    # delete temporary file
    os.remove("./tempfile.txt")
    print("The file was saved successfully! Please review link.txt documents.")
    return True


def get_packages(url, version):
    res = requests.get(url)
    # extract the download links
    data = jsonpath.jsonpath(res.json(), "$..game_packages..url")
    # save file data
    save_links("link.txt", str(data), version)


# get_packages(url, "4.8")
mainwindow = tkinter.Tk()
mainwindow.geometry("900x512")
mainwindow.resizable(0, 0)
mainwindow.title("GenshinTools")

# create a label
label1 = tkinter.Label(mainwindow, text="游戏版本:", font=20, padx=10, pady=10)
label1.grid(row=0, column=0)
# create a input
entry1 = tkinter.Entry(mainwindow, font=20)
entry1.grid(
    row=0,
    column=1,
)

# create a button
btn1 = tkinter.Button(
    mainwindow,
    text="确定",
    font=20,
)

btn1.grid(row=0, column=2, padx=5)
links_content = tkinter.Text(
    mainwindow,
    autoseparators=False,
    exportselection=True,
)
links_content.place(
    anchor="center",
    width=900,
    height=480,
    relx=0.5,
    rely=0.55,
)

btn1.bind("FocusIn", print(entry1.get()))
btn1.focus_set()
# f = open("./link.txt", "r")
# links_content.insert("end", f.read())
# f.close()
mainwindow.mainloop()
