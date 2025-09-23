"""
Created by: Boning Zhu
Created on: Sept 23 2025
This program is prompts the user for a hand of three
cards and determines the point value of the hand.
"""

"""
check rank
in the if() function it list the all possible ranks
"""
def validate_rank(rank):
    if (rank == "2" or rank == "3" or rank == "4" or rank == "5" or
        rank == "6" or rank == "7" or rank == "8" or rank == "9" or
        rank == "10" or rank == "J" or rank == "Q" or
        rank == "K" or rank == "A"):
        return True
    else:
        return False

"""
check suit
"""

def validate_suit(suit):
    if (suit == "H" or suit == "D" or suit == "C" or suit == "S"):
        return True
    else:
        return False

"""
convert rank to value
"""
def rank_value(rank):
    if rank == "J" or rank == "Q" or rank == "K":
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)  # for 2–10


print("Enter cards as <rank><suit> (e.g., AH or 10S).")

"""
Card 1
"""
card1 = input("Card 1: ")
suit1 = card1[-1]
rank1 = card1[:-1]

if not validate_rank(rank1):
    print(f"Invalid rank {rank1}. Must be 2-10, J, Q, K, or A.")
if not validate_suit(suit1):
    print(f"Invalid suit {suit1}. Must be H, D, C, or S.")
if not validate_rank(rank1) or not validate_suit(suit1):
    exit()

"""
Card 2
"""
card2 = input("Card 2: ")
suit2 = card2[-1]
rank2 = card2[:-1]

if not validate_rank(rank2):
    print(f"Invalid rank {rank2}. Must be 2-10, J, Q, K, or A.")
if not validate_suit(suit2):
    print(f"Invalid suit {suit2}. Must be H, D, C, or S.")
if not validate_rank(rank2) or not validate_suit(suit2):
    exit()

if card2 == card1:
    print(f"There can't be two {card2} in the same hand. You're playing with a fake deck!")
    exit()

"""
Card 3
"""
card3 = input("Card 3: ")
suit3 = card3[-1]
rank3 = card3[:-1]

if not validate_rank(rank3):
    print(f"Invalid rank {rank3}. Must be 2-10, J, Q, K, or A.")
if not validate_suit(suit3):
    print(f"Invalid suit {suit3}. Must be H, D, C, or S.")
if not validate_rank(rank3) or not validate_suit(suit3):
    exit()

if card3 == card1 or card3 == card2:
    print(f"There can't be two {card3} in the same hand. You're playing with a fake deck!")
    exit()

"""

"""
val1 = rank_value(rank1)
val2 = rank_value(rank2)
val3 = rank_value(rank3)

"""
 We need the maximum sum of ranks of cards of the same suit.
"""
sum1 = 0
sum2 = 0
sum3 = 0
"""
Check each suit grouping manually, since no loops allowed
"""
if suit1 == suit2 and suit1 == suit3:
    total = val1 + val2 + val3
elif suit1 == suit2:
    sum1 = val1 + val2
    if val3 > sum1:
        total = val3
    else:
        total = sum1
elif suit1 == suit3:
    sum2 = val1 + val3
    if val2 > sum2:
        total = val2
    else:
        total = sum2
elif suit2 == suit3:
    sum3 = val2 + val3
    if val1 > sum3:
        total = val1
    else:
        total = sum3
else:
    """
    all different suits -> pick highest single card
    """
    if val1 >= val2 and val1 >= val3:
        total = val1
    elif val2 >= val1 and val2 >= val3:
        total = val2
    else:
        total = val3

print(f"Point value of hand: {total}")
