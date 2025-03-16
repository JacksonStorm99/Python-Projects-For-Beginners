import random


Question1 = input("Hey, Wanna Play A Game? (Y/N) ").lower() # These are the Questions
if Question1 == "y":
    print("Ok, let's begin! ")

if Question1 == "n":
    quit()

Number_Guess = input("Please Input Any Number From 1-20. ") # Stored In A Variable
Number_Guess = int(Number_Guess) # Converted To An Integer
RandomNumber = random.randint(1,20) 
if Number_Guess == RandomNumber:
    print("Yay, you got it right!")

else: 
    print("Oh, you got it wrong :(")
    print("The number was" , RandomNumber)