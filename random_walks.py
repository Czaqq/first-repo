from random_step_generators import drawing_func

def walk_steps(how_many_steps):
    on_axis = 0
    for i in range(how_many_steps):
        on_axis += drawing_func()
    return on_axis


def walk_distance(distance):
    step_summary = 0
    all_steps_list = []
    while distance >= step_summary:
            step_summary += drawing_func ()
            all_steps_list.append(step_summary)
    return len(all_steps_list)
