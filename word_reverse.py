word:str = input("enter the word:")

#  batyr  rytab
print( word[::-1])

s=""
for i in range(0, len(word)):
    s= s + word[-i-1]
print(s)


