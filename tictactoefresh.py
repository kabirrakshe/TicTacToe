from random import choice #Probability Library
import time
for x in range(0,5):
    print('Initializing Game......')
    time.sleep(1)
board = [['_','_','_'],['_','_','_'],['_','_','_']] #Mutable base board
starting = input('Choose a setting: Easy, Medium, Hard: ').lower()
avatar = input('Choose a character: X or O: ').upper()
if avatar == 'X': avatarcpu = 'O'
else: avatarcpu = 'X'
winner = 'No One'
winlose = {}
def Introduction():
    print('READY!!!')
    time.sleep(1)
    print('SET!!!')
    time.sleep(1)
    print('GO!!!')
    time.sleep(0.5)
###-----------------------------------------------------------------------------
def boardprinter(person):
    print('\n')
    if person == 'CPU':
        time.sleep(2)
    for n in board:
        print(n[0] + '|' + n[1] + '|' + n[2])
###-----------------------------------------------------------------------------
def Player1():# Certain coordinates correspond to indices in list
    while True:
        coordinate_a = int(input(' Player 1 Move X Coordinate: ')) - 1
        coordinate_b = int(input(' Player 1 Move Y Coordinate: ')) - 1
        if board[coordinate_b][coordinate_a] == '_':
            board[coordinate_b][coordinate_a] = avatar
            break
        else: continue
    boardprinter('')
    return
###----------------------------------------------------------------------------
def enemyreference():
    count = -1
    adjacent = None
    primary = -1
    thing = 0
    column = board[:][thing]
    count = -1
    for items in board:
        count = count +1
        if items.count(avatar) == 2 and '_' in items:
            fill = items.index('_')
            board[count][fill] = avatarcpu
            boardprinter('CPU')
            print('hi')
            return
    while thing < 2:
        if column.count(avatar) ==2 and '_' in column:
            fill = column.index('_')
            board[fill][thing] = avatarcpu
            boardprinter('CPU')
            return
        thing = thing+1
        column = board[:][thing]

def enemyhardreference():
    diagonala = (board[0][0],board[1][1],board[2][2])
    diagonalb = (board[2][0],board[1][1],board[0][2])
    if diagonala.count(avatar) == 2 and '_' in diagonala:
        fill = diagonala.index('_')
        if fill == 0: diag = 0
        elif fill == 1: diag = 1
        else: diag = 2
        board[fill][diag] = avatarcpu
        boardprinter('CPU')
        return
    elif diagonalb.count(avatar)== 2 and '_' in diagonalb:
        fill = diagonalb.index('_')
        if fill == 0: diag = 2
        elif fill == 1: diag = 1
        else: diag = 0
        board[fill][diag] = avatarcpu
        boardprinter('CPU')
        return
###----------------------------------------------------------------------------------
def Easy_mode():#Activated if user input(starting) == 'easy' Chooses random only
    while True:
        x = choice([0,1,2])
        y = choice([0,1,2])
        if board[y][x] == '_':
            board[y][x] = avatarcpu
            boardprinter('CPU')
            return
        else:
            continue
###-----------------------------------------------------------------------------
def Mid_mode():
    count = -1
    adjacent = None
    primary = -1
    thing = 0
    column = board[:][thing]
    for items in board:
        count = count + 1
        if items.count(avatarcpu) == 2and '_' in items:
            fill = items.index('_')
            board[count][fill] = avatarcpu
            boardprinter('CPU')
            return
    while thing < 2:
        if column.count(avatarcpu) == 2 and '_' in column:
            fill = column.index('_')
            board[fill][thing] = avatarcpu
            boardprinter('CPU')
            return
        thing = thing+1
        column = board[:][thing]
        enemyreference()
###-----------------------------------------------------------------------------
def Hard_mode():
    diagonala = (board[0][0],board[1][1],board[2][2])
    diagonalb = (board[2][0],board[1][1],board[0][2])
    if diagonala.count(avatarcpu) ==2 and '_' in diagonala:
        fill = diagonala.index('_')
        if fill == 0: diag = 0
        elif fill == 1: diag = 1
        else: diag = 2
        board[fill][diag] = avatarcpu
        boardprinter('CPU')
        return
    elif diagonalb.count(avatarcpu) ==2 and '_' in diagonalb:
        fill = diagonalb.index('_')
        if fill == 0: diag = 2
        elif fill == 1: diag = 1
        else: diag = 0
        board[fill][diag] = avatarcpu
        boardprinter('CPU')
        return
    Mid_mode()
    enemyhardreference()
###------------------------------------------------------------------------------
def gameover(): #Function to decide when game is finished
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return True
    acolumn = board[:][0]
    bcolumn = board[:][1]
    ccolumn = board[:][2]
    for node in [acolumn,bcolumn,ccolumn]:
        if node[0] == node[1] == node[2] != '_':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != '_':
        return True
    return False
    if board[0 and 1 and 2].count('_') == 0:
        return True
    return False
###-----------------------------------------------------------------------------

def Initiate():#Initiation Sequence, Apex Function
    global board
    global winner
    global winlose
    global starting
    Introduction()
    for value in range(5):
        Player1()
        if gameover() == True:
            if board[0 and 1 and 2].count('_')>0:
                winner = 'Player'
            break
        if starting == 'easy': Easy_mode()
        elif starting == 'medium': Mid_mode()
        elif starting == 'hard': Hard_mode()
        if gameover() == True:
            winner = 'CPU'
            break
    winlose[winner] = winlose.get(winner,0) + 1
    print('The winner of this match is......\n')
    print(winner+'!!!!!!')
    print(winlose)
    final_question = input('Would you like to play again? ').lower()
    if final_question.strip() == 'no':
        # print('Based on your overall performance and the difficulty you chose, the computer gives you a rating of',rating,'out of 100')
        quit()
    else:
        board = [['_','_','_'],['_','_','_'],['_','_','_']] #Mutable base board
        starting = input('Choose a setting: Easy, Medium, Hard: ').lower()
        avatar = input('Choose a character: X or O: ').upper()
        if avatar == 'X': avatarcpu = 'O'
        else: avatarcpu = 'X'
        winner = 'No One'
        Initiate()
#-------------------------------------------------------------------------------
Initiate() ##firsttime
