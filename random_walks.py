"""W pliku random_walks napisz funkcje walk_steps,
która przyjmie liczbę kroków do przejścia i zwróci pozycję na osi w której się znajdujesz.
Użyj funkcji z pliku random_step_generators żeby poruszać się krok w przód lub w tył.
Zaczynasz w pozycji 0 i przechodzisz do 1 lub -1 w pierwszym kroku i tak dalej.
W najgorszym przypadku dla wywołania walk_steps(10) znajdziesz sie w pozycji -10 a w najlepszym 10.
Odpal to 1_000_000 razy. Ile miałeś 10?
W tym samym pliku napisz funkcję walk_distance która przyjmie dystans do pokonania i zwróci ilość kroków potrzebnych
do pokonania tego dystansu z uzyciem funkcji z pliku random_step_generators."""

from collections import Counter
from random_step_generators import drawing_func

def walk_steps(how_many_steps):
    steps_register = []
    x = 0
    while x < 1_000_000:
        steps_register.append(sum(drawing_func(how_many_steps)))
        x += 1
    return steps_register
# 10: na 1_000_000 było ok 900 i w górę


def walk_distance(distance_meters):
    step_summmary = 0
    while distance_meters >= step_summmary:
        steps_to_walk_distance = len(str(drawing_func(distance_meters)))
        step_summmary += steps_to_walk_distance
    return step_summmary
# ok 350 kroków do zrobienia na dystansie 100

print(Counter(walk_steps(10)))
print("")
print(walk_distance(1))