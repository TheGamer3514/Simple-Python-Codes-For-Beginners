"""
dungeonAdventure.py
This script implements an enhanced text-based dungeon adventure game where the player navigates through various rooms,
encounters monsters, finds treasures, and manages an inventory of items.
"""

import random

def display_intro():
    """Display the introduction of the game."""
    print("Welcome to the Enhanced Dungeon Adventure!")
    print("You will explore a dark dungeon filled with treasures and monsters.")
    print("Collect items, fight monsters, and find the ultimate treasure!")
    print("--------------------------------------------------")

def choose_room():
    """Randomly choose a room for the player to enter."""
    return random.choice(["Monster Room", "Treasure Room", "Empty Room", "Item Room"])

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

def find_item():
    """Simulate finding an item."""
    items = ["Health Potion", "Magic Amulet", "Treasure Map"]
    found_item = random.choice(items)
    print(f"You found a {found_item}!")
    return found_item

def display_inventory(inventory):
    """Display the player's inventory."""
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

def play_game():
    """Main function to play the game."""
    display_intro()
    total_treasure = 0
    inventory = []
    
    while True:
        room = choose_room()
        print(f"\nYou enter the {room}.")
        
        if room == "Monster Room":
            if not encounter_monster():
                break  # Game over if the player loses
        elif room == "Treasure Room":
            total_treasure += find_treasure()
        elif room == "Item Room":
            item = find_item()
            inventory.append(item)  # Add found item to inventory
        elif room == "Empty Room":
            print("The room is empty. You find nothing.")
        
        display_inventory(inventory)  # Show inventory after each room

        continue_playing = input("Do you want to explore another room? (yes/no) ").lower()
        if continue_playing != 'yes':
            break  # Exit the loop if the player doesn't want to continue

    print(f"\nYou leave the dungeon with {total_treasure} gold coins and the following items:")
    display_inventory(inventory)
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
