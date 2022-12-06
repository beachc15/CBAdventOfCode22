def solve(part: int) -> int:
    # boxes
    one = ['Z', 'P', 'M', 'H', 'R']
    two = ['P', 'C', 'J', 'B']
    pairs_count = 0
    with open("input", 'r') as f:
        for line in f:
            a1, a2 = get_elf_assignments(line)
            if part == 1:
                if all(x in a1 for x in a2) or all(x in a2 for x in a1):
                    pairs_count += 1
            elif part == 2:
                if any(x in a1 for x in a2) or any(x in a2 for x in a1):
                    pairs_count += 1
    return pairs_count


def get_elf_assignments(raw_string: str) -> tuple[list[int], list[int]]:
    # Split the string into a first and second assignment
    assignment_one, assignment_two = raw_string.split(",")
    assignment_one_start, assignment_one_end = list(map(int, assignment_one.split("-")))
    assignment_two_start, assignment_two_end = list(map(int, assignment_two.split("-")))
    # create two lists
    assignment_one_range = list(range(assignment_one_start, assignment_one_end + 1))
    assignment_two_range = list(range(assignment_two_start, assignment_two_end + 1))

    return assignment_one_range, assignment_two_range


if __name__ == '__main__':
    print(solve(1))
    print(solve(2))
