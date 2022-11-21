"""W pliku random_walks napisz funkcje walk_steps,
która przyjmie liczbę kroków do przejścia i zwróci pozycję na osi w której się znajdujesz.
Użyj funkcji z pliku random_step_generators żeby poruszać się krok w przód lub w tył.
Zaczynasz w pozycji 0 i przechodzisz do 1 lub -1 w pierwszym kroku i tak dalej.
W najgorszym przypadku dla wywołania walk_steps(10) znajdziesz sie w pozycji -10 a w najlepszym 10.
Odpal to 1_000_000 razy. Ile miałeś 10?
W tym samym pliku napisz funkcję walk_distance która przyjmie dystans do pokonania i zwróci ilość kroków potrzebnych
do pokonania tego dystansu z uzyciem funkcji z pliku random_step_generators."""

from random_step_generators import drawing_func

def walk_steps(how_many_steps):
    on_axis = 0
    for i in range(how_many_steps):
        on_axis += drawing_func()
    return on_axis
#print(walk_steps(10))

#def test_walk_steps(how_many_times):
#    for i in range(how_many_times):
#        print(walk_steps(10))
#test_walk_steps(1_000_000)


def walk_distance(distance):
    step_summary = 0
    all_steps_list = []
    while distance >= step_summary:
            step_summary += drawing_func ()
            all_steps_list.append(step_summary)
    return len(all_steps_list)
#print(walk_distance(100))


#def test_walk_distance(how_many_times):
#    for i in range(how_many_times):
#        print(walk_distance(10))
#test_walk_distance(10)
