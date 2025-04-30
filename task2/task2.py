with (
    open('circle.txt', 'r') as file_1,
    open('dot.txt', 'r') as file_2,
):
    data_circle, data_points = [], []
    for i in file_1:
        data_circle.append([int(x) for x in i.split()])
    for i in file_2:
        data_points.append([int(x) for x in i.split()])

    for point in data_points:
        y_length_2 = abs(point[1] - data_circle[0][1]) ** 2
        x_length_2 = abs(point[0] - data_circle[0][0]) ** 2
        if x_length_2 + y_length_2 > data_circle[1][0] ** 2:
            print(2)
        elif x_length_2 + y_length_2 < data_circle[1][0] ** 2:
            print(1)
        else:
            print(0)
