
input_text = input("enter the words, examp: aaa bbb ccc:")

words = input_text.split()
print( sorted(words, key=len) )

