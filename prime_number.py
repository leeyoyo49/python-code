x= int(input())
a=0
for y in range(x):
    if y==0:
        continue
    if x%y==0:
        a+=1
if a>2:
    print("非質數")
else:
    print("質數")
    