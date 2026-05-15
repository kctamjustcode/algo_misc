numBottles = 10
numExchange = 3

drunk_bottles = numBottles
empty_bottles = numBottles

while empty_bottles >= numExchange:
    empty_bottles -= numExchange
    numExchange += 1
    drunk_bottles += 1
    empty_bottles += 1

print(drunk_bottles)
