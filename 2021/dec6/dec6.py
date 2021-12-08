import time

def main():
    # get input
    with open("problems/dec6/input.txt") as f:
        population = [int(x) for x in f.readline().split(",")]
    start = time.perf_counter()
    spawn_queue = [0] * 9
    for i in population:
        spawn_queue[i] += 1
    pass_time(spawn_queue, 256)
    end = time.perf_counter()
    print('The program completed in %.7f s' % (end-start))



def pass_time(spawn_queue, days):
    for _ in range(days):
        # This handles the general breeding circle of the population
        new_queue = spawn_queue.copy()
        for i in range(1, 7):
            new_queue[i-1] = spawn_queue[i]
        new_queue[6] = spawn_queue[0]
        spawn_queue = new_queue.copy()
    
        # Count new spawns
        new_spawns = spawn_queue[6]

        # Move newly spawned and add brand new spawns
        spawn_queue[6] += spawn_queue[7]
        spawn_queue[7] = spawn_queue[8]
        spawn_queue[8] = new_spawns

    print(f'Population after {days} days: {sum(spawn_queue)}')


if __name__ == "__main__":
    main()
