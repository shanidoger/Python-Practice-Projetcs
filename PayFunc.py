
    #declare function called by monthly pay
    #function have 2 arguments,
    # So user will inform by monthly hours and rates
def Monthlypay(hours, rate):
        Pay = hours * rate
        return Pay
    

    #call fucntion and print 
print(Monthlypay(160,12))
