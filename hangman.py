import random
print("This is a hangman game. You will 10 chances to guess the word.")
name=input("What is your name?\n")
print("Good luck "+name+"!")
words=["scraps","studio","language","dictionary","level","school","diary","vehicles","rainbow"]
word=random.choice(words)
# print(word)
guesses=""
turns=10
while turns>0:
    leftGuesses=0
    for char in word:
        if char in guesses:
            print(char)
        else:
         print("_")
         leftGuesses+=1
        #  print(leftGuesses)
    if leftGuesses==0:
        print("Congrats, You guessed the word right!")
        break    
        
    guess=input("Guess a character of the word:")
    guesses+=guess
    if guess not in word:
        turns-= 1
        print("it is wrong")
        print("you have "+str(turns)+" left")
        if turns==0:
            print("The correct word is "+word+"\n"+"Good luck next time!")    