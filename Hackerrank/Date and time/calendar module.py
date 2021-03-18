# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
mm,dd,yy = map(int,input().split())
print((calendar.day_name[calendar.weekday(yy,mm,dd)]).upper())  #weekday returns the day of the week in number format. so we need weekday function to get the name of the week.
