# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
days_left = (90 * 365) - (365 * int(age))
weeks_left = (90 * 52) - (52 * int(age))
months_left = (90 * 12) - (12* int(age))

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')
