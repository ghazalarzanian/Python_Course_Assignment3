from calendar import c
import random
from re import T
from unittest import result

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = str(random.choice(words)) 
win =0
joon = 10
Result_word = str()
print(word)
Result_word = ("-" * len(word))
print(Result_word)# ----
while joon > 0 and Result_word != word :
    print("\n")
    user_character = input() 
    user_character=user_character.lower()
    if user_character in word:
        win +=1
        for j in range(len(word)):
            if word[j] == user_character:
                 Result_word= Result_word[:j] + user_character + Result_word[j+1:]
            j+=1
        print(Result_word)               
    else:
        joon = joon - 1
        print('no')
if Result_word == word:
    print("YOU Winnnnnn!!:)")