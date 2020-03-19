number=input("請輸入整數:")
number=int(number)

#要如何辨識input的是int還是str?

if type(number) != int:
    print("請輸入純數字")
else:
    for y in range(number):
        if y*y==number:
            print("平方根為: ",y)
            break
    else:
        print("無正整數解")