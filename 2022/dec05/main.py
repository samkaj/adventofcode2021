#!/usr/bin/env python3

def main():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    crates = []
    instructions = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if line.strip().startswith('['):
                crates.append(line.replace('\n',''))
            elif line.startswith('move'):
                instructions.append(line.strip())

    pos = lambda i: int((i-1)/4) # yes
    stack9000 = Stack(9, True)
    stack9001 = Stack(9, False)
    for line in crates:
        for i, c in enumerate(line):
            if c in letters:
                stack9000.add(c, pos(i))
                stack9001.add(c, pos(i))

    for i in instructions:
        stack9000.move(i)
        stack9001.move(i)
    
    for s in stack9000:
        print(s[-1], end='')
    print()
    for s in stack9001:
        print(s[-1], end='')
    print()


class Stack:
    def __init__(self, stacks: int, is9000: bool) -> None:
        self.crates = [[] for _ in range(stacks)]
        self.is9000 = is9000
    
    def add(self, crate, pos: int):
        self.crates[pos].insert(0, crate)

    def move(self, instruction: str):
        instruction_list = instruction.split(' ')
        amount = int(instruction_list[1])
        frm = int(instruction_list[3]) - 1
        to = int(instruction_list[5]) - 1
        moving_crates = [self.crates[frm].pop() for _ in range(amount)]
        if self.is9000:
            # reversing the order is the same as taking all at once
            moving_crates.reverse() 

        # place the crate on top of the one already there
        start = len(self.crates[to])
        for crate in moving_crates:
            self.crates[to].insert(start,crate)

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.crates):
            x = self.i
            self.i += 1
            return self.crates[x]
        raise StopIteration


if __name__ == '__main__':
    main()