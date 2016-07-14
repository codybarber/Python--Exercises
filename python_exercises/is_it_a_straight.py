def is_straight(cards):
    sorted_cards = sorted(cards)
    streak = 1
    x = 0
    y = 1
    for card in sorted_cards:
        if streak == 5:
            print "Your hand is a straight"
            break
        elif streak < 5 and card < 6:
            if sorted_cards[x] + 1 == sorted_cards[y]:
                streak = streak + 1
                x = x + 1
                y = y + 1
            else:
                streak = 0
                x = x + 1
                y = y + 1
        elif streak < 5 and card > 6:
            print "Your hand is not a straight"
            break
        else:
            pass

cards = [3, 8, 5, 4, 1, 9, 7]
is_straight(cards)
