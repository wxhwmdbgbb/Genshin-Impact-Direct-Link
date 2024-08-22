import requests,jsonpath,os

# 存储链接文本
def save_links(filename, data, version):
    # 分割字符串，使每个连接单独成行
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
    # 删除临时文本
    os.remove('./tempfile.txt')
    print("The file was saved successfully! Please review link.txt documents.")

res = requests.get('https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8')
# 提取下载连接
data = jsonpath.JSONPath("$..game_packages..url").parse(res.json())
version = input("Please input game version:")
# save file data
save_links('link.txt',str(data),version)