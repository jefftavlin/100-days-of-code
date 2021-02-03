# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
avg = round(sum(student_heights) / len(student_heights))
print(avg)
