from art import logo
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

num1 = int(input("What's the first number?: "))
for key in operations:
  print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
function_chosen = operations[operation_symbol]
print(f"{num1} {operation_symbol} {num2} = {function_chosen(num1,num2)}")
