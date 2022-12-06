def solve(part: int):
    # boxes
    one = ['Z', 'P', 'M', 'H', 'R']
    two = ['P', 'C', 'J', 'B']
    three = ['S', 'N', 'H', 'G', 'L', 'C', 'D']
    four = ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L']
    five = ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M']
    six = ['T', 'F', 'S', 'Z', 'B', 'G']
    seven = ['N', 'R', 'V']
    eight = ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M']
    nine = ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
    boxes = [one, two, three, four, five, six, seven, eight, nine]

    top_row = [None]
    with open("input", 'r') as f:
        for line in f:
            amount, start, end = parse_direction(line)
            boxes_to_move = boxes[start][-amount:]
            del boxes[start][-amount:]
            # copy the list
            flipped_boxes_to_move = boxes_to_move.copy()
            # flip the order
            flipped_boxes_to_move.reverse()
            # place boxes on new stack
            if part == 9000:
                boxes[end].extend(flipped_boxes_to_move)
            if part == 9001:
                boxes[end].extend(boxes_to_move)
            top_row = get_top_row(boxes)

    return ''.join(top_row)


def get_top_row(stacks: list):
    # Take in a list of letters, return the last letter or "top" of box stack
    out_stack = []
    for stack in stacks:
        try:
            out_stack.append(stack[-1])
        except IndexError:
            pass
    return out_stack


def parse_direction(direction: str):
    # take in input in the form "move X from Y to Z"
    amount, start, end = 0, 0, 0

    # pull variables
    split_direction = direction.split(' ')
    amount = int(split_direction[1])
    start = int(split_direction[3]) - 1
    end = int(split_direction[5]) - 1

    return amount, start, end


if __name__ == '__main__':
    print(solve(9000))
    print(solve(9001))
