# To Do application 
def greet(name):
    print("Welcome! " + name)
greet('isabel')


def game_player(player):
    try:
        game_mode = int(input("pick your mode "
                              "(0 - Easy | 1 - Soldier | 2 - Legendary)"))
        result = 100 / game_mode
        
    except ZeroDivisionError:
        print("Ready!")
    except ValueError:
        print("invalid option try again!")
    else:
        print(f"you win!")
    finally:
        print("game over!")

characters_list = ['Tracer', 'Dva', 'Widowmaker', 'Reaper']

#main menu 
user_input = 0 
while user_input != 5:
    print('''
    \nMain menu
    1. Pick a character 
    2. View Character list 
    3. Add to you character list 
    4. Delete a charcter 
    5. Exit
''')
    try:
        user_input = int(input("please choose one (1 or 2 or 3 or 4 or 5):"))
    except ValueError:
        print("oops, please choose an option")
    
    if user_input == 1:
        try:
            player_name = input("enter your player choice".lower())
    
            if not player_name.strip():
                raise ValueError("must make a choice")
        except ValueError as e:
            print(e)
        else:
            game_player(player_name)
    elif user_input == 2:
        print("Here is your list:", characters_list)
        
        
    elif user_input == 3:
        
        while True:
            character_add = input("Enter a new character (or type 'done' to finish)")
            if character_add.lower() == "done":
                break
        
            characters_list.append(character_add)
            
        print("Your new list:", characters_list) 
        #
    elif user_input == 4:
        
        def delete_character():
            print("current list:", characters_list)
            character_to_remove = input("Enter the player to remove: ").capitalize()
            
            try:
                characters_list.remove(character_to_remove)
                print("player eliminated")
            except ValueError:
                print("player not found")
            except NameError:
                print("Invalid player")
            
            print("Updated list:", characters_list)   
        
        delete_character()
    elif user_input == 5:
            print("see you later!")





