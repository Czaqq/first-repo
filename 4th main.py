from main import website

def list_of_links_wikipedia(url):
    content = website(url)
    lines = content.split("\n")
    for line in lines:
        if "https" in line:
            print_line = line.strip()
            print_index1 = print_line.find('<a href="')-9
            print_index2 = print_line.find('"')
            clean_line = print_line.startswith('https')
            if clean_line == True:
                list_of_links.append(print_line[print_index1:print_index2])
    return list_of_links

print(list_of_links_wikipedia("https://pl.wikipedia.org/wiki/Gdynia"))
