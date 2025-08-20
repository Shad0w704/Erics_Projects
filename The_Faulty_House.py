# This is a game where the user has to react accordingly to issues in the house. 20 successes to win!

from random import randint
from threading import Event, Thread
from os import _exit

current_timer = None
stop_event = Event()

def countdown_timer():
    if stop_event.wait(2):
        return
    print("\nYou took too long to respond!")
    print("YOU LOSE!")
    _exit(0)

# This adds a fault to the screen
def random_house_fault():
    global random_num, current_timer
    
    stop_event.set()
    if current_timer and current_timer.is_alive():
        current_timer.join()
    stop_event.clear()
    
    # Generating a new fault
    random_num = randint(1, 3)
    if random_num == 1:
        print("The roof is leaking water!\n")
    elif random_num == 2:
        print("There are mice in the walls!\n")
    else:
        print("Robbers at the door!\n")

    
    current_timer = Thread(target=countdown_timer)
    current_timer.daemon = True
    current_timer.start()

successes = 0

start = input("Quickly press the correct number before time runs out. Get 21 successes in a row to win!\nEnter any key to start: ")
while True:
    random_house_fault()
    
    try:
        action = input("Input a number:  1. Patch Roof | 2. Lay mouse traps | 3. Scare the robbers\n")
    except EOFError:
        _exit(1)

    stop_event.set()
    
    if action == "1":
        if random_num == 1:
            print("Roof patched successfully!\n")
        else:
            print("YOU LOSE!")
            break
    elif action == "2":
        if random_num == 2:
            print("Mice have left!\n")
        else:
            print("YOU LOSE!")
            break
    elif action == "3":
        if random_num == 3:
            print("Robbers flee!\n")
        else:
            print("YOU LOSE!")
            break
    else:
        print("Input just a number!\nYOU LOSE!")
        break
    successes += 1
    if successes == 21:
        print("21 Successes in a row. YOU WIN!")
        break

