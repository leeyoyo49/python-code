file=open("write.txt",mode="w",encoding ="utf-8") #開啟
file.write("brenden Wu\nis brenden Wu\n 哈哈哈") #做事
file.close() #關閉

with open("write.txt", mode="w",encoding="utf-8") as file: #自帶關閉
    file.write("brenden Wu\nis brenden Wu\n 哈哈哈")
with open("write.txt", mode="r",encoding="utf-8") as file:
    a=file.read()
print(a)


sum=0
with open("number.txt", mode="w",encoding="utf-8") as file:
    file.write("12\n3")
with open("number.txt", mode="r",encoding="utf-8") as file:  
     for x in file:
        sum+=int(x)
print(sum)
#json之後再用

