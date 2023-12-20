rooms = {
    'start': {
        'description': 'You are in a dark room. There is a door to the north and a door to the east.',
        'choices': {
            'north': 'room1',
            'east': 'room2'
        }
    },
    'room1': {
        'description': 'You are in a dusty library. There is a bookshelf to the west and a door to the south.',
        'choices': {
            'west': 'room3',
            'south': 'start'
        }
    },
    'room2': {
        'description': 'You are in a creepy basement. There is a staircase to the west and a door to the south.',
        'choices': {
            'west': 'start',
            'south': 'room4'
        }
    },
    'room3': {
        'description': 'You are in a secret chamber. There is a hidden passage to the east.',
        'choices': {
            'east': 'room1'
        }
    },
    'room4': {
        'description': 'You are in a treasure room. There is a door to the north.',
        'choices': {
            'north': 'room2'
        }
    }
}
inventory = []
player_name = input("Enter your name: ")
current_room = 'start'
while True:
    print(rooms[current_room]['description'])
    print("Available choices:")
    for choice in rooms[current_room]['choices']:
        print(choice)
    player_choice = input("Enter your choice: ")
    if player_choice in rooms[current_room]['choices']:
        current_room = rooms[current_room]['choices'][player_choice]
    else:
        print("Invalid choice. Please try again.")