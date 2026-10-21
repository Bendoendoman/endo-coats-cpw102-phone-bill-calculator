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
    overuse(input())
main()