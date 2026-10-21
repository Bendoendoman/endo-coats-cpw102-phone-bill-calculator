dataUsed = 0


    
    
def overuse(dataUsed):
    tempDataUsed = float(dataUsed)
    if tempDataUsed<=10:
    #true if it is below limit, false if not
        return True
    elif tempDataUsed>10:
        return False
    
def main():
    print("how much data did you use?")
    amountOveruse = float
    tempData = float(input())
    print("how much does your plan cost?")
    tempCost = float(input())
    
    if overuse(tempData) == False:
        amountOveruse = tempData-10
        if tempData > 10 and tempData <= 15:
            print("You are over your data limit")
            print("Moderate extra usage")
            print("Your total bill is: " + (str(tempCost + amountOveruse * 2 )))
        elif tempData > 15:
            print("You are over your data limit")
            print("High extra usage")
            print("Your total bill is: " + (str((tempCost) + amountOveruse * 2 )))
    else:
        print("You are within your data limit")
        print("Your total bill is: " + str(tempCost))

main()