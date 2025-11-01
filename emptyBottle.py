def drink(numBottles, exchangeBottles):
    if numBottles<exchangeBottles:
        return(0)
    else:
    return(drink(numBottles/exchangeBottles,exchangeBottles))

numBottles=9
exchangeBottles=3

