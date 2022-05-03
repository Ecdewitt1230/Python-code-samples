# Colton DeWitt - Kobe Dog's Quest! - Text Based Game - 4-16-2022 - Updated 5-3-2022
# Note: I left an exit command (go to sleep) in my code because I liked the idea of the
# player being able to quit whenever they want to.


# Function that prints introduction text and player commands
def intro():
    print('Made by: Colton DeWitt')  # Author
    print('Kobe Dog\'s Quest!')  # Title
    print('The family is away, and they left a bunch of tasty rib bones in the trash can! Collect the 6\n'
          'necessary items from around the house to knock the trash can over and get the "Kobe Lock" off its mouth,\n'
          'so that Kobe dog may feast! Or fail and go to sleep in comfy bed.')  # Intro text
    print('Move Commands: go North, go South, go East, go West, go to sleep')  # Move Commands. Kept exit command
    print('Pick up an item: get Item Name')  # Pick up an item command ex. get Bone


# This function prints out the player's/Kobe's current room and his current items
def player_status(items, room):  # Arguments are player's/Kobe's current items and room
    print('\n{}'.format('=' * 25))  # Prints a line of separator text
    print('Kobe is in {}'.format(room))  # Player's/Kobe's current room
    print("Kobe's items: {}".format(items))
    if 'item' in rooms[room]:
        if rooms[room]['item'] not in items:  # If the item in the room has already been acquired, do not print item
            print('Kobe sniffs out a {}!'.format(rooms[room]['item']))
        print('{}'.format('=' * 25))  # Prints a line of separator text
    elif 'villain' in rooms[room]:  # If the villain is in the room, the kitchen, then call the trash_can function
        trash_can(items)
    else:
        print('{}'.format('=' * 25))  # Prints a line of separator text


# The trash_can function is called when player/Kobe enters the kitchen. It prints ending game text
def trash_can(final_items):  # Argument is player's/Kobe's current items/inventory
    print('\nKobe sees the evil trash can!\nCannot resist! Must try to get ribs out!')  # Prints regardless of items
    if len(final_items) == 6:  # Length of a full items list/inventory. This is game win! Victory!
        print('Kobe, now encouraged by his Favorite Cow and the stashed away Taco Bell Wrapper he got\n'
              'from the trash can a week before, cleans his teeth on his Teeth Cleaning Stick,\n'
              'sharpens his teeth with his Bone, devours the Packet of Hot Cocoa Mix for jittery energy,\n'
              'and hauls the Book underneath the evil trash can!\n'
              'While standing on his hind legs on top the book, Kobe shoves the trash can\n'
              'over with a mighty booty slam! Then with the rest of his chocolate high,\n'
              'he pulls the wicked "Kobe Lock" off with a mighty growl!\n'
              'Senses overloading, Kobe devours the rib bones and everything else he can find in the trash can.\n'
              'He then spends the rest of the day shaking and puking up chocolatey BBQ bones until\n'
              'his loving and distraught family comes home.\n')
    else:  # If the items list/inventory is not full, then game over
        print('Kobe tries with all his might to push the trash can over, but he sadly cannot.\n'
              'He even tries to stand on his hind legs and get the lid open with his snoot,\n'
              'but the blasted "Kobe Lock" keeps its mouth shut!\n'
              'With a disgruntled huff, Kobe lumbers into his bed and goes to sleep.\n')


# Movement function that takes desired movement direction and current room as arguments
def movement(direction, room):
    direction = direction.replace('go ', '')  # Get rid of the 'go ' part of the command. Just want the direction
    if direction in rooms[room]:  # Check to see if the desired direction is possible in current room
        new_room = rooms[room][direction]  # If yes, go to that next room in that direction
    else:  # Desired direction is not possible. It is not in the room dict for that room
        print('Kobe cannot go that way!')
        new_room = room  # Player cannot go in desired direction so return current room
    return new_room  # Return the new room that player/Kobe should be in


# Get item function that validates item input and returns desired item to pick up
def get_item(desired_item, room, items):  # Arguments are desired item to pick up, current room and current items
    desired_item = desired_item.replace('get ', '')  # Get rid of the 'get ' part of the command. Just want the item
    if desired_item in items:  # If the player is trying to pick up an item that is already in the inventory
        print('Kobe already has that item!')
        new_item = 'invalid'  # Sets new_item to invalid, which will be removed from inventory immediately after return
    elif desired_item == rooms[room]['item']:  # If the desired item is in current room, then pick it up
        new_item = rooms[room]['item']  # Set new_item to current room's item and return
        print('Kobe snatched up the {}!'.format(rooms[room]['item']))
    else:  # If the desired item is not in current room, let the player know
        print('Kobe does not sniff that item!')
        new_item = 'invalid'  # Sets new_item to invalid, which will be removed from inventory immediately after return
    return new_item  # Return new_item


# Main function containing rooms dict and gameplay loop
if __name__ == '__main__':

    # Rooms of the house and the items in each room.
    global rooms  # Set the dict rooms to global so that functions can access it
    rooms = {
        'Living Room': { 'South': 'Mud Room', 'North': 'Hallway', 'West': 'Back Porch', 'East': 'Office' },
        'Mud Room': { 'North': 'Living Room', 'East': 'Kitchen', 'item': 'Favorite Cow' },
        'Kitchen': { 'West': 'Mud Room', 'villain': 'Trash Can' },  # 'villain' Kobe's nemesis!
        'Back Porch': { 'East': 'Living Room', 'item': 'Taco Bell Wrapper' },
        'Hallway': { 'South': 'Living Room', 'East': "Aunt's Room", 'item': 'Teeth Cleaning Stick' },
        "Aunt's Room": { 'West': 'Hallway', 'item': 'Packet of Hot Cocoa Mix' },
        'Office': { 'West': 'Living Room', 'North': 'Master Bedroom', 'item': 'Book' },
        'Master Bedroom': { 'South': 'Office', 'item': 'Bone' }
    }

    move_commands = ['go North', 'go South', 'go East', 'go West']  # The only movements the player can make

    item_commands = ['get Favorite Cow', 'get Taco Bell Wrapper', 'get Teeth Cleaning Stick',
                     'get Packet of Hot Cocoa Mix', 'get Book', 'get Bone']  # List of get item commands

    intro()  # Call the intro function and print out intro game text and possible commands

    in_room = 'Living Room'  # Where the player/Kobe starts

    item_list = []  # Player's/Kobe's empty inventory

    move_input = ''  # Start with empty input

    player_awake = True  # Player/Kobe is awake

    # Gameplay loop. Will loop as long as player/Kobe is awake and not asleep
    while player_awake:  # While player_awake is True
        player_status(item_list, in_room)  # Update player on Kobe's status

        if in_room == 'Kitchen':  # If in the kitchen, ending function trash_can() has already
            player_awake = False  # been called, game end text printed, and loop must end. Player/Kobe is now asleep
            break  # Break out of loop

        move_input = input('What will Kobe do?:\n')  # Get player/Kobe movement or item command

        if move_input in move_commands:  # If player input is valid and in move_commands, call the movement function
            in_room = movement(move_input, in_room)  # Update player's/Kobe's current room
        elif move_input == 'go to sleep':  # This will end the loop and the game. Puts player/Kobe to sleep
            player_awake = False  # Player/Kobe is not awake
        elif move_input in item_commands:  # If player input is valid and in item_commands, call get_item function
            item_list.append(get_item(move_input, in_room, item_list))  # Append returned new item to item_list
            if 'invalid' in item_list:  # If the player entered an item not in room or already in item_list
                item_list.remove('invalid')  # Invalid was returned so must remove invalid from item_list
        else:  # If not a valid input, print try again and re-loop
            print("Kobe doesn't know that action! Try again!")

    # Print end program text to let user know program/game is terminated
    print('Thank you for playing my game about my dog! Based on a true story.')
    print('{}'.format('=' * 25))  # One last line of separator text
