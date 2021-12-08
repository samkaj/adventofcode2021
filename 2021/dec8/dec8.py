def main():
    # get input
    with open("problems/dec8/input.txt") as f:
        # entries[i][0] = signal pattern
        # entries[i][1] = output signal
        entries = [x.strip().split(' | ') for x in f.readlines()]

    outputs = [entry[1] for entry in entries]
    uniques = 0
    for output in outputs:
        for signal in output.split():
            if is_easy_digit(signal):
                uniques += 1
    print(uniques)

def is_easy_digit(digit):
    digit_len = len(digit)
    return digit_len == 2 or digit_len == 3 or digit_len == 4 or digit_len == 7


if __name__ == "__main__":
    main()
