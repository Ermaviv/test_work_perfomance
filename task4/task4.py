import sys

numbers = sys.argv[1]
# не рабочий код, неправильное среднее число

with open(numbers, 'r') as file:
    content = []
    for i in file:
        content.append(int(i))
    mode = max(content, key=content.count)
    if content.count(mode) == 1:
        mode = int((max(content) + min(content)) / 2)
    steps_count = 0
    for value in content:
        steps_count += abs(value - mode)
    print(steps_count)
