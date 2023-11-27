board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Know if game is still going on by setting it to True
game_on = True

# Initialize our current player to be X
current_player = "X"

#Function to display our game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1|2|3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4|5|6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7|8|9")
display_board()

#miao miao
#first move
user_choice = int(input("Select a box (1-9): \n"))

#check win based on last move
def check_win():
    if board[0] == board[1] == board[2] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[3] == board[4] == board[5] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[6] == board[7] == board[8] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[0] == board[3] == board[6] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[1] == board[4] == board[7] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[2] == board[5] == board[8] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[0] == board[4] == board[8] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[2] == board[4] == board[6] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[0] == board[1] == board[2] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[0] == board[1] == board[2] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    elif board[0] == board[1] == board[2] != "-":
        print("|" + current_player + "| " + "is the winner!")
        display_board()
        return False
    else:
        return True

while game_on:
    #this code runs after the player enterted a number and the box is empty
    if board[user_choice - 1] == "-":
        board[user_choice - 1] = current_player
        if not check_win():
            break
        display_board()
        if "-" not in board:
            print("It's a tie!")
            break
        user_choice = int(input("Select a box (1-9): \n"))
        #need fix
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    #this code runs when the box is already taken
    else:
        print("This box is already taken!")
        display_board()
        user_choice = int(input("Select a box (1-9): \n"))
