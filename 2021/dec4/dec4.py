from bingo import Bingo


def main():
    # get input
    with open("2021/dec4/input.txt") as f:
        draws = [int(n) for n in f.readline().strip().split(",")]
        boards = []
        lines = [line.strip() for line in f.readlines()[1:]]
        for line in lines:
            boards.append([int(x) for x in line.split()])
        for l in boards:
            if l == []:
                boards.remove(l)

    best_bingo = Bingo(boards[0:5], draws)
    best_bingo.play()
    for i in range(5, len(boards), 5):
        b = Bingo(boards[i : i + 5], draws)
        b.play()
        if b.get_turns() < best_bingo.get_turns():
            best_bingo = b

    worst_bingo = Bingo(boards[0:5], draws)
    worst_bingo.play()
    for i in range(5, len(boards), 5):
        b = Bingo(boards[i : i + 5], draws)
        b.play()
        if b.get_turns() > worst_bingo.get_turns():
            worst_bingo = b

    print(best_bingo.get_score())
    print(worst_bingo.get_score())


if __name__ == "__main__":
    main()
