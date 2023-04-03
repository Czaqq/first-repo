from main import website

def counting_number_of_times(word):
    content = website("https://pl.wikipedia.org/wiki/Gdynia")
    counter = content.count(word)
    return counter

print(counting_number_of_times("Gdynia"))
