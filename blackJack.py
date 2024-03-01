import math
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Import modules
import random
import art
from art import logo


print(logo)

# Functions

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Returns a drandom card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
  
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
    #0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Hint 8: Inside calculate_score() check for an 11 (ace). 
    ## If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    else:
        score = sum(cards)# part or hint 6
        return score    

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack."
    elif user_score == 0:
        return "You win, with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."  
    else:
        return "You lose."
        
is_game_over = False

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
while not is_game_over:

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    
    #Hint 10: If the game has not ended, ask the user if they want to draw another card.
    #If yes, then use the deal_card() function to add another card to the             user_cards List. If no, then the game has ended.
    else:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == "y":
            user_cards.append(deal_card())      
        else:
            is_game_over = True
            

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))

##tests##
# print(deal_card())
# print(f"{user_cards}")
# print(f"{computer_cards}")
# print(user_score)
