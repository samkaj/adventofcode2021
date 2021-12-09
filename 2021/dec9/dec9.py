def main():
    # get input
    with open("2021/dec9/input.txt") as f:
        height_map = [
            [int(c) for c in x] for x in [line.strip() for line in f.readlines()]
        ]

    l = get_low_points(height_map)
    print(sum(l))


def get_low_points(m):
    low_points = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            adjacent = []
            # edge cases
            if i != 0:
                # look above
                adjacent.append(m[i - 1][j])
            if i != len(m) - 1:
                # look below
                adjacent.append(m[i + 1][j])
            if j != 0:
                # look to the left
                adjacent.append(m[i][j - 1])
            if j != len(m[i]) - 1:
                # look to the right
                adjacent.append(m[i][j + 1])

            is_low_point = True
            # check if it is a low point
            for neighbour in adjacent:
                if m[i][j] >= neighbour:
                    is_low_point = False

            if is_low_point:
                low_points.append(m[i][j] + 1)

    return low_points


if __name__ == "__main__":
    main()
