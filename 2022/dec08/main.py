#!/usr/bin/env python3    


class Tree:
    def __init__(self, height) -> None:
        self.visible = False
        self.height = height

    def __str__(self) -> str:
        return f"{self.height}"

    def check(self, neighbors):
        if self.visible:
            return
        elif len(neighbors) == 0:
            print('hello')
            self.visible = True
        else:
            for n in neighbors:
                if n.height >= self.height:
                    return
            self.visible = True
    

def main():
    with open('input.txt', 'r') as f:
        tree_grid = [[Tree(int(i)) for i in list(x.strip())] for x in f.readlines()]

    for j, trees in enumerate(tree_grid):
        for i, tree in enumerate(trees):
            if j == 0 or i == 0:
                tree.visible = True
            else:
                tree.check(trees[0:i])
                tree.check(trees[i+1:])
                y = [t[i] for t in tree_grid]
                tree.check(y[j-1::-1])
                tree.check(y[j+1::])  
    
    tot = 0
    for row in tree_grid:
        for tree in row:
            if tree.visible:
                tot += 1
                print(f'', end=' ')
            else:
                print(f' ', end=' ')
        print()
    
    print(f'Part one: {tot}')


if __name__ == '__main__':
    main()