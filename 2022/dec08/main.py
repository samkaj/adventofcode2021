#!/usr/bin/env python3


class Tree:
    def __init__(self, height) -> None:
        self.visible = False
        self.height = height

    def check(self, neighbors):
        if self.visible:
            return
        else:
            for n in neighbors:
                if n.height >= self.height:
                    return
            self.visible = True

    def scenic_factor(self, neighbors):
        factor = 0
        for tree in neighbors:
            if tree.height < self.height:
                factor += 1
            else:
                return factor + 1
        return factor


def part_one(tree_grid):
    for row, trees in enumerate(tree_grid):
        for col, tree in enumerate(trees):
            if row == 0 or col == 0:
                tree.visible = True
            else:
                tree.check(trees[0:col])
                tree.check(trees[col+1:])
                y = [t[col] for t in tree_grid]
                tree.check(y[row-1::-1])
                tree.check(y[row+1::])
    return sum([sum([1 for tree in row if tree.visible]) for row in tree_grid])


def part_two(tree_grid):
    best = 0
    score = 1
    for row, trees in enumerate(tree_grid):
        for col, tree in enumerate(trees):
            y = [n[col] for n in tree_grid]
            score *= tree.scenic_factor(trees[0:col][::-1])  # left
            score *= tree.scenic_factor(trees[col+1:])  # right
            score *= tree.scenic_factor(y[0:row][::-1])  # up
            score *= tree.scenic_factor(y[row+1:])  # down
            if score > best:
                best = score
            score = 1
    return best


def main():
    with open('input.txt', 'r') as f:
        tree_grid = [[Tree(int(i)) for i in list(x.strip())]
                     for x in f.readlines()]

    print(f'Part one: {part_one(tree_grid)}')
    print(f'Part one: {part_two(tree_grid)}')


if __name__ == '__main__':
    main()
