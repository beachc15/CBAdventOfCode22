def run1():
    score = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day3\input", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = False
            firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:]
            print(firstpart, secondpart)
            for character in firstpart:
                if character in secondpart and match == False:
                    match = True
                    score += priority(character)
    return score


def run2():
    sack_i = 0
    score = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day3\input", 'r') as f:
        input = f.read()
    chunks = input.split('\n')
    while sack_i < len(chunks) - 1:
        match = False
        c1 = (chunks[sack_i])
        c2 = (chunks[sack_i + 1])
        c3 = (chunks[sack_i + 2])

        for character in c1:

            if character in c2 and character in c3 and match is False:
                print(character)
                match = True
                score += priority(character)

        sack_i += 3

    return score


def priority(x):
    li = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return li.index(x)


if __name__ == '__main__':
    print(run2())
