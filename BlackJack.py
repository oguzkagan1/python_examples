"""In this exercise you are going to implement some rules of Blackjack, such as the way the game is played and scored."""

def value_of_card(card):
    if card == "A":
        return 1
    elif card in "JQK":
        return 10
    else:
        return int(card)
def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two 
def value_of_ace(card_one, card_two):
    card_value = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        ace = 1
        return ace
    elif card_value <= 10:
        ace = 11
        return ace
    else:
        ace = 1
        return ace
def is_blackjack(card_one, card_two):
    if (card_one in "A") and (card_two in "KQJ10"):
        blackjack = True
        return blackjack
    elif  (card_two in "A") and (card_one in "KQJ10"):
        blackjack = True
        return blackjack
    else:
        blackjack = False
        return blackjack
        
def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        split_pairs = True
        return split_pairs
    else :
        split_pairs = False
        return split_pairs
        
    
def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)
    if total_value in [9, 10, 11]:
        return True
    else:
        return False

card_one = "3"
card_two = "6"

print("Value Of Ace" ,value_of_ace(card_one, card_two))
print("is Blackjack :", is_blackjack(card_one, card_two))
print("Can Double Down :", can_double_down(card_one, card_two))