import math
def direction_(direction_inp,tile):
    if direction_inp=="e":
        tile=tile+10
    if direction_inp=="w":
        tile=tile-10
    if direction_inp=="n":
        tile=tile+1
    if direction_inp=="s":
        tile=tile-1
    return tile
borderW="0"
borderN="0"
borderE="0"
borderS="0"
def border_e(tile):
    borderE="0"
    if tile==11:
        borderE="1"
    if tile==22:
        borderE="1"
    if tile==21:
        borderE="1"
    if tile==33 or tile==32:
        borderE="1"
    return borderE
def border_n(tile):
    borderN="0"
    if tile==22:
        borderN="1"
    if tile==13 or tile==23 or tile==33:
        borderN="1"
    return borderN
def border_w(tile):
    borderW="0"
    if tile==21:
        borderW="1"
    if tile==32:
        borderW="1"
    if tile==13 or tile==12 or tile==11:
        borderW="1"
    return borderW
def border_s(tile):
    borderS="0"
    if tile==23:
        borderS="1"
    if tile==11 or tile==21:
        borderS="1"
    return borderS
tile=11
while tile!=31:
    out=""
    count=0
    borderS=border_s(tile)
    borderN=border_n(tile)
    borderW=border_w(tile)
    borderE=border_e(tile)
    if borderN=="0":
        out =out+"(N)orth"
        count+=1
    if borderE=="0":
        if count>0:
            out=out+" or "
        out=out+"(E)ast"
        count+=1
    if borderS=="0":
        if count>0:
            out=out+" or "
        out=out+"(S)outh"
        count+=1
    if borderW=="0":
        if count>0:
            out=out+" or "
        out=out+"(W)est"
        count+=1

    print("You can travel: "+out+".")
    direction_inp=input("Direction: ")
    direction=str.lower(direction_inp)
    if direction=="w"and borderW=="1":
        print("Not a valid direction!")
    elif direction=="s"and borderS=="1":
        print("Not a valid direction!")
    elif direction=="n"and borderN=="1":
        print("Not a valid direction!")
    elif direction=="e"and borderE=="1":
        print("Not a valid direction!")
    else:
        tile=direction_(direction,tile)

print("Victory!")



#Tile traveller
"""tiles = ["ynnn11", "yyyn12", "nyyn13", "ynnn21", "nnyy22", "nyny23", "ynnn31", "ynyn32", "nnyy33"]
current_tile = tiles[0]
def tile_mover(tile, direction):
    current_xvalue = int(tile[4])
    current_yvalue = int(tile[5])
    change_xvalue = 0
    change_yvalue = 0
    if direction == "N":
        change_yvalue = 1
    if direction == "E":
        change_xvalue = 1
    if direction == "S":
        change_yvalue = -1
    if direction == "W":
        change_xvalue = -1
    updated_xvalue = current_xvalue + change_xvalue
    updated_yvalue = current_yvalue + change_yvalue
    for i in range(9):
        if tiles[i][4] == str(updated_xvalue) and tiles[i][5] == str(updated_yvalue):
            return tiles[i]
def tile_checker(tile, direction):
    new_tile = ''
    if direction == "N" and tile[0] == "y":
        return True
    elif direction == "E" and tile[1] == "y":
        return True
    elif direction == "S" and tile[2] == "y":
        return True
    elif direction == "W" and tile[3] == "y":
        return True
    else:
        print('Not a valid direction!')
        return False
while current_tile[4] != "3" or current_tile[5] != "1":
    first_direction = True
    you_can_travel = "You can travel: "
    if current_tile[0] == 'y':
        you_can_travel += '(N)orth'
        first_direction = False
    if current_tile[1] == 'y':
        if first_direction:
            you_can_travel += '(E)ast'
            first_direction = False
        else:
            you_can_travel += ' or (E)ast'
    if current_tile[2] == 'y':
        if first_direction:
            you_can_travel += '(S)outh'
            first_direction = False
        else:
            you_can_travel += ' or (S)outh'
    if current_tile[3] == 'y':
        if first_direction:
            you_can_travel += '(W)est'
            first_direction = False
        else:
            you_can_travel += ' or (W)est'
    print('{}.'.format(you_can_travel))
    direction = input("Direction: ").upper()
    if tile_checker(current_tile, direction):
        current_tile = tile_mover(current_tile, direction)
print("Victory!")"""