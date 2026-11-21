import os
board=[' ' ,' ',' '],[' ',' ',' '],[' ',' ',' ']
win_pairs=(((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))
def sample():
    board=['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3']
    for i in board:
            print("\033[38;2;0;245;212m|\033[0m".join(i))
            print("\033[38;2;0;245;212m-\033[0m"*7)
def display():
    global board 
    print("\033[38;2;0;245;212m-\033[0m"*5)
    for i in board:
        print("\033[38;2;0;245;212m|\033[0m".join(i))
        print("\033[38;2;0;245;212m-\033[0m"*5)
def mark(pos,player):
    global board
    if pos[0]=='a':
        i=0
    if pos[0]=='b':
        i=1
    if pos[0]=='c':
        i=2
    j=int(pos[1])-1
    board[i][j]=player
def win():
    for (r1,c1),(r2,c2),(r3,c3) in win_pairs:
        if board[r1][c1]==board[r2][c2]==board[r3][c3]!=" ":
            return True
    return False
def instructions():
    print("\033[38;2;0;255;127mInsrtuctions to play:\n1.This is a two player game.\n2.Player 1 uses X and player 2 uses O.\n3.Player 1 gets the first turn.\033[0m")
    print("\033[38;2;0;255;127m4.The game board consists of 3 rows and 3 coloums.\n4.Enter position (eg:a1,a2,c3...) as per sample table to place your symbol.\033[0m")
    board=['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3']
    print("\033[38;2;0;245;212m-\033[0m"*7)
    for i in board:
            print("\033[38;2;0;245;212m|\033[0m".join(i))
            print("\033[38;2;0;245;212m-\033[0m"*7)
    print("\033[38;2;0;255;127m6.Players takes turn placing there symbol.\n7.You cannot choose a position that is already occupied.\033[0m")
    print("\033[38;2;0;255;127m8.The first player to get three symbols in row, coloum or diagonal wins.\n9.If all positions are filled and nobody wins,the game ends in draw.\033[0m")
    print(" ")
print("\033[38;2;255;176;0m===TIC TAC TOE===\033[0m")
print(" ")
instructions()
print("\033[38;2;255;176;0m Type -h to display instructions between the game\033[0m")
print(" ")
print("\033[38;2;0;255;127mPress ENTER to play\033[0m")
input()
os.system("cls")
display()
occupied=[]
i=1
while True:
    if i%2!=0:
        player='\033[38;2;255;107;53mX\033[0m'
    else:
        player='\033[38;2;255;176;0mO\033[0m'
    pos=input(f"It's player {player} turn ")
    os.system("cls")
    if pos=="-h":
        instructions()
        display()
        continue
    elif pos in occupied:
        print("\033[38;2;255;65;65mOOPS! The column is already occupied\033[0m ")
        display()
        continue
    elif pos not in {'a1','a2','a3','b1','b2','b3','c1','c2','c3'}:
        print("\033[38;2;255;65;65mInvalid choice,Try again!\033[0m")
        display()
        continue
    occupied.append(pos)
    mark(pos,player)
    display()
    if win():
        print("\033[38;2;255;85;85mPlayer\033[0m",player ,"\033[38;2;255;85;85mwon!\033[0m")
        exit()
    if i==9:
        print(f"\033[38;2;255;176;0mOh!It's a Draw\033[0m")
        exit()
    i=i+1

    