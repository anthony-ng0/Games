'''
Algorithm
    Call the main function
        Display introduction and rules
        Use while loop to continue playing the game after games finish
            Calls the choose_color function to determine the user's color
            Calls the initialize function to set the board values to 0
            Use while loop to play the game and loop through turns
                Calls the board_display function to display the board 
                Initialize counter to alternate between turns
                Prompt for user input to choose a column, "pass", or "exit"
                if user chooses a columns:
                    Call the drop_disc function to drop a disc onto the board
                    Call the is_game_over function to determine if game is over
                if user chooses "pass":
                    The game ends, user surrenders and a message is printed
                if user chooses "exit"
                    The game exits and prints an exit message
'''

pieces = {'black':'b', 'white':'w'}
COLUMN = 7
ROW = 6

def initialize():
    '''
    Initializes a list for the board
    Uses for loop to iterate 6 times
        Creates lists to represent the rows
        Uses for loop to iterate 7 times
            Appends the value 0, 7 times in each row to represnet columns
        Then appends the rows to the board
    Returns: The list representing the board
    '''
    #Initializes the list representing the board
    board_list = []
    #Uses for loop to add 6 rows to the board and 7 values of 0 to each row.
    for i in range(6):
        row_list = []
        for i in range(7):
            row_list.append(0)
        board_list.append(row_list)
    #Returns the list of lists of 0's
    return board_list

def choose_color():
    '''
    Prompts for user input to choose a color
    While the user input is not a valid color
        Prompts again for user input
    if the user input is "white"
        the player is determined to be white, and the opponent is black
    if the user input is "black"
        the player is determined to be black, and the opponent is white
    Returns: The colors of the player and the opponent within a tuple
    '''
    #Prompts the user to choose a color
    color_str = input("Pick a color: ")
    #While the user input is not valid, print an error message and reprompt
    while color_str.lower() != "black" and color_str.lower() != "white":
        print("Wrong color; enter only 'black' or 'white', try again.")     
        color_str = input("Pick a color: ")
    #Determines the colors of the player and the opponent
    if color_str.lower() == "white":
        player_str = "white"
        opponent_str = "black"
        return player_str, opponent_str
    if color_str.lower() == "black":
        player_str = "black"
        opponent_str = "white"
        return player_str, opponent_str

def board_display(board):
    '''
    Uses the board parameter
    to create a more visually appealing list representing the game board
    Returns: Nothing
    '''
    #Visually displays the lists of lists representing the board
    print("Current board:")
    C = COLUMN
    R = ROW
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R):
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_)

def drop_disc(board, column, color): 
    '''
    Uses if statements to represent the color values as "w" or "b" to display
    on the screen
    Uses try-except format to catch IndexErrors when iterating through board
        Iterates through the board from the bottom row to top using for loop
        If the bottom row of the selected column is a value of 0:
            It will be replaced with a "w" or a "b".
            Returns: The row number
        Else:
            Returns: None
    '''
    #Creates a list of column indexes to determine validity of the column input
    column_list = [0,1,2,3,4,5,6]
    #Creates the strings that is to used in the board
    if color == "white":
        color = "w"
    if color == "black":
        color = "b"
    column = column - 1
    #Use try-except to return None if an IndexError occurs
    try:
        #If the column is within the list of column indexes
        if column in column_list:
            #Iterates through each row from the bottom to the top
            for i in range(5,-1,-1):
                #If the value of the column within the row is 0
                if board[i][column] == 0:
                    #Set that value to the color which is "w" or "b"
                    board[i][column] = color
                    #Returns the row number
                    return i + 1
            #Returns full if the for-loop finishes the iterations 
            return "full"
        #If the column is not within the list of column indexes
        if column not in column_list:
            return None
    except IndexError:
        return None
    
def check_disc(board, row, column):
    '''
    Lists all the possible winning sequences based on the current
    row/column that is selected.
    Using Try-Except format to pass through an IndexError if it occurs
    If a winning sequence is found
        Returns: True
    If the column or row is not valid:
        Returns: None
    If a value of 0 is encountered in a sequence
        Returns: False
    If a winning sequence is not found:
        Returns: None
    '''
    #Creates a list of column and row indexes
    column_list = [0,1,2,3,4,5,6]
    row_list = [0,1,2,3,4,5]
    column = column - 1
    row = row - 1
    #If the column or row is not with column_list or row_list, return None
    if column not in column_list:
        return None
    if row not in row_list:
        return None
    #If the value of the row and column in the board is 0, then return False
    if board[row][column] == 0 :
        return False
    
    #Checks for the winning sequences along the row/horizontal, it does this
    #by listing all the possible combinations of a winning sequence in a list
    #Uses try-except format to pass through IndexErrors if they occur
        #If a winning sequence exists, 4 values in a row all equal one another
            #Returns True
    try:
        if board[row][column] == board[row][column+1] == board[row][column+2]\
        == board[row][column+3]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row][column+1] == board[row][column+2]\
        == board[row][column-1]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row][column-1] == board[row][column-2]\
        == board[row][column-3]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row][column+1] == board[row][column-1]\
        == board[row][column-2]:
            return True
    except IndexError:
        pass
    
    #Checks for the winning sequences along columns/vertical 
    try:
        if board[row][column] == board[row+1][column] == board[row+2][column]\
        == board[row+3][column]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row+1][column] == board[row+2][column]\
        == board[row-1][column]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row+1][column] == board[row-1][column]\
        == board[row-2][column]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row-1][column] == board[row-2][column]\
        == board[row-3][column]:
            return True
    except IndexError:
        pass
        
    #Checks for the winning sequences along right-diagonals
    try:
        if board[row][column] == board[row-1][column+1] == \
        board[row-2][column+2] == board[row-3][column+3]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row-1][column+1] == \
        board[row-2][column+2] == board[row+1][column-1]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row-1][column+1] == \
        board[row+1][column-1] == board[row+2][column-2]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row+1][column-1] == \
        board[row+2][column-2] == board[row+3][column-3]:
            return True
    except IndexError: 
        pass

    #Checks for the winning sequences along left-diagonals
    try:
        if board[row][column] == board[row-1][column-1] == \
        board[row-2][column-2] == board[row-3][column-3]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row-1][column-1] == \
        board[row-2][column-2] == board[row+1][column+1]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row-1][column-1] == \
        board[row+1][column+1] == board[row+2][column+2]:
            return True
    except IndexError:
        pass
    try:
        if board[row][column] == board[row+1][column+1] == \
        board[row+2][column+2] == board[row+3][column+3]:
            return True
    except IndexError:
        pass
    #Returns False if none of these occur
    return False
    
def is_game_over(board):
    '''
    Uses a counter determine if the board is full
    Iterates through each value in the board using for loops
    If each value in the board is not 0, then the board is full
        Returns: "draw"
    Iterates through each value in the board using for loops
        Calls the function check_disc to determine if there is a winning
        sequence at that value
        If the check_disc returns True:
            Checks if the winning sequence contains a "w" or "b"
            If it contains a "w"
                Returns: "white"
            If it contains a "b"
                Returns: "black"
    '''
    #Sets a counter
    counter_int = 0 
    #Uses for loop to iterate through each row
    for rows in board:
        #Uses for loop to iterate through values in the row
        for value in rows:
            #If the value does not equal 0
            if value != 0:
                #Increase the counter by 1
                counter_int += 1
    #If the counter equals 42, then that means the board is full 
    if counter_int == 42:
        return "draw"
    #Iterates through each row using for loop
    for row in range(1,7):
        #Iterates through each value in the row using for loop
        for value in range(1,8):
            #Call the check_disc function to determine if there is a 
            #winning sequence at that value
            winning_sequence_bool = check_disc(board,row,value)
            #Returns the color of the winner if there is a winning sequence
            if winning_sequence_bool == True:
                color_str = board[row-1][value-1]
                if color_str == "w":
                    return "white"
                if color_str == "b":
                    return "black"
    return None

def main():
    '''
    Initializes the banner, introduction and usage and prints them
    Call the initialize() function to intialize the values of the board to 0
    Uses while loop to determine if the game is played again after it ends
        Uses while loop to play the game and iterate through turns
            Call the board_display() function to display the board
            Prompt for user input to determine user usage
            Uses while loop to reprompt the user if the input is not valid
            If the user_input equals "pass"
                The current player surrenders and the opponent wins
            If the user_input equals "exit"
                Prints an goodbye message
            If the user_input equals a valid integer
                Call the drop_disc() function to drop the disc onto the board
                If the drop_disc() function returns a row number
                    Call the is_game_over function to determine if
                    there is a winning sequence
    Returns: None
    '''
    #Initializes the banner, intro and usage prompts
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    print(banner)
    print(intro)
    print(usage)
    continue_game = 'yes'  # can't use "continue" because it has a special meaning
    #While the game input equals yes, the game will play again
    while continue_game == 'yes':
        column_list = ["1","2","3","4","5","6","7"]
        #Calls the choose_color function to determine who is who
        colors_tup = choose_color()
        #Extracts the colors of the player and opponent from the returned tuple
        player_str = colors_tup[0]
        opponent_str = colors_tup[1]
        print("You are '{:s}' and your opponent is '{:s}'.".\
              format(player_str,opponent_str))
        board = initialize()
        #Uses a counter to keep track of who is playing
        counter_int = 2
        #Uses while loop to iterate through the player turns
        while True:
            #If the counter is divisible by 2, the first player is playing
            #Else, the opponent is playing
            if counter_int % 2 == 0:
                player_turn = player_str
                other_player = opponent_str
            else:
                player_turn = opponent_str
                other_player = player_str
            #Display the board
            board_display(board) 
            #prompr for user input
            user_input = input( "{:s}'s turn :> ".format(player_turn))
            
            #Uses while loop to reprompt if the user_input is not valid
            while user_input.lower() != "pass" and user_input.lower() != \
            "exit" and user_input not in column_list:
                #If the user_input is a integer
                if user_input.isdigit():
                    #Uses while loop to reprompt for another column
                    while user_input not in column_list:
                        user_input = int(user_input)
                        valid_disc = drop_disc(board,user_input,player_turn)
                        print("Invalid column: 1 <= column <= 7. \
                              Please try again.")
                        user_input = input( "{:s}'s turn :> ".\
                                           format(player_turn))
                        break
                #If the user_input is a word and is not valid
                if user_input.isalpha() and user_input.lower() != "pass" \
                and user_input.lower() != "exit":
                    #Then print an error message and reprompt
                    print("Invalid option")
                    print(usage)
                    user_input = input( "{:s}'s turn :> ".format(player_turn))
            #If the user_input equals "pass", then the player surrenders
            if user_input == "pass":
                #A winning message is printed
                print("{:s} gave up! {:s} is the winner!! yay!!!".\
                      format(player_turn,other_player))
                break
            #If the user_input equals "pass"
            if user_input == "exit":
                #break out of the loop
                break
            #If the user_input is an integer
            if user_input.isdigit(): 
                #If the user_input is a valid column
                if user_input in column_list:
                    user_input = int(user_input)
                    #Call the drop_disc function
                    valid_disc = drop_disc(board,user_input,player_turn)
                    #If the drop_disc function returns "full"
                    if valid_disc == "full":
                        print("This column is full. Please try again.")
                    else:
                        #Call the is_game_over function to determine if 
                        #there is a winning sequence
                        game_over = is_game_over(board)
                        #if the is_game_over function returns "draw"
                        if game_over == "draw":
                            board_display(board)
                            print("This game ends in a draw.")
                            break
                        #if the is_game_over function returns "white
                        if game_over == "white":
                            board_display(board)
                            print("{:s} wins!".format(player_turn))
                            break
                        #if the is_game_over function returns "black"
                        if game_over == "black":
                            board_display(board)
                            print("{:s} wins!".format(player_turn))
                            break
                        #Adds one to switch the turn
                        counter_int += 1
        #An additional if statement to break out of a second loop
        if user_input == "exit":
            #Prints an exit message
            print("\nThanks for playing! See you again soon!")
            break
        #Prompts if the user wants to play again
        continue_game = input("Would you like to play again? ").lower() 
    else:
        print("\nThanks for playing! See you again soon!")
        
#Calls the main function    
if __name__ == "__main__":
    main()
