'''
write your pay program using try and except so
that your program handles non-numeric input
gracefully.
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''

def GrossPay():
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))

 # if hours & rate != int:
       # print("write hours and rate in numeric words")

  pay = hours + rate
  return pay

print(GrossPay())