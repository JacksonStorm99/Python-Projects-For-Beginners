# One Piece Fan Game - Inspired by One Piece
# ------------------------------
# This is a fan-made project inspired by Eiichiro Oda's One Piece.
# I do not own One Piece, its characters, story, or any related assets.
# All rights belong to their respective owners.
# This game is made purely for fun and educational purposes.
# No copyright infringement intended.

import random

name = input("Hello, my name is Kaizo. What's your name, kid? ")
print("Welcome " + name + ", To The One Piece!")

q1 = input("You are currently in Hoshima Village. I heard you wanted to join The Crimson Tide Pirates. (Y/N) ").lower()

if q1 == "y":
    print("Wow, you dream big kid. The thing is, it's gonna take a lot of work to join their crew.")
    print("First, you need to prove yourself. You have two options:")
    
    q2 = input("Do you want to (1) Train with the swordmaster, or (2) Steal a treasure from the Marines? (1/2) ")


    # Sword Training Path ⚔️
    if q2 == "1":
        print("\nYou head to the swordmaster's dojo. He looks at you and says, 'Show me what you've got!'")
        print("You grab a wooden sword and prepare to fight... ⚔️")

        # Combat System
        player_hp = 20  # Player's health
        swordmaster_hp = 30  # Swordmaster's health

        while player_hp > 0 and swordmaster_hp > 0:
            input("\nPress Enter to attack! ⚔️")
            player_attack = random.randint(4, 10)  # Random attack damage
            swordmaster_hp -= player_attack
            print(f"You strike with your wooden sword and deal {player_attack} damage! 💥")

            if swordmaster_hp <= 0:
                print("\nYou defeated the Swordmaster! 🏆 He nods in approval.")
                print("'Not bad, kid... Maybe you have what it takes after all.'")
                break  # Exit loop

            swordmaster_attack = random.randint(5, 12)  # Swordmaster attacks
            player_hp -= swordmaster_attack
            print(f"The Swordmaster swings his sword and hits you for {swordmaster_attack} damage! 😨")

            if player_hp <= 0:
                print("\nYou collapse to the ground... You lost. 💀")
                print("'Come back when you're stronger, kid.'")
                break  # Exit loop

    q3 = input("Wow you failed badly kid do you want to continue? (Y/N) ")
    if q3 == "y":
        print("Alright let's go")
        print("\nYou sneak towards the Marine base at night... 🌙")
        print("The treasure is locked away inside, but guards are patrolling everywhere!")
        
        stealth_level = 3  # If this reaches 0, the player gets caught

        while stealth_level > 0:
            print("\nYou approach a hallway with a guard. What do you do?")
            print("1️⃣ Hide behind a barrel 🛢️")
            print("2️⃣ Sneak past quietly 🕶️")
            print("3️⃣ Knock out the guard 🥊")

            choice = input("Choose an action (1/2/3): ")

            if choice == "1":
                success = random.randint(1, 10)  # Random chance to stay hidden
                if success > 3:
                    print("You hold your breath... The guard walks past. 😰✅")
                else:
                    print("The guard hears something and looks around suspiciously... You barely escape! 😨❌")
                    stealth_level -= 1

            elif choice == "2":
                success = random.randint(1, 10)  # Random chance to sneak successfully
                if success > 5:
                    print("You move like a shadow... No one notices you. 😎✅")
                else:
                    print("Your footstep echoes too loudly! The guard turns around. 🚨❌")
                    stealth_level -= 1

            elif choice == "3":
                fight_result = random.randint(1, 10)  # Random chance to win
                if fight_result > 4:
                    print("You knock out the guard silently. Nice work! 💪✅")
                else:
                    print("The guard dodges and calls for backup! 🚨❌")
                    stealth_level -= 2  # Fighting is risky!

            else:
                print("You freeze in place... The guard spots you! 🚨❌")
                stealth_level -= 1

            # Check if the player got caught
            if stealth_level <= 0:
                print("\nYou're surrounded by Marines! You're thrown in jail. 🚔💀")
                print("'Better luck next time, rookie.'")
                quit()

            # If the player succeeds multiple times, they get the treasure!
            if stealth_level > 0 and random.randint(1, 5) == 1:
                print("\nYou finally reach the treasure chest... 💰🏴‍☠️")
                print("You grab the loot and escape into the night! 🎉")
                print("'You might find the One Piece one day after all.'")
                break  # End the loop since the player won

    else:
        print("You hesitated... Looks like you're not ready yet.")
elif q3 == "n":
    quit()

    
elif q1 == "n":
    print("Oh, well see you later kid.")
    quit()

else:
    print("What?")