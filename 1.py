# A low line count approach. It's more unreadable this way, I know.
def part1():
    # Split the input into entities, convert to integer and sum the integers.
    # Finally, check the highest value from the resulting list.
    return max([sum([int(x) for x in x.split('\n')]) for x in open('In/1').read().split('\n\n') if x])


def part2():
    # same as in part1 but sort the list and only keep the last 3 numbers in the list.
    # Finally, sum the last three numbers.
    return sum(sorted([sum([int(x) for x in x.split('\n')]) for x in open('In/1').read().split('\n\n') if x])[-3:])


print(f"Answer for part 1: {part1()}")
print(f"Answer for part 2: {part2()}")
