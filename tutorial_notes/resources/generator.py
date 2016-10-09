import math

# A Set to store results
calculated = set()

def calc_generator(num):
    return math.log((num % 7), 5)

counter = 1
while counter < 7:
    num = calc_generator(counter)

    print("log5(" + str(counter) + ") = " + str(num))
    
    if num in calculated:
        print(calculated)

    calculated.add(num)

    counter += 1
