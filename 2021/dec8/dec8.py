def main():
    # get input
    with open("2021/dec8/input.txt") as f:
        # entries[i][0] = signal pattern
        # entries[i][1] = output signal
        entries = [x.strip().split(" | ") for x in f.readlines()]

    outputs = [entry[1] for entry in entries]
    uniques = 0
    for output in outputs:
        for signal in output.split():
            if is_easy_digit(signal):
                uniques += 1
    
    total = sum([get_7seg(entry) for entry in entries])
    print(total)


def is_easy_digit(digit):
    digit_len = len(digit)
    return digit_len == 2 or digit_len == 3 or digit_len == 4 or digit_len == 7


def get_easy_digit(digit):
    digit_len = len(digit)
    if digit_len == 2:
        return 1
    elif digit_len == 3:
        return 7
    elif digit_len == 4:
        return 4
    elif digit_len == 7:
        return 8


def get_7seg(entry):
    pattern = entry[0]
    output = entry[1]
    positions = {}
    _7seg = {}
    # get uniques
    for digit in pattern.split():
        if is_easy_digit(digit):
            _7seg[get_easy_digit(digit)] = digit

    # get a (subtract 7 from 1, remainder is a)
    positions["a"] = subtract_patterns(_7seg[1], _7seg[7])

    # get c and f
    c_f = get_common_digits(_7seg[1], _7seg[7])

    # determine what 6 is and set c and f exactly
    six_length_digits = get_digits_from_len(pattern, 6)
    seven = _7seg[7]
    for digit in six_length_digits:
        maybe_c = subtract_patterns(digit, _7seg[8])
        if maybe_c in seven:
            # if remainder is in 7, its 6.
            # now we know c, which also gives f
            positions["c"] = maybe_c
            positions["f"] = subtract_patterns(maybe_c, c_f)
            _7seg[6] = digit
            break

    # determine d and e approximately
    six_length_digits.remove(_7seg[6])
    d_e = subtract_patterns(six_length_digits.pop(), six_length_digits.pop())

    # determine g
    # remove 7 + (d_e) from 3, we should get one remaining
    d_e_7 = [combine_patterns(d_e[0], _7seg[7]), combine_patterns(d_e[1], _7seg[7])]
    five_length_digits = get_digits_from_len(pattern, 5)
    for combo in d_e_7:
        for digit in five_length_digits:
            remainder = subtract_patterns(combo, digit)
            if len(remainder) == 1:
                positions["g"] = remainder
                _7seg[3] = digit
                break
    # determine d
    # 7 - 3 - pos[g] = d
    d_g = subtract_patterns(_7seg[7], _7seg[3])
    positions["d"] = subtract_patterns(d_g, positions["g"])

    # determine e: 6 - 3 - c - 4 - f - d
    d = subtract_patterns(_7seg[6], _7seg[3])  # c b e
    cbe_4 = combine_patterns(d, _7seg[4])
    positions["e"] = subtract_patterns(cbe_4, _7seg[4])

    # determine b
    known = ""
    for p in positions:
        known += positions[p]

    # remove all known from 8 and get the remaining
    positions["b"] = subtract_patterns(known, _7seg[8])

    # add remaining to _7seg (0, 2, 5, 9)
    _7seg[0] = (
        positions["a"]
        + positions["b"]
        + positions["c"]
        + positions["e"]
        + positions["f"]
        + positions["g"]
    )
    _7seg[2] = (
        positions["a"]
        + positions["c"]
        + positions["d"]
        + positions["e"]
        + positions["g"]
    )
    _7seg[5] = (
        positions["a"]
        + positions["b"]
        + positions["d"]
        + positions["f"]
        + positions["g"]
    )
    _7seg[9] = (
        positions["a"]
        + positions["b"]
        + positions["c"]
        + positions["d"]
        + positions["f"]
        + positions["g"]
    )

    # sort the 7segs alphabetically
    for i in range(10):
        _7seg[i] = ''.join(sorted(_7seg[i]))
    
    sorted_output = []
    for digit in output.split():
        sorted_output.append(''.join(sorted(digit)))
    
    answer = []
    for digit in sorted_output:
        for i in range(10):
            if digit == _7seg[i]:
                answer.append(str(i))
                break

    return int(''.join(answer))

def combine_patterns(d1, d2):
    pattern = d1
    for c in d2:
        if c not in pattern:
            pattern += c
    return pattern


def subtract_patterns(d1, d2):
    remainder = ""
    for c in d2:
        if c not in d1:
            remainder += c
    for c in d1:
        if c not in d2:
            remainder += c
    return remainder


def get_common_digits(d1, d2):
    commons = []
    for c in d1:
        if c in d2:
            commons.append(c)
    return commons


def swap(s1, s2):
    tmp = s1
    s1 = s2
    s2 = tmp


def get_digits_from_len(digits, length):
    new_digits = []
    for digit in digits.split():
        if len(digit) == length:
            new_digits.append(digit)
    return new_digits


if __name__ == "__main__":
    main()
