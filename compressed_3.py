# //Implement a function to perform basic string compression
# //        using the counts of repeated characters. For example,
# //        the string "aabcccccaaa" would become "a2b1c5a3".
# //        Example: Input: "aabcccccaaa" -> Output: "a2b1c5a3"

# word = input("enter the word:")

word = "bbbaaattatyrrrrbbb"
chars = [*word]
compressed: str =  ""

count = 0
last_char = chars[0]

for i in range(len(chars)):

    if last_char == chars[i]:
        count+=1
    else:
        compressed = compressed +last_char+str(count)
        count = 1
    last_char = chars[i]

compressed = compressed +last_char+str(count)
print(compressed)





