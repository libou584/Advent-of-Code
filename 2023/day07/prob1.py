


def type(hand) :
    if all([hand[i] == hand[0] for i in range(1, 5)]) :
        return 7
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4 :
        return 6
    elif 


def sort_(hand1, hand2) :
