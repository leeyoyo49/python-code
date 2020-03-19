class point:
    def __init__(self, x, y): #那條底線要按兩次
        self.x=x              #一定要用self
        self.y=y              #用來定義實體屬性
p1=point(1,2)
print(p1.x,p1.y)
print(p1)

class fulname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=fulname("yoyo","lee")
name2=fulname("yuyu","lee")
print(name1.first,name1.last)
print(name2.first,name2.last)

