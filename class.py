#定義io有兩個屬性 src 和 say
class io:
    sup=["a","b"]  #這個是列表
    def read(src):
        if src not in io.sup:
            print("nope")
        else:
            print("this is", src)
    def say():
        print("l")
#使用類別
print(io.sup)
io.read("h")
io.read("a")
io.say()
