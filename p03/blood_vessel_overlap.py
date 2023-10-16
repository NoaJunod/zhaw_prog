network = [[0 for _ in range(10)] for _ in range(10)]
vessels = [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]]
    ]


def examine():
    for v in vessels:
        distance = max(abs(v[0][0] - v[1][0]), abs(v[0][1] - v[1][1])) + 1
        start_point = v[0]
        end_point = v[1]
        x = v[0][0]
        y = v[0][1]
        x_dir = 0
        y_dir = 0
        if start_point[0] < end_point[0]:
            x_dir = 1
        elif start_point[0] > end_point[0]:
            x_dir = -1
        if start_point[1] < end_point[1]:
            y_dir = 1
        elif start_point[1] > end_point[1]:
            y_dir = -1
        for i in range(distance):
            network[y][x] += 1
            x += x_dir
            y += y_dir
    for row in network:
        print(row)
