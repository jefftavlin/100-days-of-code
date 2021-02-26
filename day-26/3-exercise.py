def func(file):
  with open(file) as file:
    f = [i for i in list(file.readlines())]
  return f
  
f1 = func('file1.txt')
f2 = func('file2.txt')
result = [int(i) for i in f1 if i in f2]


# Write your code above 👆
print(result)
# print(result)
