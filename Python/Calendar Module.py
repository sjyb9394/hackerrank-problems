# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, date, year = map(int, input().split())
print(list(calendar.day_name)[calendar.weekday(year,month,date)].upper())
