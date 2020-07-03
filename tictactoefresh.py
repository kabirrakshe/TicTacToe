# this is my program

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
winlose = {'Player':0,'CPU':0,'No One':0}
moves = []
level = []
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
    thing = 0
    column = (board[0][thing],board[1][thing],board[2][thing])
    for items in board:
        count = count +1
        if items.count(avatar) == 2 and '_' in items:
            fill = items.index('_')
            board[count][fill] = avatarcpu
            boardprinter('CPU')
            return True
    while thing < 2:
        if column.count(avatar) ==2 and '_' in column:
            fill = column.index('_')
            board[fill][thing] = avatarcpu
            boardprinter('CPU')
            return True
        thing = thing+1
        column = (board[0][thing],board[1][thing],board[2][thing])

def enemyhardreference():
    diagonala = (board[0][0],board[1][1],board[2][2])
    diagonalb = (board[2][0],board[1][1],board[0][2])
    if diagonala.count(avatar) ==2 and '_' in diagonala:
        fill = diagonala.index('_')
        if fill == 0: diag = 0
        elif fill == 1: diag = 1
        else: diag = 2
        board[diag][fill] = avatarcpu
        boardprinter('CPU')
        return True
    elif diagonalb.count(avatar) ==2 and '_' in diagonalb:
        fill = diagonalb.index('_')
        if fill == 0: diag = 2
        elif fill == 1: diag = 1
        else: diag = 0
        board[diag][fill] = avatarcpu
        boardprinter('CPU')
        return True
###----------------------------------------------------------------------------------
def Easy_mode():#Activated if user input(starting) == 'easy' Chooses random only
    while True:
        x = choice([0,1,2])
        y = choice([0,1,2])
        if board[y][x] == '_':
            board[y][x] = avatarcpu
            boardprinter('CPU')
            return
        else: continue
###-----------------------------------------------------------------------------
def Mid_mode(diff):
    count = -1
    thing = 0
    column = (board[0][thing],board[1][thing],board[2][thing])
    for items in board:
        count = count + 1
        if items.count(avatarcpu) == 2 and '_' in items:
            fill = items.index('_')
            board[count][fill] = avatarcpu
            boardprinter('CPU')
            return True
    while thing < 2:
        if column.count(avatarcpu) == 2 and '_' in column:
            fill = column.index('_')
            board[fill][thing] = avatarcpu
            boardprinter('CPU')
            return True
        thing = thing+1
        column = (board[0][thing],board[1][thing],board[2][thing])
        if enemyreference() == True: return True
        else:
            if diff == 'hard': return
            else:
                Easy_mode()
                return
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
    if Mid_mode('hard') == True: return
    else:
        if enemyhardreference() == True: return
        else:
            if enemyreference() == True: return
            else: Easy_mode()
###------------------------------------------------------------------------------
def gameover(): #Function to decide when game is finished
    thing = 0
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return True
    while thing <= 2:
        acolumn = (board[0][thing],board[1][thing],board[2][thing])
        if acolumn[0] == acolumn[1] == acolumn[2] != '_':
            return True
        thing = thing + 1
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != '_':
        return True
    rowa = board[0]
    rowb = board[1]
    rowc = board[2]
    if rowa.count('_')== 0 and rowb.count('_') == 0 and rowc.count('_') == 0:
        return True
    return False
###-----------------------------------------------------------------------------

def Initiate():#Initiation Sequence, Apex Function
    while True:
        global winner
        global winlose
        global starting
        global moves
        global level
        global board
        Introduction()
        for value in range(5):
            Player1()
            if gameover() == True:
                winner = 'Player'
                break
            if starting == 'easy':
                diff = 1
                Easy_mode()
            elif starting == 'medium':
                diff = 2
                Mid_mode('')
            elif starting == 'hard':
                diff = 4
                Hard_mode()
            if gameover() == True:
                winner = 'CPU'
                break
        winlose[winner] = winlose[winner] + 1
        print('The winner of this match is......\n')
        time.sleep(3)
        print(winner+'!!!!!!')
        print('Your total wins, losses, and ties: ',winlose)
        moves.append(10/value) # save the rating
        level.append(diff)
        final_question = input('Would you like to play again? ').lower()
        if final_question.strip() == 'no':# ranking calculation
            suma = 0
            sumb = 0
            for overall in moves:
                suma = suma + overall
            for average in level:
                sumb = sumb+average
            sumb = sumb / len(level)
            suma = suma + sumb - winlose['CPU']
            denominator = winlose['Player']+winlose['CPU']
            print('Player Ranking Based on Skill: ',suma,' out of ',denominator*10)
            quit()
        else:
            board = [['_','_','_'],['_','_','_'],['_','_','_']]
            starting = input('Choose a setting: Easy, Medium, Hard: ').lower()
            avatar = input('Choose a character: X or O: ').upper()
            if avatar == 'X': avatarcpu = 'O'
            else: avatarcpu = 'X'
            winner = 'No One'
            continue
#-------------------------------------------------------------------------------
Initiate() ##firsttime
