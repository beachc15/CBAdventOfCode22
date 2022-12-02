def run1():
    player1score = 0
    player2score = 0
    ans1, ans2 = '', ''
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day2\input", 'r') as f:
        lines = f.readlines()
        for line in lines:
            ans1, ans2 = line[0], line[2]
            ans2 = convert(ans2)
            print('P1 played: ', ans1, 'P2 played: ', ans2)
            thewinner = winner(ans1, ans2)
            print('winner was', thewinner)
            if thewinner == 1:
                player1score += 6
                print('P1 got 6 addt points')
            elif thewinner == 2:
                player2score += 6
                print('P2 got 6 addt points')
            elif thewinner == 0:
                print('draw')
                player1score += 3
                player2score += 3
            else:
                print("ERROR")
            # add score based on choice
            player1score += score(ans1)
            player2score += score(ans2)

    return player1score, player2score


def run2():
    player1score = 0
    player2score = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day2\input", 'r') as f:
        lines = f.readlines()
        for line in lines:
            ans1, the_outcome = line[0], line[2]
            # 0 for lose, 1 for draw, 2 for win
            the_outcome = convert2(the_outcome)
            ans2 = give_move(ans1, the_outcome)
            print(ans1, ans2)
            thewinner = winner(ans1, ans2)

            if thewinner == 1:
                player1score += 6
            elif thewinner == 2:
                player2score += 6
            elif thewinner == 0:
                player1score += 3
                player2score += 3
            else:
                pass

            player1score += score(ans1)
            player2score += score(ans2)

    return player1score, player2score


def convert2(__ans):
    if __ans == 'X':
        __ans = 0
    elif __ans == 'Y':
        __ans = 1
    elif __ans == 'Z':
        __ans = 2
    return __ans


def convert(__ans):
    if __ans == 'X':
        __ans = 'A'
    elif __ans == 'Y':
        __ans = 'B'
    elif __ans == 'Z':
        __ans = 'C'
    return __ans


def give_move(__ans1, __outcome):
    if __outcome == 1:
        # result is tie
        return __ans1
    elif __outcome == 0:
        if __ans1 == "A":
            return 'C'
        elif __ans1 == "B":
            return "A"
        elif __ans1 == "C":
            return "B"
    elif __outcome == 2:
        if __ans1 == "A":
            return 'B'
        elif __ans1 == "B":
            return "C"
        elif __ans1 == "C":
            return "A"


def winner(__ans1, __ans2):
    if __ans1 == __ans2:
        # 0 means tie
        return 0
    elif __ans1 == 'A':
        if __ans2 == "C":
            # 1 mean 1 wins
            return 1
        else:
            return 2
    elif __ans1 == "B":
        if __ans2 == "A":
            return 1
        else:
            return 2
    elif __ans1 == "C":
        if __ans2 == "B":
            return 1
        else:
            return 2


def score(__ans):
    # print(__ans)
    factor = 0
    if __ans == 'A':
        factor = 1
    elif __ans == 'B':
        factor = 2
    elif __ans == 'C':
        factor = 3
        # print(factor)
    return factor


if __name__ == '__main__':
    x, y = run2()
    print(x, '', y)
