def main():
    # get input
    with open("problems/dec7/input.txt") as f:
        starting_positions = [int(x) for x in f.readline().split(",")]

    starting_positions.sort()
    mid = int(len(starting_positions) / 2)
    # Get from minimum median if there are two
    fuel = min(
        get_fuel_cost(starting_positions, starting_positions[mid]),
        get_fuel_cost(starting_positions, starting_positions[mid - 1]),
    )
    print(f"In total: {fuel}")


def get_fuel_cost(positions, pos):
    fuel = 0
    for crab in positions:
        cost = abs(crab - pos)
        fuel += cost
    return fuel


if __name__ == "__main__":
    main()
