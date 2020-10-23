#Exercise 2
#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

def Extratimepay(hours, rate):
    if hours > 40:
        rate = rate + (rate/2)

    pay = hours * rate
    return pay

print(Extratimepay(50,20))