def solve():
    score = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day3\input", 'r') as f:
        for line in f:
            first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
            for character in first_half:
                if character in second_half:
                    score += priority(character)
                    break
    return score


def solve2():
    sack_i, score = 0, 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day3\input", 'r') as f:
        chunks = f.read().split('\n')
    while sack_i < len(chunks) - 1:
        c1 = (chunks[sack_i])
        c2 = (chunks[sack_i + 1])
        c3 = (chunks[sack_i + 2])

        for character in c1:
            if c1.find(character) != -1 and c2.find(character) != -1 and c3.find(character) != -1:
                score += priority(character)
                break

        sack_i += 3

    return score


def priority(x):
    li = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return li.index(x)


if __name__ == '__main__':
    print(solve())
    print(solve2())
