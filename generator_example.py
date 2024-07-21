def get_digits_sum(number: int) -> int:
    sum = 0

    while (number > 0):
        digit = number % 10
        number = int (number/10)
        sum = sum +digit
    return sum


res = [ print(i) for i in range(1001) if i % 3 == 0 and i % 5 ==0 and get_digits_sum(i)<10  ]

# print(res)


