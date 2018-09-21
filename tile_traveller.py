#https://github.com/Znorlaxing2Day/Snorriforri-tari

#Algorithm for solving the game:
#Við búum til breytur sem halda utan um texta um allar áttir til að hreyfast í.
#Svo þarf að búa til allt mögulegt input fyrir notandann til að ferðast sem má vera stór og lítill stafur.
#Það leysti ég með því að capitalize-a það sem er skrifað og tékkað hvort að það sé það sama og stórt N, E, S og W.
#Svo er if setning sem skoðar í hvaða reit notandi er staddur og svo bíður þér að velja átt.
#Svo á meðan (while) notandi er ekki í reit 3.1 byrja if setningar sem prenta út valmöguleika um hvaða áttir eru í boði og bætir við
#+1 ef notandi ferðast upp, -1 ef notandi ferðast niður, +0,1 ef notandi ferðast til hægri og -0,1 ef notandi ferðast til vinstri.
#Ef valið er átt sem er ekki í boði prentast "invalid direction".
#Svo þarf að round-a töluna sem bætist við því annars verður of mikið af aukastöfum (1.3 != 1.3000000000)
#Þegar reiturinn verður 3.1 eða vinningsstaður þá prentast "Victory!" og forrit hættir
position = 1.1

inv_dir = "Not a valid direction!"

in_n = "N"
in_e = "E"
in_s = "S"
in_w = "W"

travelstr = "You can travel: "
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"

one_one = travelstr + N + "."
one_two = travelstr + N + " or " + E + " or " + S + "."
one_three = travelstr + E + " or " + S + "."
two_one = travelstr + N + "."
two_two = travelstr + S + " or " + W + "."
two_three = travelstr + E + " or " + W + "."
three_one = "Victory!"
three_two = travelstr + N + " or " + S + "."
three_three = travelstr + S + " or " + W + "."

while position != 3.1:
    if position == 1.1:
        print(one_one)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_n:
                position += 0.1
                break
            else:
                print(inv_dir)
    elif position == 1.2:
        print(one_two)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_n:
                position += 0.1
                break
            elif direction == in_e:
                position += 1
                break
            elif direction == in_s:
                position -= 0.1
                break
            else:
                print(inv_dir)
    elif position == 1.3:
        print(one_three)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_e:
                position += 1
                break
            elif direction == in_s:
                position -= 0.1
                break
            else:
                print(inv_dir)
    elif position == 2.1:
        print(two_one)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_n:
                position += 0.1
                break
            else:
                print(inv_dir)
    elif position == 2.2:
        print(two_two)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_w:
                position -= 1
                break
            elif direction == in_s:
                position -= 0.1
                break
            else:
                print(inv_dir)
    elif position == 2.3:
        print(two_three)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_e:
                position += 1
                break
            elif direction == in_w:
                position -= 1
                break
            else:
                print(inv_dir)
    elif position == 3.2:
        print(three_two)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_n:
                position += 0.1
                break
            elif direction == in_s:
                position -= 0.1
                break
            else:
                print(inv_dir)
    elif position == 3.3:
        print(three_three)
        while True:
            direction = input("Direction: ").capitalize()
            if direction == in_w:
                position -= 1
                break
            elif direction == in_s:
                position -= 0.1
                break
            else:
                print(inv_dir)
    position = round(position,2)
else:
    print(three_one)