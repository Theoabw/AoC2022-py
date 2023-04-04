def part1():
    with open('In/2') as IN:
        data = [x.split(' ') for x in IN.read().split('\n')]

    # A = rock, B = paper, C = scissors
    # X = rock, Y = paper, Z = scissors
    loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    points = {'X': 1, 'Y': 2, 'Z': 3}

    score = 0

    for line in data:
        if loss[line[0]] == line[1]:
            score += points[line[1]]
        elif win[line[0]] == line[1]:
            score += 6 + points[line[1]]
        else:
            score += 3 + points[line[1]]

    return score


def part2():
    with open('In/2') as IN:
        data = [x.split(' ') for x in IN.read().split('\n')]

    loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    points = {'X': 1, 'Y': 2, 'Z': 3}

    score = 0

    for line in data:
        if line[1] == 'X':
            score += points[loss[line[0]]]
        elif line[1] == 'Z':
            score += 6 + points[win[line[0]]]
        else:
            score += 3 + points[draw[line[0]]]

    return score


print(f"total score for part 1: {part1()}")
print(f"total score for part 2: {part2()}")
