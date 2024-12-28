import random as r

# creating list, variable for functions
card_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ask_play = None
while ask_play not in ('y', 'n'):
    ask_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n' )? :  ").lower()
player_cards = []
computer_cards = []
scores = {}
cards = {}


def pick_card(my_list, number_cards):
    for i in range(0, number_cards):
        single_player_card = r.choice(card_list)
        my_list.append(single_player_card)
        cards["player"] = my_list
        single_computer_card = computer_cards.append(r.choice(card_list))
        cards["computer"] = computer_cards
    return cards


def comunication():
    if len(cards["player"]) >= 2 and give_final_score:
        if scores['computer'] > scores['player'] or scores['player'] > 21:
            print(f"Your cards {cards['player']}, player score {scores['player']}")
            print(f"Computer card: {cards['computer']}, computer score {scores['computer']}")
            print("You lose! Try another game!")
        elif scores['computer'] < scores['player'] and scores['player'] <= 21:
            print(f"Your cards {cards['player']}, player score {scores['player']}")
            print(f"Computer card: {cards['computer']}, computer score {scores['computer']}")
            print("Congratulations, You won! Play game!")
    elif len(cards["player"]) == 2:
        if len(cards["player"]) == 2 and not give_final_score:
            print(f"Your cards {cards['player']},current score {scores['player']}")
            #print(f"Computer card: {cards['computer'][0]}")
        elif scores['computer'] > scores['player'] or scores['player'] > 21 and give_final_score:
            print(f"Your cards {cards['player']}, player score {scores['player']}")
            print(f"Computer card: {cards['computer']}, computer score {scores['computer']}")
            print("You lose! Try another game!")
        elif scores['computer'] < scores['player'] and scores['player'] <= 21 and give_final_score:
            print(f"Your cards {cards['player']}, player score {scores['player']}")
            print(f"Computer card: {cards['computer']}, computer score {scores['computer']}")
            print("Congratulations, You won! Play again!")
        elif scores['computer'] == scores['player'] and scores['player'] <= 21 and give_final_score:
            print(f"Your cards {cards['player']}, player score {scores['player']}")
            print(f"Computer card: {cards['computer']}, computer score {scores['computer']}")
            print("It's a tie! Play again!")


def game_score():
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    scores["player"] = player_score
    scores["computer"] = computer_score
    return scores


if ask_play == 'y':
    pick_card(player_cards, 2)
    game_score()
    give_final_score = False
    comunication()
    another_card = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
    give_final_score = True
    if another_card == "y":
        pick_card(player_cards, 1)
        game_score()
        give_final_score = True
        comunication()
    elif another_card == 'n':
        game_score()
        comunication()
