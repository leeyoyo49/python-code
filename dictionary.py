#集合的運算
s1={3,4,5,6,7,8,8,9}
print(10 not in s1, 9 in s1)
s2={4,5,6,7,8}
#交集(&):取兩個資料中相同的部分
s3=s1&s2
print(s3)
#聯集(|):取兩個集合的相同資料，但不重複
s4=s1|s2
print(s4)
#差級(-):從s1中減去s2重疊的部分
s5=s1-s2
print(s5)
#反交級(^):兩個集合中，取不重複的部分
s6=s1^s2
print(s6)

#把字串中的字母改成集合，set("字串")
sss=set("hello")
print(sss)
#dict 的多種寫法
#list裡面set
a=dict([('appple','a'),('bapple','b')])
print(a)
#dict等於
b=dict(apple='a',bapple='b')
print(b)
#字典的運算:key-value
dic={"apple":"蘋果","banana":"香蕉"}
#替換
dic["apple"]="蘋蘋果果"
#刪除(會兩個一起刪)
del dic["apple"]
print(dic)

#難的::::從獵表的資料產生字典
dic2={x:x*2 for x in [3,4,5,6]}
#[]改成s1,2,3,4...也可以
print(dic2)

#dict.fromkeys(list,value或叫seq)
diction = dict.fromkeys(dic,10)
print(diction)