import time

def solve(part):
    score = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day3\input", 'r') as f:
        if part == 1:
            # Read the input file line by line
            for line in f:
                first_half = line[:len(line) // 2]
                second_half = line[len(line) // 2:]
                for character in first_half:
                    if second_half.find(character) != -1:
                        score += priority(character)
                        break
        elif part == 2:
            # Read the first three lines of the file
            c1 = f.readline().strip()
            c2 = f.readline().strip()
            c3 = f.readline().strip()
            while c1 and c2 and c3:
                for character in c1:
                    if c2.find(character) != -1 and c3.find(character) != -1:
                        score += priority(character)
                        break
                # Read the next three lines of the file
                c1 = c2
                c2 = c3
                c3 = f.readline().strip()

    return score


def priority(x):
    # The ASCII value of the lowercase letters is in the range 97-122,
    # and the ASCII value of the uppercase letters is in the range 65-90.
    if ord(x) >= 97:
        return ord(x) - 96
    elif ord(x) >= 65:
        return ord(x) - 38
    else:
        return 0


if __name__ == '__main__':
    start = time.time()
    print(solve(1))
    print(solve(2))
    end = time.time()
    print(end-start)