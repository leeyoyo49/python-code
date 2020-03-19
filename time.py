import time
import calendar
import datetime
#print(time.localtime())
#print(datetime.date.today())
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print (type(today))  # 檢視獲取到時間的型別
    print (type(yesterday))
    return yesterday
yesterday = getYesterday()
print (("昨天的時間："), yesterday
)
