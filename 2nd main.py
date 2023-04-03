from main import website

def list_of_links(url):
    content = website(url)
    lines = content.split("\n")
    list_of_links = []
    for line in lines:
        if "https" in line:
            print_line = line.strip().replace('<a href="', "")
            print_index = print_line.find('"')
            clean_line = print_line.startswith('https')
            if clean_line == True:
                list_of_links.append(print_line[0:print_index])
    return list_of_links

print(list_of_links("https://ontap.pl"))
