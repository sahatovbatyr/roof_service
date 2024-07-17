import math
number = int( input("Enter the number:"))


def is_prime_number(_number: int) -> bool:
    count = 0
    control_number = int(math.sqrt(_number))+1
    for i in range(1, control_number  ):
        if _number % i == 0: count += 1
        if count > 1: return False

    return True

for i in range(1, number+1):
    is_prime = is_prime_number( i )
    if is_prime: print(i)







