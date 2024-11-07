ascii_art = """
                                                                                                                                                                                         
         ,--.                                                                                                                                                                            
       ,--.'|               ___      ,---,                                      .--.--.               ,---,                 ,--,         ,-.                                        ,-.  
   ,--,:  : |             ,--.'|_  ,--.' |                                     /  /    '.           ,--.' |               ,--.'|     ,--/ /|                 ,--,               ,--/ /|  
,`--.'`|  ' :             |  | :,' |  |  :                      ,---,         |  :  /`. /           |  |  :               |  | :   ,--. :/ |          .---.,--.'|         .--.,--. :/ |  
|   :  :  | |             :  : ' : :  :  :                  ,-+-. /  |        ;  |  |--`            :  :  :               :  : '   :  : ' /          /. ./||  |,        .--,`|:  : ' /   
:   |   \ | :  ,--.--.  .;__,'  /  :  |  |,--.  ,--.--.    ,--.'|'   |        |  :  ;_       ,---.  :  |  |,--.  ,--.--.  |  ' |   |  '  /        .-'-. ' |`--'_        |  |. |  '  /    
|   : '  '; | /       \ |  |   |   |  :  '   | /       \  |   |  ,"' |         \  \    `.   /     \ |  :  '   | /       \ '  | |   '  |  :       /___/ \: |,' ,'|       '--`_ '  |  :    
'   ' ;.    ;.--.  .-. |:__,'| :   |  |   /' :.--.  .-. | |   | /  | |          `----.   \ /    / ' |  |   /' :.--.  .-. ||  | :   |  |   \   .-'.. '   ' .'  | |       ,--,'||  |   \   
|   | | \   | \__\/: . .  '  : |__ '  :  | | | \__\/: . . |   | |  | |          __ \  \  |.    ' /  '  :  | | | \__\/: . .'  : |__ '  : |. \ /___/ \:     '|  | :       |  | ''  : |. \  
'   : |  ; .' ," .--.; |  |  | '.'||  |  ' | : ," .--.; | |   | |  |/          /  /`--'  /'   ; :__ |  |  ' | : ," .--.; ||  | '.'||  | ' \ \.   \  ' .\   '  : |__     :  | ||  | ' \ \ 
|   | '`--'  /  /  ,.  |  ;  :    ;|  |  :_:,'/  /  ,.  | |   | |--'          '--'.     / '   | '.'||  :  :_:,'/  /  ,.  |;  :    ;'  : |--'  \   \   ' \ ||  | '.'|  __|  : ''  : |--'  
'   : |     ;  :   .'   \ |  ,   / |  | ,'   ;  :   .'   \|   |/                `--'---'  |   :    :|  | ,'   ;  :   .'   \  ,   / ;  |,'      \   \  |--" ;  :    ;.'__/\_: |;  |,'     
;   |.'     |  ,     .-./  ---`-'  `--''     |  ,     .-./'---'                            \   \  / `--''     |  ,     .-./---`-'  '--'         \   \ |    |  ,   / |   :    :'--'       
'---'        `--`---'                         `--`---'                                      `----'             `--`---'                          '---"      ---`-'   \   \  /            
                                                                                                                                                                      `--`-'   
"""

print(ascii_art)
import random

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print("\n---------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def make_move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    computer = "O"
    game_over = False
    
    while not game_over:
        print_board(board)
        if player == "X":
            while True:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if make_move(board, player, row, col):
                    break
                else:
                    print("Invalid move! Try again.")
        else:
            empty_cells = get_empty_cells(board)
            cell = random.choice(empty_cells)
            make_move(board, player, cell[0], cell[1])
            print(f"Computer played at row {cell[0]} column {cell[1]}")
            
        if check_win(board, player):
            print_board(board)
            print(f"{player} wins!")
            game_over = True
        elif len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            game_over = True
        
        player = "O" if player == "X" else "X"

play_game()

