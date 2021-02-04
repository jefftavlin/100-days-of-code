#Write your code below this line 👇
def prime_checker(number):
  divisors = []
  for i in range(1,number):
    if number % i == 0:
      divisors.append(i)
  if len(divisors)  <= 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
