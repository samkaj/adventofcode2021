#!/usr/bin/env python3


def get_prio(s: str) -> int:
    '''
    Gets the prio score by using ASCII values so we don't need O(N)
    or a boring dictionary for point lookup :)

    ord('A') = 65 and A should give 27 points
    ord('a') = 97 and a should give 1 point
    '''
    is_upper = s.capitalize() == s
    if is_upper:
        prio = ord(s) - 64 + 26
    else:
        prio = ord(s) - 96
    return prio

def get_dupe_quad(line: str) -> str:
    '''
    Standard lookup with in keyword is linear, and if we naively
    use in for each char until the dupe is found would be O(N^2), which
    we can do better...
    '''
    bags = [line[:int(len(line)/2)], line[int(len(line)/2)::]]
    for c in bags[0]:
        if c in bags[1]:
            return c
    return ''

def get_group(lines: list()) -> int:
    '''
    Part two.
    I'm tired and hungover, we'll make it O(N^3)...
    '''
    for line in lines:
        line = line[:-2] # remove newline
        for c in line:
            if c in lines[1] and c in lines[2]:
                return get_prio(c)
    return 0

def main():
    score1 = 0
    score2 = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            score1 += get_prio(get_dupe_quad(line))
            if i % 3 == 0:
                score2 += get_group(lines[i:i+3])
                
    print(f'Part one: {score1}')
    print(f'Part two: {score2}')

if __name__ == '__main__':
    main()