import requests,json,jsonpath


# 存储文本
def data_save(filename, data):
    file = open(filename,'w')
    file.write(data)
    file.close()
    print("The file was saved successfully !")

res = requests.get('https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8')
# 提取下载连接
data = jsonpath.JSONPath("$.data.game_packages..main..game_pkgs..url").parse(res.json())

# 分割字符串，使每个连接单独成行
data = str(data).replace(',',',\n')
data = data.replace('[','')
data = data.replace(']','')
data = data.replace("'",'')
# save file data
data_save('link.txt',str(data))