"""W pliku random_step_generators napisz funkcję która używając modułu random wylosuje 1 lub -1
z prawdopodobieństwem 0.5.
Wymysl dobrą nazwę.
Jak sprawdzisz że faktycznie jest 50% 1 i 50% -1?"""

import random
from collections import Counter

def drawing_func(how_many_draws):
    step_list = [1, -1]
    steps_draw_list = []
    for i in range(how_many_draws):
        steps_draw_list.append(random.choice(step_list))
#użyłem random.choice (nie choices), gdyż ta funkcja domyślnie rodzieliła po równo prawdopodobieństwo na ilość elementów, w tym wypadku 2 elementy czyli 50/50 na każdy element
    return steps_draw_list

#print(Counter(drawing_func(200)))
