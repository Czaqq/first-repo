"""W pliku simulations zaimportuj obie funkcje z pliku random_walks.
Napisz funkcję simulate_drunk_walks_distance która przyjmie ilość spacerów
z  wykorzystaniem walk_distance i zwróci najmniejszą ilość kroków.
W  kolejnej funkcji simulate_drunk_walks_steps która przyjmie ilość spacerów z walk_steps i ilość kroków.
Gdzie najdalej udało się dojść podczas 10_000 spacerów o długości 10_000 kroków?"""

from random_walks import walk_steps, walk_distance

def simulate_drunk_walks_distance(how_many_walks, distance):
    step_rate = []
    for x in range(how_many_walks):
        step_rate.append(walk_distance(distance))
    return min(step_rate)
print(simulate_drunk_walks_distance(100, 10))

def simulate_drunk_walks_steps(how_many_walks, how_many_steps):
    step_rate = []
    for x in range(how_many_walks):
        step_rate.append(walk_steps(how_many_steps))
    return max(step_rate)
print(simulate_drunk_walks_steps(10_000, 10_000))
