import random
guess =[]
wrongguess=0
correctguess=0
found=0
def random_word_picker():
    global guess
    words = ["flower","elephant","photo","computer"]
    randomindex = random.randint(0,len(words)-1)
    randomword = list(words[randomindex])
    guess=["-"]*len(randomword)
    return randomword

RandomWord = random_word_picker()
print(RandomWord)
print (guess)
while(correctguess<len(RandomWord)and wrongguess<=7):
    letter = input("please type in your guess\n")
    for x in range(0,len(RandomWord)):
     if letter == RandomWord[x]:
            guess[x]=letter
            RandomWord[x]=""
            correctguess=correctguess+1
            found=found+1
            print(guess)
    if (found == 0):
        wrongguess=wrongguess+1
        print(f"Wrong guess, attempts left: {7-wrongguess}")
    found = 0 
    
#Go through the word letter by letter, if letter mathces the guess, take note of the index of the letter, then place the letter at the same index on the guessed word 