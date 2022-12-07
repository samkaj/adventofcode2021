#!/usr/bin/env python3

from textwrap import indent
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f'- {self.name} (file, size={self.size})'

    def tree(self, gap):
        print(indent(self.__str__(), gap * ' '))

    def get_size(self, dir_sizes):
        return self.size

class Dir:
    def __init__(self, parent, name: str):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def __str__(self):
        return f'- {self.name} (dir)'

    def add_child(self, child):
        self.children.append(child)
        self.size += child.size

    def tree(self, gap):
        print(indent(self.__str__(), gap * ' '))
        gap += 2
        for child in self.children:
            child.tree(gap)

    def get_size(self, dir_sizes):
        tot = 0
        for child in self.children:
            tot += child.get_size(dir_sizes)
        dir_sizes.append(tot)
        return tot


class FileSystem:
    def __init__(self):
        self.root = Dir(None, '/')
        self.wd = self.root
        self.dir_sizes = []

    def add_child(self, child: Dir | File):
        self.wd.add_child(child)

    def cd(self, dir: str):
        if dir == '..':
            self.wd = self.wd.parent
            return
        for child in self.wd.children:
            if dir == child.name:
                self.wd = child
                return
        if dir != '/':
            self.add_child(Dir(self.wd, dir))

    def tree(self, gap):
        self.root.tree(gap)

    def get_size(self):
        return self.root.get_size(self.dir_sizes)



def main():
    fs = FileSystem()
    cmd = ''
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split(' ')
            if tokens[0] == '$':
                cmd = tokens[1]
            else:
                if cmd == 'ls':
                    if tokens[0] == 'dir':
                        fs.add_child(Dir(fs.wd, tokens[1]))
                    else:
                        fs.add_child(File(tokens[1], int(tokens[0])))
            if cmd == 'cd':
                fs.cd(tokens[2])

    fs.get_size()
    tot = 0
    for size in fs.dir_sizes:
        if size <= 100000:
            tot += size

    print(f'Part one: {tot}')



if __name__ == '__main__':
    main()
