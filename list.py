numbers=[11,12,13,13,12,24,354,63456,56754]
#numbers裡面的第一個數字
a=numbers[0]
#numbers裡面第二到第七個數字
b=numbers[1:7]
#numbers裡面有多少數字
c=len(numbers)
#新增
numbers=numbers+[69,69,69]
#numbers*2不等於裡面的值乘二
#會變成資料寫兩遍
print(a)
print(b)
print(c)
print(numbers)

#將小於400的資料留下來並且最後乘2
new_list = [number*2 for number in numbers if number<400]
print(new_list)