def main():
    # get input
    with open("2021/dec9/input.txt") as f:
        height_map = [
            [int(c) for c in x] for x in [line.strip() for line in f.readlines()]
        ]

    print(f"Low points sum: {low_point_sum(height_map)}")
    print(f"Three largest basins product: {basin_product(height_map)}")

    # too low: 336

def low_point_sum(m):
    return sum(get_low_points(m)[0])


def get_low_points(m):
    low_points = []
    coords = []
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
                coords.append([i, j])

    return low_points, coords


def basin_product(grid):
    lows = get_low_points(grid)[1]
    # replace every pos != 9 with 0
    m = grid.copy()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 9:
                m[i][j] = 0

    # fill the different basins with a unique integer
    for i in range(len(lows)):
        fill_basin(m, lows[i][0], lows[i][1], 0, i)

    # fill a dictionary with the unique integers and count occurences
    basins = {i: 0 for i in range(len(lows))}
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 9:
                basins[m[i][j]] += 1

    # append the key values in the dictionary to basin sizes
    basin_sizes = []
    for b in basins:
        basin_sizes.append(basins[b])


    # multiply the three largest together
    largest_multiplier = 1
    basin_sizes.sort() # sort so we simply can use the three last values
    l = len(basin_sizes)
    for i in basin_sizes[l-3:l]:
        largest_multiplier *= i

    return largest_multiplier


def fill_basin(m, x, y, prev_val, new_val):
    row = len(m)
    col = len(m[0])
    # base cases
    if (
        x < 0
        or x >= row
        or y < 0
        or y >= col
        or m[x][y] != prev_val
        or m[x][y] == new_val
    ):
        return

    m[x][y] = new_val

    # Fill recursively in all directions
    fill_basin(m, x + 1, y, prev_val, new_val)
    fill_basin(m, x - 1, y, prev_val, new_val)
    fill_basin(m, x, y + 1, prev_val, new_val)
    fill_basin(m, x, y - 1, prev_val, new_val)


if __name__ == "__main__":
    main()
