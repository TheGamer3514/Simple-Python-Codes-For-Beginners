"""
dungeonGame.py
This script implements a simple text-based dungeon adventure game where the player navigates through rooms, encounters monsters, and finds treasures.
"""

import random

def display_intro():
    """Display the introduction of the game."""
    print("Welcome to the Dungeon Adventure!")
    print("You will explore a dark dungeon filled with treasures and monsters.")
    print("Your goal is to find the treasure and escape alive!")
    print("--------------------------------------------------")

def choose_room():
    """Randomly choose a room for the player to enter."""
    return random.choice(["Monster Room", "Treasure Room", "Empty Room"])

def encounter_monster():
    """Simulate encountering a monster."""
    print("Oh no! You have encountered a monster!")
    action = input("Do you want to [f]ight or [r]un? ").lower()
    
    if action == 'f':
        if random.randint(1, 2) == 1:  # 50% chance of winning
            print("You fought bravely and defeated the monster!")
            return True  # Player wins
        else:
            print("You were defeated by the monster. Game over!")
            return False  # Player loses
    elif action == 'r':
        if random.randint(1, 2) == 1:  # 50% chance to escape
            print("You successfully escaped the monster!")
            return True  # Player escapes
        else:
            print("You failed to escape and the monster caught you. Game over!")
            return False  # Player loses
    else:
        print("Invalid action. The monster attacks you!")
        return False  # Player loses

def find_treasure():
    """Simulate finding treasure."""
    treasure_amount = random.randint(1, 100)
    print(f"You found {treasure_amount} gold coins!")
    return treasure_amount

def play_game():
    """Main function to play the game."""
    display_intro()
    total_treasure = 0
    
    while True:
        room = choose_room()
        print(f"\nYou enter the {room}.")
        
        if room == "Monster Room":
            if not encounter_monster():
                break  # Game over if the player loses
        elif room == "Treasure Room":
            total_treasure += find_treasure()
        elif room == "Empty Room":
            print("The room is empty. You find nothing.")

        continue_playing = input("Do you want to explore another room? (yes/no) ").lower()
        if continue_playing != 'yes':
            break  # Exit the loop if the player doesn't want to continue

    print(f"\nYou leave the dungeon with {total_treasure} gold coins. Thanks for playing!")

if __name__ == "__main__":
    play_game()
