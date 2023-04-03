def gen_website_n_city(city_name):
    strings = '<a href="https://ontap.pl/bialystok/multitapy" class="btn btn-default" style="margin-bottom: 3px;"> Białystok <div class="badge">2</div>', '<a href="https://ontap.pl/bielsko-biala/multitapy" class="btn btn-default" style="margin-bottom: 3px;"> Bielsko-Biała <div class="badge">1</div>'
    for string in strings:
        if city_name in string:
            clean_line = string.replace('<a href="', "").replace('" class="btn btn-default" style="margin-bottom: 3px;"> ', "")
            print_line = clean_line.partition(city_name)
    return print_line[:-1]

print(gen_website_n_city('Białystok'))
