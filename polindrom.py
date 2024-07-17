
word = input("enter the word:")


word_length = len(word)
index =  word_length/2 if word_length % 2 == 0 else (word_length-1)/2
index = int(index)

for i in range(0, index+1):
    if word[i] != word[-i-1]:
        print(f"{word} is NOT anagram!")
        quit()
print(f"{word} is anagram!")

