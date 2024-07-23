number_1: str = "999"
number_2: str =  "9"

len_1: int = len(number_1)
len_2: int = len(number_2)

def fil_zero(s, width ) -> str:
    return s.zfill(width + len(s))


max_len: int = max( len(number_1), len(number_2))

if len_1 > len_2:
    number_2 = fil_zero(number_2, len_1-len_2  )
else:
    number_1 = fil_zero(number_1, len_2 - len_1)

print(number_1)
print(number_2)
memory: int = 0
text: str = ""
i: int = 0

while ( i < max_len ):
    print(f"number_1={number_1}")
    print(f"number_2={number_2}")
    last_digit_1: int = int(number_1[-1]) if len(number_1) >1 else int(number_1)
    last_digit_2: int = int(number_2[-1]) if len(number_2) >1 else int(number_2)

    number_1 = number_1[:-1] if len(number_1) > 1 else number_1
    number_2 = number_2[:-1] if len(number_2) > 1 else number_2

    res: int = last_digit_1+last_digit_2 + memory
    last_digit_in_sum = res % 10
    memory = res//10

    text =  str(last_digit_in_sum) + text
    print( text)
    i = i+1

if memory > 0:
    text = str(memory) + text

print(text)



