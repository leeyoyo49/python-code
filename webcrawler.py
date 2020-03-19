import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request 物件，附加Requeest Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析原始碼:用來取得標題

import bs4
root=bs4.BeautifulSoup(data,"html.parser") #解析中
title=root.find_all("div",class_="title")  #尋找class="title"的div標籤
with open("ptt.txt","w",encoding="utf-8") as file:
    for titles in title:
        if titles.a != None:
            file.write(titles.a.string+"\n")
