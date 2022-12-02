#!/usr/bin/env python3

def part_one(rounds):
    outcomes = {
        'BX': 1,
        'CY': 2,
        'AZ': 3,
        'AX': 4,
        'BY': 5,
        'CZ': 6,
        'CX': 7,
        'AY': 8,
        'BZ': 9
    }
    print(sum([outcomes[x] for x in rounds]))

def part_two(rounds):
    outcomes = {
        'AX': 3,
        'BX': 1,
        'CX': 2,
        'AY': 4,
        'BY': 5,
        'CY': 6,
        'AZ': 8,
        'BZ': 9,
        'CZ': 7
    }
    print(sum([outcomes[x] for x in rounds]))

def main():
    with open('input.txt', 'r') as f:
        rounds = [line.replace(' ','').strip() for line in f.readlines()]
    part_one(rounds)
    part_two(rounds)


if __name__ == '__main__':
    main()
