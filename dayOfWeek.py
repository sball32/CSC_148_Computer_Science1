# dayOfWeek.py given an arbitrary day, month, and year calculates the exact
# day of the week 0-6 in which the date occurs (0 being Sunday, 1 being
# Monday, etc.).  

# Sydney Ball
# CSC 148-001
# Assignment #1: What day is it?
# 20 January 2024

month = 1-12
day = 1-31
year = 2003-2024 
weekday = 0-6       #note the range for each variable 

print()
print(76*'-')

#Assigning values for inputs of days, months, years
m = int(input("Enter an int between 1 and 12 representing the month: "))
d = int(input("Enter an int between 1 and 31 representing the day in"+
              "the month: "))
y = int(input("Enter an int for the year, e.g. 2021: "))

#Make the date m/d/y
date = (str(m) + '/' + str(d) + '/' + str(y))   #write inital code to organize

#Code in the math from the doomsday equation 
yr_0 = y - (14 - m)//12
leap_0 = yr_0 + (yr_0 // 4) - (yr_0 // 100) + (yr_0 // 400) 
month_0 = m + 12 * ((14 - m) // 12) - 2
day_0 = (d + leap_0 + ((31 * month_0) // 12)) % 7

#Assign the number of week day
final_answer = str(day_0)

#Print the final answer in format
print(date, 'is on day', final_answer +'.')

print(76*'-')
print()
