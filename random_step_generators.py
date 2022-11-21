"""W pliku random_step_generators napisz funkcję która używając modułu random wylosuje 1 lub -1
z prawdopodobieństwem 0.5.
Wymysl dobrą nazwę.
Jak sprawdzisz że faktycznie jest 50% 1 i 50% -1?"""

import random

def drawing_func():
    return random.choice([-1, 1])
#print(drawing_func())

#def test_drawing_func(how_many_times):
#    for i in range(how_many_times):
#        print(drawing_func())
#test_drawing_func(1000)
