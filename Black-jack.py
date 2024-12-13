
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __str__(self):
        return f"{self.rank} of {self.suit}"


mycard = Card("Hearts","Ace")

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):    
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop() 


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    


class Chips:
    
    def __init__(self,total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
        return self.total
        
    def lose_bet(self):
        self.total = self.total - self.bet
        return self.total


def take_bet(chips):
    while True:     
        try:
            chips.bet = int(input("Please enter your no. of chips you want to bet: "))    
        except:
            print("Please enter a valid amount for your bet")
        else:
            if chips.bet > chips.total:
                print(f"Place your bet from remaining balance of {player_chips.total} /-")
            else:
                break
            

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        choice = input("Want to Hit or Stand (h/s)? ")
        if choice[0].lower() == 'h':
            hit(deck,hand)

        elif choice[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False

        else:
            print("Please enter a valid choice from 'h' or 's'")
            continue
        break



def show_some(player,dealer):
    print('\n')
    print("Dealer's hand is: ")
    print("First card is hidden")
    print(f"Second card is {dealer.cards[1]}")
    print('\n')
    print(f"Player's hand is: ")
    for card in player.cards:
        print(card)      
    
def show_all(player,dealer):
    print('\n')
    print(f"Dealer's hand: ")
    for card in dealer.cards:
        print(card)     

    print(f"Value of dealer's hand is: {dealer.value}")
    print('\n')
    print(f"Player's hand: ")
    for card in player.cards:
        print(card)    

    print(f"Value of player's hand is: {player.value}")


def player_busts(player,dealer,chips):
    print("\nPlayer busted")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer Won!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nPlayer Won, Dealer Busted")
    chips.win_bet()
   
def dealer_wins(player,dealer,chips):
    print("\nDealer Wins!!")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nIt is a Tie.")



while True:
    # Print an opening statement
    print('Welcome to the "Black Jack" game')

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for x in range(2):
        
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()
      
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing: 
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total
    print(f"\n Player total chips are at: {player_chips.total}")    
        
    # Ask to play again
    game_on = input("Do you want to play another hand (y/n)? ")
    if game_on[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you")
        break
