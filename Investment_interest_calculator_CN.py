# -*- coding: utf-8 -*-
"""
Calculate the interest of the mutual funds purchased by my mom (CN version)

"""
import datetime
import calendar

amount = input('本金: ')
interest_rate = input('年化利率 (%): ')
day = input('购买天数: ')
starting_date = input('起息日 (YYYY-MM-DD): ')

def interest(amount, interest_rate, day):
    return int(amount) * float(interest_rate)/100 / 365 * int(day)

interest_result = interest(amount, interest_rate, day)

def total(amount, interest_result):
    return float(amount) + float(interest_result)
x = total(amount, interest_result)

print('利息: RMB', round(interest_result, 2),  '本金利息总共: RMB', round(x,2) )

def next_day(date):
    date = date + datetime.timedelta(days = int(day))
    return '到期日： {d}'.format(d=date)
    
word = starting_date.split('-')
YYYY = int(word[0])
MM = int(word[1])
DD = int(word[2])
s_d = datetime.date(YYYY, MM, DD)
deadline = next_day(s_d)

Y = deadline[5:9]
M = deadline[10:12]
D = deadline[13:]
int_Y = int(Y)
int_M = int(M)
int_D = int(D)
print(deadline)

WhichDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
final_day = WhichDays[calendar.weekday(int_Y, int_M, int_D)]
final_day_CN = {"Monday": "星期一", "Tuesday": "星期二", 
                "Wednesday": "星期三", "Thursday": "星期四", 
                "Friday": "星期五", "Saturday": "星期六", "Sunday": "星期天"}
print(final_day_CN[final_day], '及下一个工作日留意手机入账短信提醒')
