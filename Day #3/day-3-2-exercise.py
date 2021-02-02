# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

bmi = weight / (height ** 2)
import math

if bmi < 18.5:
  print('underweight')
elif bmi >= 18.5 and bmi < 25:
  print(f'Your BMI is {math.ceil(bmi)}, you have a normal weight.')
elif bmi >= 25 and bmi < 30:
  print(f'Your BMI is {math.ceil(bmi)}, you are slightly overweight.')
elif bmi >= 30 and bmi < 35:
  print(f'Your BMI is {math.ceil(bmi)}, you are obese.')
else:
  print(f'Your BMI is {math.ceil(bmi)}, you are clinically obese.')
