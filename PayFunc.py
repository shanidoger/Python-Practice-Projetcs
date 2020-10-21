
#declare function called by monthly pay
def Monthlypay(hours, rate): #function have 2 arguments, So user will inform by monthly hours and rates
    Pay = hours * rate
    return Pay

#call fucntion and print 
print(Monthlypay(160,12))
