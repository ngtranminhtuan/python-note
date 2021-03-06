'''
Created on Jun 26, 2017

@author: xuananh
'''
import datetime
import calendar
import time
import dateutil.parser
from dateutil.tz import tzutc

print('----------------------------------------------------------- timezone')
print(time.tzname)

# print(datetime.datetime(2019, 2, -1))

print('----------------------------------------------------------- convert other format to python datetime')
print('UTC timestamp now 1: ', time.time())
print('UTC timestamp now 2: ', datetime.datetime.now().timestamp())
print('UTC timestamp now 3: ', datetime.datetime.utcnow())
print('UTC timestamp now 4: ', calendar.timegm(time.gmtime()))
print('UTC timestamp to datetime :       ', datetime.datetime.fromtimestamp(1575963196))
print('UTC timestamp to datatime - 24h : ', datetime.datetime.fromtimestamp(1575963196 - 24 * 60 * 60))
print('UTC timestamp to hour :       ', datetime.datetime.fromtimestamp(1575963196).hour)

print('RFC 3339 format: ', dateutil.parser.parse('2008-09-03T20:56:35.450686Z'))
print('                 ', datetime.datetime(2008, 9, 3, 20, 56, 35, 450686, tzinfo=tzutc()))

print('ISO 8601 extended format: ', dateutil.parser.parse('2008-09-03T20:56:35.450686'))
print('                          ', datetime.datetime(2008, 9, 3, 20, 56, 35, 450686))

print('ISO 8601 basic format: ', dateutil.parser.parse('20080903T205635.450686'))
print('                       ', datetime.datetime(2008, 9, 3, 20, 56, 35, 450686))

print('ISO 8601 basic format, date only: ', dateutil.parser.parse('20080903'))
print('                                  ', datetime.datetime(2008, 9, 3, 0, 0))

print('----------------------------------------------------------- format datetime')
my_time = dateutil.parser.parse("2018-06-06T08:01:53.420Z")
print('my_time:          ', my_time)
print("my_time formated: ", my_time.strftime("[%Y-%m-%d]-[%H:%M:%S]"))
my_time = datetime.datetime.now()
print('my_time:          ', my_time)
print("my_time formated: ", my_time.strftime("[%Y-%m-%d]-[%H:%M:%S]"))


print('----------------------------------------------------------- period')
start = datetime.datetime.now()
print("start:          ", start)

print('....spleeping 3s...')
time.sleep(3)

now = datetime.datetime.now()
print("now:          ", now)

period = (now - start).seconds
print("period: ", period)

print('----------------------------------------------------------- datetime ago')
now = datetime.datetime.now()
datetime_7_day_ago = now - datetime.timedelta(days=7)
print("now :           ", now)
print("date_7_day_ago: ", datetime_7_day_ago)

today = datetime.date.today()
date_7_day_ago = today - datetime.timedelta(days=7)
print('today           ', today)
print('date_7_day_ago: ', date_7_day_ago)

print('----------------------------------------------------------- datetime future or past')
now = datetime.datetime.now()
datetime_7_day_ago = now + datetime.timedelta(days=7)
print("now :                 ", now)
print("date_7_day_in_future: ", datetime_7_day_ago)
print("timestamp: ", datetime_7_day_ago.timestamp())

today = datetime.date.today()
date_7_day_ago = today + datetime.timedelta(days=7)
print('today                 ', today)
print('date_7_day_in_future: ', date_7_day_ago)
print("timestamp: ", datetime_7_day_ago.timestamp())

d = datetime.datetime.utcnow()
for i in range(-2, 3):
    d1 = d + datetime.timedelta(minutes=i)
    print(d1.strftime("%Y-%m-%dT%H:%M"))

print('----------------------------------------------- extract year, month, hour, minute')
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

print(datetime.date(1991, 1, 1))