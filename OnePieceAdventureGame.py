# One Piece Fan Game - Inspired by One Piece
# ------------------------------
# This is a fan-made project inspired by Eiichiro Oda's One Piece.
# I do not own One Piece, its characters, story, or any related assets.
# All rights belong to their respective owners (Shueisha, Toei Animation).
# This game is made purely for fun and educational purposes.
# No copyright infringement intended.

name = input("Hello, my name is Kaizo. What's your name, kid? ")
print("Welcome " + name + ", To The One Piece!")

q1 = input("You are currently in Hoshima Village. I heard you wanted to join The Crimson Tide Pirates. (Y/N) ").lower()

if q1 == "y":
    print("Wow, you dream big kid. The thing is, it's gonna take a lot of work to join their crew.")
    print("First, you need to prove yourself. You have two options:")
    
    q2 = input("Do you want to (1) Train with the swordmaster, or (2) Steal a treasure from the Marines? (1/2) ")

    if q2 == "1":
        print("You head to the swordmaster's dojo. He looks at you and says, 'Show me what you've got!'")
        print("You grab a wooden sword and prepare to fight...")
        # You can continue the battle sequence here!
        
    elif q2 == "2":
        print("You sneak into the Marine base at night, your heart pounding...")
        print("One wrong move and you'll be caught!")
        # Add stealth mechanics or choices here!

    else:
        print("You hesitated... Looks like you're not ready yet.")
    
elif q1 == "n":
    print("Oh, well see you later kid.")
    quit()

else:
    print("What?")


