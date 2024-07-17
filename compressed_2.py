# //Implement a function to perform basic string compression
# //        using the counts of repeated characters. For example,
# //        the string "aabcccccaaa" would become "a2b1c5a3".
# //        Example: Input: "aabcccccaaa" -> Output: "a2b1c5a3"


# word = input("enter the word:")  "aabcccccaaa"  "aabcccccaaa"

word = "aabcccccaaa"
chars = [*word]

text = ""
count = 0
i=j=0

# last_char = chars[0]
while i < len( chars):
    count = 0
    for j in range(i, len(chars)):

        if chars[i] == chars[j]:
            count += 1
        else:
            i=j-1
            break

    text = text + chars[i] + str(count)
    i+=1
    if j == len(chars)-1:
        break

print(text)

















