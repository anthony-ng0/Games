'''
Basra: 

Algorithm:
    Call the main function 
        Initialize lists for the player cards,piles and basras
        Prompt for player input
        Use while loop to check for incorrect input and use loop to keep the program continuous
            Clear the lists, shuffle deck and initialize counters
            Use while loop to keep track of rounds
                Set up control for round 1 and subsequent rounds
                Call the distribute_cards function to distribute cards
                Call the display table function
                Use while loop to keep track of player turns and to play the game
                    Prompt for index integer to play a card
                    Call the play function to play the card
                If the deck is empty, there are no cards left
                    Call the compute_score function to compute score
                    Print out the scores and determine winner
        Remprompt for player input to see if user wants to play again         

'''
from cards import Card
from cards import Deck
from itertools import zip_longest,chain,combinations #for displaying the table and sum

def distribute_cards(deck,p1_cards,p2_cards,t_cards,round1):
    '''
    If it is round 1, Use for loops to distribute 4 cards to each player and the table
    If it is any other round, use for loops to distribute 4 cards to only the players
    Returns: None
    '''
    #If round1 boolean equals True
        #Use for loops to distribute 4 cards to each player and the table
    if round1 == True:
        for i in range(4):
            p1_cards.append(deck.deal())
        for i in range(4):
            p2_cards.append(deck.deal())
        for i in range(4):
            t_cards.append(deck.deal())
    #If the round1 boolean is false
        #Use for loop to distribute cards to each player only
    else:
        for i in range(4):
            p1_cards.append(deck.deal())
        for i in range(4):
            p2_cards.append(deck.deal())
             
def get_card_index(card,cards_list):
    '''
    Takes in a list of cards and the card players
    Use for loop and loops through the enumerated cards_list
        If the card played equals the card in the list
            Returns: the index
        Else:
            Returns: None
    
    '''
    #Use for loop to iterate though enumerated cards_list
    for i,v in enumerate(cards_list):
        #If card played equals the card in the list
        if card == v:
            return i
    return None
            
def get_matching_cards(card,t_cards):
    '''
    Initialize a list for the similar cards
    Use for loop to iterate through table cards list
        If the card's rank is equal to the card in the table list
            Append the table_list card to the list
    Returns: The similar_cards_list
    '''
    similar_cards_list = []
    #Use for loop to iterate through table list
    for v in t_cards:
        #If card played's rank equals the card's rank in table list
        if card.rank() == v.rank():
            #Appends the card in the table list
            similar_cards_list.append(v)
    return similar_cards_list
    
def numeric_card(card):
    '''
    Takes in the card played
    If the card's rank is less than or equal to 10
        Returns: True
    Else: 
        Returns: False
    '''
    #If the card's rank is less than or equal to 10
    if card.rank() <= 10:
        return True
    else:
        return False
    
def remove_cards(cards_list,cards):
    '''
    Takes in a list of cards, and the list of cards to be removed
    Uses for loop to iterate through list of cards
        Uses for loop to iterate through list of larger cards
            If the cards to be removed equals the cards in the bigger cards list
                Remove the card from the list
    Returns: None
    '''
    #Iterate through cards 
    for v in cards:
        #Iterates through cards list
        for i in cards_list:
            #IF the card equals the card in the cards_list, remove that card from the card list
            if v == i:
                cards_list.remove(i)

def get_sum_matching_cards(card,t_cards):
    '''this function return a list of cards that add up to card rank,
    if the card is Jack, Queen or king, the function returns empty list'''
    
    matching_sum_list=[]
    numeric_list=[]

    # make a list of the numeric cards on the table
    if len(t_cards)>1:
        for i in t_cards:
            if numeric_card(i):
                numeric_list.append(i)

    # collect pairs of numeric cards that sum to card
    if len(numeric_list) > 1:
        # collect combinations of length 2, i.e. pairs, of cards
        # only if the ranks of the pair sum to card's rank
        matching_sum_pair = [seq for seq in combinations(numeric_list, 2) \
                         if seq[0].rank() + seq[1].rank() == card.rank()]
        # combine the list of lists into one list
        matching_sum_list = list(chain(*matching_sum_pair))
    
    return matching_sum_list

def sum_rank(cards): #optional
    '''Put your docstring here''' 

    pass

def jack_play(card,player,pile,basra,t_cards):
    '''
    If the table_cards list is empty
        Add the card to the table and remove from player's hand
    Else:
        Add the cards in the table to the player's pile
        If there is already a jack or is full of jacks
            The played jack is a basra and will be added to the basra pile
            Remove from player's hand
        Else:
            Add the played jack to the player's pile
            Remove from player's hand
    Returns: None
    ''' 
    #If the length of table cards is 0 
    if len(t_cards) == 0:
        #Appends to table and removes from player's hand
        t_cards.append(card)
        player.remove(card)
    else:
        counter = 0
        #Appends cards in table list to the player's pile
        for i in t_cards:
            pile.append(i)
        #Counts the number of jacks on the table
        for i in t_cards:
            if i.rank() == 11:
                counter += 1
        #If the table has 1 or all jacks on table
        if counter == 1 or counter == len(t_cards):
            #Appends played card to basra
            basra.append(card)
            player.remove(card)
            t_cards.clear()
        else:
            #Appends played car to the pile
            pile.append(card)
            player.remove(card)
            t_cards.clear()

def seven_diamond_play(card,player,pile,basra,t_cards):
    '''
    If the table_cards list is empty
        Add the card to the table and remove from player's hand
    Else:
        Appends the cards in the pile to player's hand
        Use for loop to find the sum of card ranks on the table
        If the sum is less than or equal to 10:
            Add the played card to the basra pile
        Else:
            Add the played card to the pile list
        Remove from players hand
        Returns: None
    '''
    #If the length of table cards is 0
    if len(t_cards) == 0:
        t_cards.append(card)
        player.remove(card)
    else:
        #Appends the cards in the table to the player's pile
        card_sum = 0
        for i in t_cards:
            pile.append(i)
        #Calculates sum of cards on table
        for i in t_cards:
            card_sum += i.rank()
        #If the sum is less than or equal to 10
        if card_sum <= 10:
            #Card is basra and append to basra_list
            basra.append(card)
            player.remove(card)
            t_cards.clear()
        #If the sum is over 10, append the played card to the player pile
        else:
            pile.append(card)
            player.remove(card)
            t_cards.clear()

def play(card,player,pile,basra,t_cards):
    '''
    If the table is empty:
        Add the card to the table
        Remove from player's hand
    Elif the card is a jack:
        Call the jack_play function
    Elif the card is a seven of diamonds:
        Call the seven_diamond_play function
    Elif the card is a king or queen:
        Call the get_matching_cards function
        Depending on the board, the card played will be in basra pile or player_pile
    Else:
        Call the get_matching_cards function
        Call the get_sum_matching_cards function
        If there are no matching cards:
            Add the played card to the table
            Append the table cards to the player file
        Else:
          Depending on the board, the card played will be in basra pile or player_pile
    Returns: None    
    '''
    #If the table is empty
    if len(t_cards) == 0:
        t_cards.append(card)
        player.remove(card)
    #if the card played is a jack
    elif card.rank() == 11:
        jack_play(card,player,pile,basra, t_cards)
    #If the card played is a seven of diamonds
    elif card.rank() == 7 and card.suit() == 2:
        seven_diamond_play(card,player,pile,basra, t_cards)
    #if the card played is a queen or king
    elif card.rank() > 11:
        matching_cards = get_matching_cards(card, t_cards)
        #If the card played is a king or queen
        if len(matching_cards) == 0:
            t_cards.append(card)
            player.remove(card)
        else:
            #Iterates through the list of matching cards
            for i in matching_cards:
                for v in t_cards:
                    if i == v:
                        pile.append(v)
                        t_cards.remove(v)
            if len(t_cards) == 0:
                basra.append(card)
                player.remove(card)
            else:
                pile.append(card)
                player.remove(card)
    #If the card played's rank is less than or equal to 10
    else:
        matching_cards = get_matching_cards(card, t_cards)
        sum_cards = get_sum_matching_cards(card, t_cards)
        #If the lists are empty
        if len(sum_cards) == 0 and len(matching_cards) == 0:
            t_cards.append(card)
            player.remove(card)
        else:
            #Iterates through the matching_cards list
            for i in matching_cards:
                if i in t_cards:
                    t_cards.remove(i)
                    pile.append(i)
            #Iterates through the matching sum cards list
            for i in sum_cards:
                if i in t_cards:
                    t_cards.remove(i)
                    pile.append(i)
            #If the table is empty afterwards, card played is a basra
            if len(t_cards) == 0:
                basra.append(card)
                player.remove(card)
            #Appends the played card to player's pile
            #Remove from player's hand
            else:
                pile.append(card)
                player.remove(card)       

def compute_score(p1_pile,p2_pile,basra_1,basra_2):
    '''
    The player with the greater amount of cards will receive 30 points
    Iterate through the basra_lists for each player
        If the basra is a card with a rank less than or equal to 10
            The player's score will increase by 10
        Elif the basra is a king or queen
            The player's score will increase by 20
        Elif the basra is a jack
            The player's score will increase by 30
    Returns: a tuple of the the player 1 and player 2 scores
    '''
    player1_score = 0
    player2_score = 0
    #If the length of the player's pile and basra pile is greater than the other player's pile
    if (len(p1_pile)+len(basra_1)) > (len(p2_pile)+len(basra_2)):
        #Adds 30 to player 1's score
        player1_score += 30
    elif (len(p2_pile)+len(basra_2)) > (len(p1_pile)+len(basra_1)):
        #Adds 30 to player 1's score
        player2_score += 30
    #iterate through player 1's basra list
    for i in basra_1:
        #If the basra's rank is less than or equal to 10
        if i.rank() <= 10:
            player1_score += 10
        #If the basra is a king or queen
        elif i.rank() == 13 or i.rank() == 12:
            player1_score += 20
        #if the basra is a jack
        elif i.rank() == 11:
            player1_score += 30
    #Iterates through player 2's basra list
    for i in basra_2:
        if i.rank() <= 10:
            player2_score += 10
        elif i.rank() == 13 or i.rank() == 12:
            player2_score += 20
        elif i.rank() == 11:
            player2_score += 30
    score_tuple = (player1_score,player2_score)
    return score_tuple
    
def display_table(t_cards,p1_cards,p2_cards): 
    '''Display the game table.'''
    print("\n"+36*"=")
    print("{:^36s}".format('Player1'))
    print(9*" ", end = ' ')
    for card in p1_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    table = zip_longest(*[iter(t_cards)]*4,fillvalue=0)
    hline = "\n" + 36*"-" 
    str_ = hline + '\n '
    for row in table:
        str_ += 9*" "
        for c in range(0, 4):
            str_ += ("{:>3s}".format(str(row[c])) \
                     if row[c] is not 0 else ' ') +' '
        str_ += '\n'
    str_ += hline + '\n '
    print (str_)

    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    print(9*" ", end = ' ')
    for card in p2_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print("{:^36s}".format('Player2'))
    print(36*"=")
            
def main():
    '''
    Initialize lists to be used for player cards, piles and basras
    Prompt for user input if the player wants to play or not
    Use while loop to error check for incorrect responses
        Clear the lists, reset decks and shuffle the deck
        Use while loop to keep track of the rounds that are being played
            Call the distribute cards function
            Call the display_table function
            Use while loop to keep track of player turns
                Call the play function
        If the deck is empty, there are no cards left
            Call the compute_score function to compute score
            Print out the scores and determine winner
    Reprompt for player input to see if user wants to play again     
    Returns: None      
    '''
    RULES = '''
    Basra Card Game:
        This game belongs to a category of card games called “fishing cards games”. 
        Each player in turn matches a card from their hand with one (or more) of those 
        lying face-up on the table and then takes them. 
        If the card which the player played out does not match one of the existing cards, 
        it stays on the table.
    To win, you have to collect more points.'''
    
    print(RULES) 
    #Create an object of the Deck class
    answer = input("Would you like to play? y/Y or n/N? ")
    #Use while loop to error check and to play the game
    while answer!='n':
        #Create an object of the Deck class
        deck = Deck()
        #Initialize lists
        p1_cards = [] # card in hands player1
        p2_cards = [] #card in hands player2
        t_cards = []   # card on the floor
        p1_pile = [] # for player1
        p2_pile = [] # for player2
        basra_1 = []
        basra_2 = []
        #Clears the lists for the next game
        p1_cards.clear()
        p2_cards.clear()
        t_cards.clear()
        p1_pile.clear()
        p2_pile.clear()
        basra_1.clear()
        basra_2.clear()
        deck.shuffle()
        round_counter = 0
        turn_counter = 0
        game = True
        print("---------Start The game--------")
        #Use while loop to keep track of the rounds
        while game == True: 
            #Sets a condition for the round that is being played
            if round_counter == 0:
                round1 = True
                distribute_cards(deck, p1_cards, p2_cards, t_cards, round1)
                print("Dealing the cards, 4 cards for each player, 4 cards on the table")
                print("Cards left:  {:d}".format(len(deck)))
                display_table(t_cards,p1_cards,p2_cards)
            else:
                round1 = False
                distribute_cards(deck, p1_cards, p2_cards, t_cards, round1)
                print("\n------Start new round-----")
                print("Dealing the cards, 4 cards for each player")
                print("Cards left:  {:d}".format(len(deck)))
                display_table(t_cards,p1_cards,p2_cards)
                  
            round_int = True
            #Use while loop to check if the round is over or not
            while round_int == True:
                #Uses while loop to keep track of alternating player turns
                #This is for player 1
                while turn_counter % 2 == 0:  
                    card_input = input("Player {:d} turn: -> ".format(1))
                    if card_input != "q":
                        #Use while loop to ensure the input is correct
                        while int(card_input) < 0 or int(card_input) >= len(p1_cards):
                            card_input = input('Please enter a valid card\ index, 0 <= index <= {:d}\n'.format(len(p1_cards)-1))
                            print("Player {:d} turn: -> ".format(1))
                            #If the input of the prompt is "q", program will end
                            if card_input == "q":
                                break
                        if card_input != "q":
                            #Call the play function
                            #Calls the display_table function
                            card = p1_cards[int(card_input)]
                            play(card,p1_cards,p1_pile,basra_1,t_cards)
                            display_table(t_cards,p1_cards,p2_cards)
                            #Switches the turn
                            turn_counter += 1
                    if card_input == "q":
                       round_int = False
                       game = False
                       break
                #Use while loop to keep track of alternating player turns
                #This is for player 2
                while turn_counter % 2 != 0:
                    card_input = input("Player {:d} turn: -> ".format(2))
                    if card_input != "q":
                        #Use while loop to ensure the card input is correct 
                        while int(card_input) < 0 or int(card_input) >= len(p2_cards):
                            card_input = input('Please enter a valid card index, 0 <= index <= {:d}\n'.format(len(p2_cards)-1))
                            print("Player {:d} turn: -> ".format(2))
                            #If the card_input equals "q", the program will end
                            if card_input == "q":
                                break
                        if card_input != "q":
                            #Switches the turn
                            card = p2_cards[int(card_input)]
                            play(card,p2_cards,p2_pile,basra_2,t_cards)
                            display_table(t_cards,p1_cards,p2_cards)
                            turn_counter += 1
                    if card_input == "q":
                       round_int = False
                       game = False
                       break
                #If both player's hand are empty
                if len(p1_cards) == 0 and len(p2_cards) == 0:              
                    round_int = False
                    #Increase round counter
                    round_counter += 1
                    #If table is not empty, appends the card to player's 2 pile
                    if len(t_cards) != 0:
                        for i in t_cards:
                            p2_pile.append(i)
                    t_cards.clear()
                    display_table(t_cards,p1_cards,p2_cards)
                #If the deck is empty and 6 rounds have been played
                if len(deck) == 0:
                    game = False
                    #Calls the compute_score function
                    score_tuple = compute_score(p1_pile,p2_pile,basra_1,basra_2)
                    player_1_score = score_tuple[0]
                    player_2_score = score_tuple[1]
                    #Prints the player's score
                    if len(p1_cards) == 0 and len(p2_cards) == 0:   
                        print("player 1:  {:d}".format(player_1_score))
                        print("player 2:  {:d}".format(player_2_score))
                        print("")
                        #Uses control to display the winner of the game
                        if player_1_score > player_2_score:
                            print("Player 1 is the winner")
                        elif player_2_score > player_1_score:
                            print("Player 2 is the winner")
                        else:
                            print("No winner: equal score")
        if card_input == "q":
            print('Thanks for playing. See you again soon.')
            break
        answer = input("Would you like to play? y/Y or n/N? ")
    #Prints a goodbye message
    else:
        print('Thanks for playing. See you again soon.')
    
# main function, the program's entry point
if __name__ == "__main__":
    main()
