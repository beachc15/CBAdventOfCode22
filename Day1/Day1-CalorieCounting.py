# input: calories

def run2():
    current_calorie = 0
    top_three = [0, 0, 0]
    with open('/Users/charliebeach/PycharmProjects/CBAdventOfCode22/Day1/input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                top_three[0] = max(current_calorie, top_three[0])
                current_calorie = 0
                top_three.sort()
            else:
                current_calorie += int(line)

    return sum(top_three)


def run1():
    current_calorie = 0
    max_cal = 0
    with open('/Users/charliebeach/PycharmProjects/CBAdventOfCode22/Day1/input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                max_cal = max(max_cal, current_calorie)
                current_calorie = 0
            else:
                current_calorie += int(line)

    return max_cal


if __name__ == '__main__':
    answer1 = run1()
    answer2 = run2()
    print("Max calories carried by an elf is", answer1)
    print('Combined calories carried by top 3 elfs is', answer2)
