def main():
    # get input
    with open("problems/dec5/input.txt") as f:
        vectors = []
        for line in f.readlines():
            vectors.append(create_vector_from_string(line))

    # part 1
    grid1 = get_grid(vectors)
    mark_grid(grid1, vectors, False)
    print(
        f"Horizontally and vertically - dangerous overlaps: {count_dangerous_overlaps(grid1)}"
    )
    # part 2
    grid2 = get_grid(vectors)
    mark_grid(grid2, vectors, True)
    print(
        f"Diagonally, horizontally and vertically - dangerous overlaps: {count_dangerous_overlaps(grid2)}"
    )


def create_vector_from_string(input_string: str):
    # 409,872 -> 409,963 becomes [[409, 872], [409, 963]]
    return [
        [int(n) for n in vector_string.split(",")]
        for vector_string in input_string.split(" -> ")
    ]


def get_grid(vectors):
    w = 0
    h = 0
    for vector_pair in vectors:
        for vector in vector_pair:
            if vector[0] > w:
                w = vector[0]
            if vector[1] > h:
                h = vector[1]

    grid = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    return grid


def mark_grid(grid, vectors, diagonally):
    # marks the grid horizontally and vertically
    for v in vectors:
        start = v[0]
        x0 = start[0]
        y0 = start[1]
        end = v[1]
        x1 = end[0]
        y1 = end[1]
        if start[0] == end[0]:
            # x is the same
            for y in range(min(y0, y1), max(y0, y1) + 1):
                grid[y][x0] += 1

        elif start[1] == end[1]:
            # y is the same
            for x in range(min(x0, x1), max(x0, x1) + 1):
                grid[y0][x] += 1

        elif diagonally:
            # down right
            if y0 < y1 and x0 < x1:
                x = x0
                for y in range(y0, y1 + 1):
                    grid[y][x] += 1
                    x += 1
            # down left
            elif y0 < y1 and x0 > x1:
                x = x0
                for y in range(y0, y1 + 1):
                    grid[y][x] += 1
                    x -= 1
            # up right
            elif y0 > y1 and x0 < x1:
                x = x0
                for y in range(y0, y1 - 1, -1):
                    grid[y][x] += 1
                    x += 1
            # up left
            elif y0 > y1 and x0 > x1:
                x = x0
                for y in range(y0, y1 - 1, -1):
                    grid[y][x] += 1
                    x -= 1


def count_dangerous_overlaps(grid):
    return sum([1 for row in grid for number in row if number > 1])


if __name__ == "__main__":
    main()
