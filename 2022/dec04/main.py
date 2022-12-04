#!/usr/bin/env python3

def fully_overlap(set1: set, set2: set) -> bool:
    return (set1.issubset(set2) or set2.issubset(set1))


def overlap(set1: set, set2: set) -> bool:
    return len(set1.intersection(set2)) > 0


def get_set(ids) -> set:
    [start, stop] = ids.split('-')
    return {x for x in range(int(start), int(stop)+1)}


def main():
    '''
    Utilizing some built-in set operations since it is comfortable.
    '''
    score1 = 0
    score2 = 0
    with open('sample.txt', 'r') as f:
        for line in f.readlines():
            l = line.split(',')
            elf1 = get_set(l[0])
            elf2 = get_set(l[1])
            if fully_overlap(elf1, elf2):
                score1 += 1
                score2 += 1
            elif overlap(elf1, elf2):
                score2 += 1

    print(f'Part one: {score1}')
    print(f'Part one: {score2}')


if __name__ == '__main__':
    main()
