def player_input():
###Determines which player is X and which player is O###
    start=input('Do you want to be X or O?')
    global player_1
    global player_2
    player_1=start 
    if start=='X':
        player_2='O'
    elif start=='O':
        player_2='X'
    else:
        print('Try inputting your preference again')
        player_input()
        
turn_det=0
mylist=[1,2,3,4,5,6,7,8,9]
active=''

def disp_board():
    board=(f' {mylist[0]} | {mylist[1]} | {mylist[2]} '
           f'\n--------\n {mylist[3]} | {mylist[4]} | {mylist[5]} '
           f'\n--------\n {mylist[6]} | {mylist[7]} | {mylist[8]} ')
    print(board)
    
def winning_condition():
    ###Establishes a tic-tac-toe###
    for z in range(0,9):
        if mylist[0]==mylist[4]==mylist[8] or mylist[2]==mylist[4]==mylist[6]:
            return False 
        elif mylist[z]==mylist[z+1]==mylist[z+2]:
            return False
        elif mylist[z]==mylist[z+3]==mylist[z+6]:
            return False
        else:
            return True 
        
def turns():
    for y in range(0,10):
        if winning_condition()==False:
            break
        elif y==10:
            print('The game is a tie!')
            ###Signals that all 9 turns have been played###
        else:
            turnswitch()
            replacement()

def turnswitch():
    global turn_det
    global active
    if turn_det%2==0:
        active=player_1
        turn_det+=1
    elif turn_det%2!=0:
        active=player_2
        turn_det+=1
        ###Allows turns to switch between X and O### 

def replacement():
    turn=int(input('Choose a location'))
    for x in mylist:
        if x==turn:
            mylist[x-1]=active
            ###Replaces number in position list with player's set letter ###
            disp_board()
            winning_condition()
            if winning_condition()==False:
                print('Winner!')
                break
            break
        elif x==9:
            print('Sorry, there is an error.  Try again')
            replacement()
            ###Input was not a valid position, or position was already filled on another turn###
        else:
            pass

    
player_input()
disp_board()
turns()