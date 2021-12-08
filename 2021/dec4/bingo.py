class Bingo:
    def __init__(self, playing_board, draws) -> None:
        self.draw_index = 0
        self.board = [[Tile(tile) for tile in row] for row in playing_board]
        self.draws = draws

    def play(self):
        for _ in self.draws:
            self.make_draw()
            if self.is_bingo():
                return (self.get_score(), self.draw_index)

    def get_score(self):
        return self.sum_of_unmarked() * self.draws[self.draw_index - 1]

    def get_turns(self):
        return self.draw_index

    def sum_of_unmarked(self):
        s = 0
        for row in self.board:
            for tile in row:
                if not tile.get_marked():
                    s += tile.get_number()
        return s

    def make_draw(self):
        draw = self.draws[self.draw_index]
        self.mark_board(draw)
        self.draw_index += 1

    def mark_board(self, n):
        for row in self.board:
            for tile in row:
                if tile.get_number() == n:
                    tile.mark()
                    break

    def is_bingo(self):
        for i in range(len(self.board)):
            bingo = True
            for row in self.board:
                if not row[i].get_marked():
                    bingo = False
                    break
            if bingo:
                return True

        for row in self.board:
            bingo = True
            for tile in row:
                if not tile.get_marked():
                    bingo = False
                    break
            if bingo:
                return True

        return False


class Tile:
    def __init__(self, n) -> None:
        self.n = n
        self.marked = False

    def mark(self):
        self.marked = True

    def get_marked(self):
        return self.marked

    def get_number(self):
        return self.n
