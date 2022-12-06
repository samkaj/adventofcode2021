#!/usr/bin/env python3

def is_unique(seq: str) -> bool:
    for c in seq:
        if seq.count(c) > 1:
            return False
    return True


def start_of_msg(signals: str, distinct_count: int) -> int:
    for i in range(len(signals)):
        if is_unique(signals[i:i+distinct_count]):
            return i+distinct_count


def main():
    with open('input.txt', 'r') as f:
        signals = f.readline()
    
    print(f'Part one: {start_of_msg(signals, 4)}')
    print(f'Part two: {start_of_msg(signals, 14)}')


if __name__ == '__main__':
    main()
