# //Implement a function to perform basic string compression
# //        using the counts of repeated characters. For example,
# //        the string "aabcccccaaa" would become "a2b1c5a3".
# //        Example: Input: "aabcccccaaa" -> Output: "a2b1c5a3"

# word = input("enter the word to compress")

word = "baatttyyyyrrrrr"

if len(word) == 1:
    print(word+str(1))
    quit()

chars = [*word]

s=0
last_char = chars[0]
compressed = ""
char_text = ""
for char in chars:
    if char == last_char:
        s=s+1
        char_text =char+str(s)
    else:
        compressed = compressed + char_text
        s = 1
        char_text =char+str(s)
    last_char = char

compressed = compressed + char_text
print(compressed)