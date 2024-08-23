import requests,jsonpath,os
url = 'https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8'
# save links
def save_links(filename, data, version):
    # split strings
    data = str(data).replace(',',',\n')
    data = data.replace('[','')
    data = data.replace(']','')
    data = data.replace("'",'')
    tempfile = open('tempfile.txt','w')
    tempfile.write(data)
    tempfile.close()
    tempfile = open('tempfile.txt','r')
    tempdata = tempfile.readlines()
    file = open(filename,'w')
    datalink = 0
    for line in tempdata:
        if version in line:
            file.write(line)
            datalink = datalink + 1
            # print(line)
    if datalink == 0:
        print("There is no " + version + " version!!!")
        file.write("There is no " + version + " version!!!")
    tempfile.close()
    file.close()
    # delete temporary file
    os.remove('./tempfile.txt')
    print("The file was saved successfully! Please review link.txt documents.")

res = requests.get(url)
# extract the download links
data = jsonpath.JSONPath("$..game_packages..url").parse(res.json())
version = input("Please input game version:")
# save file data
save_links('link.txt',str(data),version)