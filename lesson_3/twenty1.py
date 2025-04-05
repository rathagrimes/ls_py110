# TODO: Best 3 out of 5
#
# Standard deck of 52 cards
# Player can only see one of dealer's cards in hand
# Initial deal: 2 cards to each of player, dealer
# Phase 1: Player can choose to hit or stay until they bust or stay
# Phase 2: Dealer will hit until they reach a total of at least 17
# If someone busts, the other player is the winner.
# Otherwise, winner has higher hand value
#
# player_hand = [ card, card, ... ]
# dealer_hand = [ card, card, ... ]
# print_board(player_hand, dealer_hand)
# count_hand(hand)


import random

DEALER_MIN = 17
MAX_UNDER_BUST = 21

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
SUITS = ['♥', '♠', '♦', '♣']

DECK = [[rank, suit]
        for rank in RANKS
        for suit in SUITS]


def get_yn_choice(prompt):
    while True:
        response = input(prompt + " (y/n) ")
        try:
            return bool(['n', 'y'].index(response[:1].lower()))
        except ValueError:
            print(f"Invalid value '{response}', try again.")

def render_hand(hand, num_to_hide=-1):
    # With the num_to_hide requirement, the nice simple list comprehension
    # isn't sufficient anymore
    # return " ".join([str(rank) + suit
    #                     for (rank, suit) in hand])
    rendered_cards = []
    for i, card in enumerate(hand):
        if num_to_hide > -1 and i < num_to_hide:
            rendered_cards.append('##')
        else:
            rank, suit = card
            rendered_cards.append(str(rank) + suit)
    return "[ " + " ".join(rendered_cards) + " ]"

def print_board(player_hand, dealer_hand):
    print(f"Player: {render_hand(player_hand)}  " + \
          f"Dealer: {render_hand(dealer_hand, 1)}")

def hit(hand, deck):
    if len(deck) > 0:
        hand.append(deck.pop())
    else:
        raise ValueError("No more cards!")

def count_value(hand, cache=None):
    if cache and cache[0] is not None:
        return cache[0]

    total_value = 0
    if len(hand) > 0:
        sorted_by_rank = sorted(hand, key=lambda x: RANKS.index(x[0]))
        #print("Sorted: ", sorted_by_rank)
        for card in sorted_by_rank:
            if isinstance(card[0], int):
                total_value += card[0]
            elif card[0] == 'A':
                # Naive approach doesn't work, see test case 8
                #value += 1 if value + 10 > 21 else 11
                break
            else:
                total_value += 10

        # Handle aces separately in a holistic manner
        ace_values = [1 for rank, _ in hand if rank == 'A']
        for i, _ in enumerate(ace_values):
            # See if flipping another ace to 11 will not bust
            if total_value + sum(ace_values) + 10 <= 21:
                ace_values[i] += 10
            else:
                break
        total_value += sum(ace_values)

        if cache:
            cache[0] = total_value

    return total_value

def test_count_value():
    def validate(value, expected):
        result = count_value(value)
        print("PASS" if expected == result else "FAIL",
              value,
              ": expected ",
              expected,
              " got ",
              result)
    # Cases 1-3: vanilla
    validate([[3, '♥'], [4, '♣'], ['J', '♣']], 17)
    validate([['K', '♣'], ['J', '♣'], [3, '♥']], 23)
    validate([[5, '♥'], ['Q', '♥']], 15)
    # Case 4: Ace as 11
    validate([['K', '♥'], ['A', '♣']], 21)
    # Case 5: Ace as 1
    validate([['A', '♣'], ['Q', '♥'], [5, '♥']], 16)
    # Cases 6-7: two aces
    validate([['A', '♥'], [3, '♣'], ['A', '♦']], 15)
    validate([[2, '♦'], ['A', '♠'], ['A', '♥']], 14)
    # Case 8: Unlikely but tricky case.
    validate([['A', '♥'], ['A', '♣'], ['A', '♦'], ['K', '♥']], 13)

def busted(hand, cache):
    return count_value(hand, cache) > MAX_UNDER_BUST

def play_game():
    # shouldn't shuffle the prototypical deck, mutates a constant
    game_deck = DECK.copy()
    random.shuffle(game_deck)

    player_hand = [game_deck.pop(), game_deck.pop()]
    dealer_hand = [game_deck.pop(), game_deck.pop()]

    player_value_cache = [None]
    dealer_value_cache = [None]

    print("Welcome. Try to get as close to possible to 21 without going over.")
    print_board(player_hand, dealer_hand)

    # Player's turn
    while not busted(player_hand, player_value_cache):
        if get_yn_choice("Your current hand value is " \
                        + f"{count_value(player_hand, player_value_cache)}. " \
                        + "Do you want to hit?"):
            hit(player_hand, game_deck)
            player_value_cache[0] = None # Cachebust after mutating deck
            print_board(player_hand, dealer_hand)
        else:
            break

    if busted(player_hand, player_value_cache):
        print(f"{count_value(player_hand, player_value_cache)}! " \
              + "You busted out, game over.")
        return
    print("Your final hand value is " \
          + f"{count_value(player_hand, player_value_cache)}.")

    # Dealer's turn
    while not busted(dealer_hand, dealer_value_cache) \
        and count_value(dealer_hand, dealer_value_cache) < DEALER_MIN:
        print("Dealer hits")
        hit(dealer_hand, game_deck)
        dealer_value_cache[0] = None # Cachebust after mutating deck
        #print_board(player_hand, dealer_hand)

    dealer_value = count_value(dealer_hand, dealer_value_cache)
    if busted(dealer_hand, dealer_value_cache):
        print(f"Dealer's final hand value is {dealer_value}. " \
              + "{render_hand(dealer_hand)}")
        print("Dealer busted, you win.")
        return
    print("Dealer stays.")
    print(f"Dealer's final hand value is {dealer_value}. " \
          + f"{render_hand(dealer_hand)}")

    # Announce the results
    player_value = count_value(player_hand, player_value_cache)
    if player_value > dealer_value:
        print("You win!")
    elif dealer_value > player_value:
        print("Dealer wins.")
    else:
        print("Tie.")


def main_loop():
    while True:

        play_game()

        if not get_yn_choice("Do you want to play again?"):
            break

main_loop()
#test_count_value()
