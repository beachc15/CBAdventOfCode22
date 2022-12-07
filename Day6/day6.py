def solve(part: int):
    with open("input", 'r') as f:
        stream = f.read()
    if part == 1:
        # find unique set of four characters in string named stream
        i, n = 3, 3
    if part == 2:
        # find unique set of fourteen characters in string named stream
        i, n = 13, 13
    while i < len(stream):
        # iterate through the string using i, if the string "set_of_n" contains all unique values then return the index
        set_of_n = stream[i - n:i + 1]
        if len(set(set_of_n)) == len(set_of_n):
            break
        i += 1
    return i + 1


if __name__ == '__main__':
    print(solve(1))
    print(solve(2))
