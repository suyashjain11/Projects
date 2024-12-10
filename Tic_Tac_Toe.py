
from IPython.display import clear_output

#Creation of Game board ui

def display_board(board):

    clear_output()
    
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('----------')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('----------')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])
    
#Take player name and marker input    

def player_input():
    marker=''
    player1_name = input("Player 1 enter your name: ")
    player2_name = input("Player 2 enter your name: ")
    while marker != 'X' and marker !='O':
        marker = input(f"{player1_name} pick a marker 'X' or 'O'").upper()
        
    player1=marker
    if player1 == 'X':
        player2 = 'O'
        print(f"{player1_name} will play with 'X' and {player2_name} will play with 'O' ")
    else:
        player2 = 'X'
        print(f"{player1_name} will play with 'O' and {player2_name} will play with 'X' ")
    return (player1_name,player2_name,player1,player2)

#Function to place marker at user provided position

def place_marker(board, marker, position):
    board[position]=marker
    return board

#Function to check if any player won the game

def win_check(board, mark):
    while True:
        #check for vertical match
        
        if board[7]==board[4]==board[1]==mark:
            #print('player won')
            return True
            break

        elif board[8]==board[5]==board[2]==mark:
            #print('player won')
            return True
            break

        elif board[9]==board[6]==board[3]==mark:
            #print('player won')
            return True
            break

        #checks for horizontal match
        
        elif board[1]==board[2]==board[3]==mark:
            #print('player won')
            return True
            break
        elif board[4]==board[5]==board[6]==mark:
            #
            return True
            break
        elif board[7]==board[8]==board[9]==mark:
            #
            return True
            break
        
        #checks for diagonal match
        
        elif board[1]==board[5]==board[9]==mark:
            #
            return True
            break
        elif board[3]==board[5]==board[7]==mark:
            #
            return True
            break
        else:
            return False
            break
        

import random

#Function to pick first chance

def choose_first(player1_name,player2_name):
    first_chance = random.randint(1,2)
    if first_chance == 1:
        return player1_name
    else:
        return player2_name
    
#Function to check if any place is empty on the board

def space_check(board, position):
    
        if board[position]=='':
            return True
        else:
            return False 
            
#Function to check if the board is already full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    

#Function to take player input to place its marker and applying variouss checks for validation

def player_choice(board,player_name):
    while True:
        
        position_str = int(input(f"{player_name} enter the position at which you want to place your marker(1-9): "))
        range_list = list(range(1,10))
        if position_str in range_list:
            position = position_str
            check = space_check(board,position)
            if check == True:
                return position
            else:
                print("Please enter empty position slot no. ")
                continue
    
        else:
            print("Please enter a valid no. between 1-9")
            continue
        

#Function to check if players want to play again

def replay():
    play = input("Do you want play again (Y/N) ? ").upper()
    if play == 'Y':
        return True
    elif play == 'N':
        return False 

#Game on...

from IPython.display import clear_output
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    #player_input()   
    player1_name,player2_name,player1_marker,player2_marker = player_input()
    chance = choose_first(player1_name,player2_name)
    if chance != player1_name:
        first_player = player2_name
        first_marker = player2_marker
        second_player = player1_name
        second_marker = player1_marker
        
    elif chance != player2_name:
        first_player = player1_name
        first_marker = player1_marker
        second_player = player2_name
        second_marker = player2_marker
        
    print(f"First chance is of {first_player}")
    print(f"Second chance is of {second_player}")        
    board = ['']*10
    board[0]='#'
    start_game = input("Are you ready to play (Y/N)?").upper()
    if start_game == 'Y':
        game_on=True
    else:
        game_on=False 
        
    while game_on:
        #Player 1 Turn
        if chance == first_player:
            display_board(board)    
            position = player_choice(board,first_player)
            board = place_marker(board, first_marker, position)
               
            if win_check(board, first_marker):      
                display_board(board)
                print(f"Congratulations {first_player}, you won")
                game_on=False
                
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    chance = second_player
            
             # Player2's turn.
        else:    
            display_board(board)
            position = player_choice(board,second_player)
            board = place_marker(board, second_marker, position)
                
            if win_check(board, second_marker):
                display_board(board)
                print(f"Congratulations {second_player}, you won")
                game_on=False

            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    chance = first_player
            

    if not replay(): 
        break

