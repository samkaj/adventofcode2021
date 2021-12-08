def main():
    # get input
    with open("2021/dec3/input.txt") as f:
        diagnostics = [line.strip() for line in f]

    print(f"Energy consumtion: {power_consumption(diagnostics)}")
    print(f"Life support rating: {life_support_rating(diagnostics)}")


def power_consumption(data) -> int:
    bin_gamma = ""
    bin_epsilon = ""

    for i in range(len(str(data[0]))):
        if sum_col(data, i) > len(data) / 2:
            # there are more ones than zeroes
            bin_gamma += "1"
            bin_epsilon += "0"
        else:
            # there are less ones that zeroes
            bin_epsilon += "1"
            bin_gamma += "0"

    return int(bin_gamma, 2) * int(bin_epsilon, 2)


def life_support_rating(data):
    oxygen = rating(data, 0, True)
    co2 = rating(data, 0, False)
    return oxygen * co2


def rating(data, position, most_common):
    # base case
    if len(data) <= 1:
        return int(data[0], 2)

    # find the most common bit
    criteria = 0
    col = sum_col(data, position)
    if most_common:
        if col >= len(data) / 2:
            criteria = 1
    else:
        if col < len(data) / 2:
            criteria = 1

    # add acceptable numbers to new_data
    new_data = []
    for number in data:
        if int(number[position]) == criteria:
            new_data.append(number)

    # repeat recursively with new_data
    return rating(new_data, (position + 1) % len(new_data[0]), most_common)


def sum_col(data, n):
    return sum([int(x[n]) for x in data])


if __name__ == "__main__":
    main()
