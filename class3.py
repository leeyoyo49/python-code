class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    #定義實體方法
    def show(self):
        print(self.x,self.y)
    #到原點距離
    def distance(self):  #0.5次方就是根號
        return ((self.x)**2+(self.y)**2)**0.5
#下面的函式每一個都要寫到
p=point(3,4)
p.show()
result=p.distance()
#他不用
print(result)

class file:
    def __init__(self,name):
        self.name=name
        #未開啟檔案時是None
        self.file=None  
        #我們創的函式
    def open(self):
        #python內建函式，self.file是檔案名字
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
f1=file("write.txt")
f1.open()
data=f1.read()
print(data)








