# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("mehmet.json","r")
json_dosya=json.load(dosya)
print("API-KEY :",json_dosya["Ad"])
print("API-KEY :",json_dosya["Soyad"])
print("API KEY:",json_dosya["access_token"])
print("API KEY:",json_dosya["kimlik"])
