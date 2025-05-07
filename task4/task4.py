import sys

numbers = sys.argv[1]

with open(numbers, 'r') as file:
    content = []
    for i in file:
        content.append(int(i))
    content = sorted(content)
    median_index = int(len(content) / 2)
    steps_count = 0
    for value in content:
        steps_count += abs(value - content[median_index])
    print(steps_count)
