from datetime import datetime, timedelta

def getCurrent():
    curDate = datetime.now()
    return curDate

def getAfterDate(now,day):
    reDate = now + timedelta(days=day)
    return reDate

nowDate, afterDate = None, None

nowDate = getCurrent()
a=int(input('원하는 날자 수==>'))
afterDate = getAfterDate(nowDate,a)

print(a,'일 후 날짜와 시간 ==>',afterDate)
