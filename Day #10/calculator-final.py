from art import logo
from replit import clear
print(logo)

#Calculator

def add(n1, n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide
}

num1 = float(input("What's the first number?: "))
for key in operations:
  print(key)
operation_symbol = input("Pick an operation: ")
num2 = float(input("What's the second number?: "))
function_chosen = operations[operation_symbol]
answer = function_chosen(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

while True:
  question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
  if question == 'n':
    clear()
    break
  operation_symbol = input("Pick an operation: ")
  next_number = float(input("What's the next number?: "))
  function_chosen = operations[operation_symbol]
  answer = function_chosen(answer, next_number)
