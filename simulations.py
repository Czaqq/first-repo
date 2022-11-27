from random_walks import walk_steps, walk_distance

def simulate_drunk_walks_distance(how_many_walks, distance):
    step_rate = []
    for x in range(how_many_walks):
        step_rate.append(walk_distance(distance))
    return min(step_rate)

def simulate_drunk_walks_steps(how_many_walks, how_many_steps):
    step_rate = []
    for x in range(how_many_walks):
        step_rate.append(walk_steps(how_many_steps))
    return max(step_rate)
