import urllib.request as req
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
resquest=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36"
})
with req.urlopen(url) as response:
    data=json.loads(response.read().decode("utf-8"))
attractionsData=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for data in attractionsData:
        link="http://"+data["file"].split("http://",)[1]#忘記的話，看這裡https://zh-hant.hotbak.net/key/split()%E5%87%BD%E6%95%B8.html
        file.write(data["stitle"]+","+data["latitude"]+","+data["longitude"]+","+link+"\n")
        
