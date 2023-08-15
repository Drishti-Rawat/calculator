# addition
def add(a,b):
  return a+b
# multiplication
def multiply(a,b):
  return a*b
# subtraction
def subtract(a,b):
  return a-b
# division
def divide(a,b):
  return a/b

operation= {
   "+": add,
   "-":subtract,
   "*":multiply,
  "/":divide
}

import art
print(art.logo)
def calculator():
 num1=float(input("what's the first number?: "))
 for symbols in operation:
   print(symbols)
 should_continue = True
 while should_continue:

  operation_symbol = input("Pick an operation : ")
  num2 = float(input("What's the next number?: "))

  calculation = operation[operation_symbol]
  answer =calculation(a=num1,b=num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  ask = input(f"Type 'y' to continue calculating with {answer} and 'n' to start new calculation...  ").lower()
  if ask=="y":
    num1 = answer
  else:
    should_continue = False
    calculator()


calculator()
