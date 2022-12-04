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

def main():
    score = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            score += get_prio(get_dupe_quad(line))
    print(score)

if __name__ == '__main__':
    main()