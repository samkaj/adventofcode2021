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

def main():
    with open('input.txt', 'r') as f:
        rounds = [line.replace(' ','').strip() for line in f.readlines()]
    part_one(rounds)


if __name__ == '__main__':
    main()
