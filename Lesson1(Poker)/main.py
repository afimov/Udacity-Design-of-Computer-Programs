import random


def poker(hands):
    return max(hands, key=hand_rank)

def deal(numhands, number_of_cards = 5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[number_of_cards * i : number_of_cards * (i+1)] for i in range(numhands)]

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1,ranks))
    elif kind(3,ranks) and kind(2, ranks):
        return (6, kind(3,ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2,ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def straight(ranks):
    return len(set(ranks)) == 5 and (max(ranks) - min(ranks) == 4)


def flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))

    if pair and low_pair != pair:
        return pair, low_pair

    return None

def hand_percentages(n = 700 * 1000):

    hand_names = [
        "High Card",
        "Pair",
        "2 Pair",
        "3 of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "4 of a Kind",
        "Straight Flush"
    ]

    counts = [0] * 9
    for i in range(n/5):
        for hand in deal(5):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1

    for i in range(8,-1,-1):
        print "%14s: %6.3f %%" % (hand_names[i], 100. * counts[i]/n)


hand_percentages()