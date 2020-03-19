def brenden(n1,n2=1):
    print(n1**n2)
n1=int(input("請輸入基數﹔"))
n2=int(input("請輸入次方向﹔"))
brenden(n1,n2)

def avg(*basic):
    sum=0
    for ans in basic:
        sum+=ans
    print(sum/len(basic))
avg(1,2,3,4,5,6,7)
avg(3,4,5)