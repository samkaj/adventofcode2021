from math import floor


def main():
    # get input
    with open("problems/dec7/input.txt") as f:
        starting_positions = [int(x) for x in f.readline().split(",")]

    starting_positions.sort()

    fuel = get_fuel_cost_from_median(starting_positions)
    print(f"In total (part 1): {fuel}")
    fuel = get_fuel_cost_from_avg(starting_positions)
    print(f"In total (part 2): {fuel}")


def get_fuel_cost_from_median(positions):
    median_pos = positions[int(len(positions) / 2)]
    total_fuel_cost = 0
    for crab in positions:
        # cost = total distance to the median value
        cost = abs(crab - median_pos)
        total_fuel_cost += cost
    return total_fuel_cost


def get_fuel_cost_from_avg(positions):
    avg_pos = floor(sum(positions) / len(positions))
    total_fuel_cost = 0
    for crab in positions:
        distance = abs(crab - avg_pos)
        # cost = {1 + 2 + ... + (distance - 1) + (distance)}
        cost = int(distance * (1 + distance) / 2)
        total_fuel_cost += cost
    return total_fuel_cost


if __name__ == "__main__":
    main()
