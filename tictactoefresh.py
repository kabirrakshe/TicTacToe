from random import choice #Probability Library

board = [['_','_','_'],['_','_','_'],['_','_','_']] #Mutable base board
starting = input('Choose a setting: Easy, Medium, Hard: ').lower()
avatar = input('Choose a character: X or O: ').upper()

if avatar == 'X': avatarcpu = 'O'
else: avatarcpu = 'X'

taken_player = []
taken_cpu = []
taken_values = taken_player + taken_cpu

###---------------------------------------------------------------------------
def Player1():# Certain coordinates correspond to indices in list
    done = False
    while done == False:
        coordinate_a = int(input(' Player 1 Move X Coordinate: ')) - 1
        coordinate_b = int(input(' Player 1 Move Y Coordinate: ')) - 1
        if int(str(coordinate_a) + str(coordinate_b)) not in taken_values:
            board[coordinate_b][coordinate_a] = avatar
            done = True
        else: continue
    for n in board:
        print(n[0]+'|' + n[1] + '|' + n[2])



###----------------------------------------------------------------------------



def Easy_mode():#Uses user input (starting) to choose difficulty level
    done = False
    while done == False:
        x = choice([0,1,2])
        y = choice([0,1,2])
        if int(str(x)+str(y)) in taken_values:
            continue
        else:
            board[y][x] = avatarcpu
            done = True
            for n in board:
                print(n[0]+'|'+n[1]+'|'+n[2])

def Mid_mode():
    done = False
    a = False
    for items in board:
        if avatar in items:
            for item in items:
                if item == avatarcpu:
                    a = False
                    break
                if item == avatar:
                    



    while done == False:
        x = choice([0,1,2])
        y = choice([0,1,2])
        if int(str(x)+str(y)) in taken_values:
            continue
        else:
            board[y][x] = avatarcpu
            done = True
            for n in board:
                print(n[0]+'|'+n[1]+'|'+n[2])











###----------------------------------------------------------------------------
def checking(): ## Checking What values are taken overall
    countprime = -1
    for value in board:
        count = -1
        countprime = countprime+1
        for index in value:
            count = count + 1
            if index == avatar:
                taken_player.append(int(str(count) + str(countprime)))
            elif index == avatarcpu:
                taken_cpu.append(int(str(count) + str(countprime)))
###----------------------------------------------------------------------------
