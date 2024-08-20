import requests,json,jsonpath


# save data
def data_save(filename, data):
    file = open(filename,'w')
    file.write(data)
    file.close()
    print("The file was saved successfully !")

res = requests.get('https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8')
# find url
data = jsonpath.JSONPath("$.data.game_packages..main..game_pkgs..url").parse(res.json())

# pos = str(data).find(",")

# save file data
data_save('link.txt',str(data))