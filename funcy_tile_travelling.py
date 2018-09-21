position = 1.1

inv_dir = "Not a valid direction!"

in_n = "N"
in_e = "E"
in_s = "S"
in_w = "W"

one_one = "You can travel: (N)orth"
one_two = "You can travel: (N)orth or (E)ast or (S)outh"
one_three = "You can travel: (E)ast or (S)outh"
two_one = "You can travel: (N)orth"
two_two = "You can travel: (S)outh or (W)est"
two_three = "You can travel: (E)ast or (W)est"
three_one = "Victory!"
three_two = "You can travel: (N)orth or (S)outh"
three_three = "You can travel: (S)outh or (W)est"

while position != 3.1:
    if position == 1.1:
        print(one_one)
        direction = input("Direction: ").capitalize()
        if direction == in_n:
            position += 0.1
        else:
            print(inv_dir)
    elif position == 1.2:
        print(one_two)
        direction = input("Direction: ").capitalize()
        if direction == in_n:
            position += 0.1
        elif direction == in_e:
            position += 1
        elif direction == in_s:
            position -= 0.1
        else:
            print(inv_dir)
    elif position == 1.3:
        print(one_three)
        direction = input("Direction: ").capitalize()
        if direction == in_e:
            position += 1
        elif direction == in_s:
            position -= 0.1
        else:
            print(inv_dir)
    elif position == 2.1:
        print(two_one)
        direction = input("Direction: ").capitalize()
        if direction == in_n:
            position += 0.1
        else:
            print(inv_dir)
    elif position == 2.2:
        print(two_two)
        direction = input("Direction: ").capitalize()
        if direction == in_w:
            position -= 1
        elif direction == in_s:
            position -= 0.1
        else:
            print(inv_dir)
    elif position == 2.3:
        print(two_three)
        direction = input("Direction: ").capitalize()
        if direction == in_e:
            position += 1
        elif direction == in_w:
            position -= 1
        else:
            print(inv_dir)
    elif position == 3.2:
        print(three_two)
        direction = input("Direction: ").capitalize()
        if direction == in_n:
            position += 0.1
        elif direction == in_s:
            position -= 0.1
        else:
            print(inv_dir)
    elif position == 3.3:
        print(three_three)
        direction = input("Direction: ").capitalize()
        if direction == in_w:
            position -= 1
        elif direction == in_s:
            position -= 0.1
        else:
            print(inv_dir)
    position = round(position,2)
else:
    print(three_one)
  