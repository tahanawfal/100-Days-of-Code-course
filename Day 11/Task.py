import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def start_game():
    my_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    my_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    hand_fixing(True)
    hand_fixing(False)
    show_hands(True)
    show_hands(False)

def hit_stand_choices(turn):
    global my_hit_flag, computer_hit_flag
    if turn and my_hit_flag:
        hit_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if hit_choice == "y":
            pass
        elif hit_choice == "n":
            my_hit_flag = False
        else:
            print("Invalid input")
            hit_stand_choices(turn)
    else:
        if computer_score > 17:
            computer_hit_flag = False

def deck_shuffle(turn):
    if turn and my_hit_flag:
        my_hand.append(random.choice(cards))
    elif not turn and computer_hit_flag:
        computer_hand.append(random.choice(cards))

def hand_fixing(turn):
    global my_hand, computer_hand
    if turn:
        hand = my_hand
    else:
        hand = computer_hand
    hand_sum = sum(hand)
    ace_count = hand.count(11)
    if ace_count > 0:
        for ace in range(ace_count):
            if hand_sum > 21:
                ace_index = hand.index(11)
                hand[ace_index] = 1
                hand_sum = sum(hand)
    if turn:
        my_hand = hand
    else:
        computer_hand = hand

def show_hands(turn):
    global my_score, computer_score
    if turn and my_hit_flag:
        my_score = sum(my_hand)
        print(f"Your cards: {my_hand}, current score: {my_score}")
        print(f"Computer first card: {computer_hand[0]}")
    else:
        computer_score = sum(computer_hand)

def announce_winner():
    print(f"Your final hand: {my_hand}, final score: {my_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if computer_score > 21:
        print("Computer exceeded 21, you win")
    elif my_score > 21:
        print("you exceeded 21, you lost")
    elif my_score > computer_score:
        print("You won")
    elif my_score < computer_score:
        print("You lost")
    else:
        print("Draw")

start_play = "y"

print(logo)
while start_play == "y":
    my_hand = []
    computer_hand = []
    my_hit_flag = True
    computer_hit_flag = True
    my_score = 0
    computer_score = 0
    my_turn = True

    # start the game
    start_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_play == "y":
        start_game()
        if my_score == 21:
            announce_winner()
            break
    else:
        print("Thank you")
        break

    while (my_hit_flag or computer_hit_flag) and (my_score <= 21 and computer_score <= 21):

        # hit or stand
        hit_stand_choices(my_turn)

        # deck shuffle
        deck_shuffle(my_turn)

        # hand fix
        hand_fixing(my_turn)

        # count totals
        show_hands(my_turn)

        # handle the turn
        if my_hit_flag:
            my_turn = not my_turn
        else:
            if my_turn:
                my_turn = False

    announce_winner()