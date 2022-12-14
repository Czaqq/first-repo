import random

def drawing_func():
    x = random.choice([-1, 1])
    return x

def drawing_func_x_and_y():
    x = random.choice([-1, 1])
    y = random.choice([-1, 1])
    return x, y

def drawing_func_x_or_y_move():
    x = random.choice([-1, 1])
    y = random.choice([-1, 1])
    return random.choice([x, y])
