number = int(input("Number :"))


Factorial = 1

if number < 0:
  print("Negative numbers have not factorial")
elif number == 0:
  print("Result = 1")
else:
  for i in range(1,number +1):
    Factorial = Factorial * i
  print(Factorial)