def run():
  year = 1
  month = 1
  date = 1
  dayOfWeek = 2
  sum = 0
  while(not(year == 100 and month == 12 and date == 31)):
    if(date == 1 and dayOfWeek == 0):
      sum = sum + 1

    if(isYearEnd(month, date)):
      year = year + 1
      month = 1
      date = 1
    elif(isMonthEnd(year,month,date)):
      month = month + 1
      date = 1
    else:
      date = date + 1
      
    dayOfWeek = (dayOfWeek + 1) % 7
    
    
  print(sum)

def isYearEnd(month, date):
  return month == 12 and date == 31

monthEnds = [31,28,31,30,31,30,31,31,30,31,30,31]
def isMonthEnd(year, month, date):
  if(month == 2 and year % 4 == 0 and date == 29):
    return True
  if(date == monthEnds[month-1]):
    return True
  return False