with (open('numbers.txt', 'r') as file):
    content = []
    for i in file:
        content.append(int(i))
    middle_value = int((max(content) + min(content)) / 2)
    steps_count = 0
    for value in content:
        steps_count += abs(value - middle_value)
    print(steps_count)
