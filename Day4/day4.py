def solve(part):
    pairs_count = 0
    with open(r"C:\Users\beach\PycharmProjects\CBAdventOfCode22\Day4\input", 'r') as f:
        for line in f:
            a1, a2 = get_elf_assignments(line)
            if part == 1:
                if all(x in a1 for x in a2) or all(x in a2 for x in a1):
                    pairs_count += 1
            elif part == 2:
                if any(x in a1 for x in a2) or any(x in a2 for x in a1):
                    pairs_count += 1

        # elif part == 2:
        #     # Read the first three lines of the file
        #     c1 = f.readline().strip()
        #     c2 = f.readline().strip()
        #     c3 = f.readline().strip()
        #     while c1 and c2 and c3:
        #         for character in c1:
        #             if c2.find(character) != -1 and c3.find(character) != -1:
        #                 score += priority(character)
        #                 break
        #         # Read the next three lines of the file
        #         c1 = c2
        #         c2 = c3
        #         c3 = f.readline().strip()

    return pairs_count


def get_elf_assignments(raw_string):
    i = 0
    # Split the string into a first and second assignment
    assignment_one, assignment_two = str(raw_string).split(",")
    assignment_one_start, assignment_one_end = list(map(int, assignment_one.split("-")))
    assignment_two_start, assignment_two_end = list(map(int, assignment_two.split("-")))
    # create two lists
    assignment_one_range = list(range(assignment_one_start, assignment_one_end+1))
    assignment_two_range = list(range(assignment_two_start, assignment_two_end+1))

    return assignment_one_range, assignment_two_range


if __name__ == '__main__':
    print(solve(1))
    print(solve(2))
