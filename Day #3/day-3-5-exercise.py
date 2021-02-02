# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

true = ['t','r','u','e']
love = ['l', 'o','v','e']

name_combined = (name1 + name2).lower()
true_count = []
love_count = []

for c in true:
  true_count.append(name_combined.count(c))

for c in love:
  love_count.append(name_combined.count(c))

score = str(sum(true_count)) + str(sum(love_count))

if int(score) >= 40 and int(score) <= 50:
  print(f'Your score is {score}, you are alright together.')
elif int(score) < 10 or int(score) > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
else:
  print(f'Your score is {score}.')
