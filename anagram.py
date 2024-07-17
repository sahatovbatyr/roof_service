from collections import Counter

word1 = input(" enter first word:")
word2 = input(" enter second word:")


is_anagram = True

if len(word1) != len( word2):
    print("Not anagram")
    quit()


counter1 = Counter([*word1])
counter2 = Counter([*word2])

dict1 = {key: count  for key, count in counter1.items()}
dict2 = {key: count  for key, count in counter2.items()}

for key, value in dict1.items():
    if key not in dict2 or dict2[key] != value:
        is_anagram = False
        break

if is_anagram:
    print("anagram")
else:
    print("Not anagram")





