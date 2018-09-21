#https://github.com/Znorlaxing2Day/Snorriforri-tari

#1. Which implementation was easier?
#The second one would be simpler if I would have made the program with functions in mind 
# however changing a already in place program into functions was more difficult in this 
# particular case as I am early in my training and not really trained in functions.
#2. Which implementation is more readable and why?
#Second one is more readable as instead of reading the entire code again you know what the 
# function does and can simply know that that particular function changes Celsius to Fahrenheit for example
#3. Which problems in the first implementations were you able to solve with the latter implementation?
#There were two problems I was able to solve using the second implementation. One of which was 
# writing the entire text of instructions for the user and the second one was the math involved in each 
# step the user takes in the tilemaze.


def step_update(pos, dir):
    """the function takes updates the position according to a selected direction
    parameter pos: Current position
    parameter dir: Selected direction"""
    if dir == 'N':
        pos += 0.1
    elif dir == 'S':
        pos -= 0.1
    elif dir == 'E':
        pos += 1.0
    elif dir == 'W':
        pos -= 1.0
    return round(pos,2)

def print_options(pos):
    """Input a position that tells you the direction/s you can choose """
    travelstr = "You can travel: "
    if 'N' in pos:
        travelstr += '(N)orth or '
    if 'E' in pos:
        travelstr += '(E)ast or '
    if 'S' in pos:
        travelstr += '(S)outh or '
    if 'W' in pos:
        travelstr += '(W)est or '
    print(travelstr[:-4] + ".")
    
pos_11 = "N"
pos_12 = "N S E"
pos_13 = "E S"
pos_21 = "N"
pos_22 = "W S"
pos_23 = "E W"
pos_31 = "Victory!"
pos_32 = "N S"
pos_33 = "W S"

position = 1.1

inv_dir = "Not a valid direction!"

while position != 3.1:
    if position == 1.1:
        print_options(pos_11)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_11:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 1.2:
        print_options(pos_12)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_12:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 1.3:
        print_options(pos_13)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_13:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 2.1:
        print_options(pos_21)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_21:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 2.2:
        print_options(pos_22)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_22:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 2.3:
        print_options(pos_23)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_23:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 3.2:
        print_options(pos_32)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_32:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
    elif position == 3.3:
        print_options(pos_33)
        while True:
            direction = input("Direction: ").capitalize()
            if direction in pos_33:
                position = step_update(position, direction)
                break
            else:
                print(inv_dir)
print("Victory!")