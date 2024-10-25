# Magic 8-Ball

# My first stab at the Magic 8-Ball was big long code.
import random
playerName = input("Enter Name: ")

def magic_8(randomNumber):
    if randomNumber == 1:
        answer = "Yeah dude! Skibbity!"
    elif randomNumber == 2:
        answer = "def bro"
    elif randomNumber == 3:
        answer = "Most assuredly, my guy"
    elif randomNumber == 4:
        answer = "idk man i'm kinda lost in the sauce here"
    elif randomNumber == 5:
        answer = "ask me when im not busy shreddin' the rails"
    elif randomNumber == 6:
        answer = "nah, " + playerName + " you shouldn't hear this right now"
    elif randomNumber == 7:
        answer = "bad vibes"
    elif randomNumber == 8:
        answer = "it won't happen before GTA6 comes out"
    elif randomNumber == 9:
        answer = "absolutely not"
    else:
        answer = "Error"
    print("Magic 8-Ball's Answer: ", answer)

keep_playing = True
while keep_playing:
    playerQuestion = input("What do you want to know? ")
    randomNumber = random.randint(1,9)
    magic_8(randomNumber)
    
    ask = input("Wanna ask me again? Enter yes/y or no/n: ").lower()
    
    if ask not in ['yes', 'y']:
        keep_playing = False
print("See you on the flip side, bro!")
```

# I wanted to try writing this with more concise code. So I put the responses in a list and had the randomizer just pick a random response.

import random

responses = [
    "Yeah dude! Skibbity!", 
    "def bro", 
    "Most assuredly, my guy", 
    "idk man i'm kinda lost in the sauce here", 
    "ask me when im not busy shreddin' the rails", 
    "nah, you shouldn't hear this right now", 
    "bad vibes", 
    "it won't happen before GTA6 comes out", 
    "absolutely not"
]

playerName = input("Enter Name: ")

keep_playing = True
while keep_playing:
    playerQuestion = input("What do you want to know? ")
    print("Magic 8-Ball's Answer:", random.choice(responses))
    
    ask = input("Wanna ask me again? Enter yes/y or no/n: ").lower()
    keep_playing = ask in ['yes', 'y']

print("See you on the flip side, bro!")

