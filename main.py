import requests
import json
city = input("მიუთითეთ აშშ-ს ქალაქი: ")
key = 'db23499b205381a4995d7c88fc7fd9e7'
cnt = 16
payload = {'q': city, 'appid': key, 'days': cnt,}
resp = requests.get("https://api.openweathermap.org/data/2.5/forecast/daily", params=payload)
print(resp.url)
#print(resp)
#print(resp.text)
#print(resp.header)
##print(resp.content)
res = json.loads(resp.text)
#print(res)
#print(json.dumps(res, indent=5))
print("ქალაქ", res["name"], "-ში")
print(res["cnt"], "დღის ამინდის პროგნოზია: ")
print(res["temp"])
with open("data.json", 'w') as f:
    json.dump(res, f, indent=5)
