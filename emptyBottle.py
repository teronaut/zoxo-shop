drank=0
def drink(numBottles, exchangeBottles):
    global drank
    if numBottles<exchangeBottles:
        return(1)
    else:
        return(drink(numBottles/exchangeBottles,exchangeBottles)+drank)
numBottles=9
exchangeBottles=3
print(drink(numBottles, exchangeBottles))

