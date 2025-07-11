# programm to add animal data to a html template with the correct place holder
# the html template shows 13 errors in vscode, maybe you can pass it to someone who is working on those :D 
import json

def load_data(file_path):
    """ Loads JSON file """
    with open(file_path, "r") as data:
        return json.load(data)

def load_html(filepath_to_html):
    """ Loads HTML to put in the string """
    with open(filepath_to_html, "r") as html:
        return html.read()

def write_new_html(html, formatted_details):
    """ takes read html document and formatted text to replace the placeholder in html with the formatted details """
    final_html = html.replace("__REPLACE_ANIMALS_INFO__", formatted_details) # replacing place holder with formatted information
    output_path = "/home/coder/Zootopia/animals.html" # 
    with open(output_path, "w") as output_file:
        output_file.write(final_html)
    print(f"HTML file created: {output_path}")
    



def get_details(data):
    """ reads data and builds a dict for every animal and puts it in a list 'animals' """
    animals = []
    for animal in data:
        try:
            animal_info = {
                "name": animal.get("name", "Unknown"), # trying out get since not all animals have all keys, giving back "Unknown" if key is not found
                "diet": animal.get("characteristics", {}).get("diet", "Unknown"), #"appends" empty dict in first check for characteristics, if key not there (wasnt necessary)
                "location": ", ".join(animal.get("locations", ["Unknown"])), #join for nicer output and getting rid of the list brackets
                "type": animal.get("characteristics", {}).get("type", "Unknown"),
                "weight": animal.get("characteristics", {}).get("weight", "Unknown"),  # added for bonus
                "lifespan": animal.get("characteristics", {}).get("lifespan", "Unknown"),  # added for bonus
                "color": animal.get("characteristics", {}).get("color", "Unknown"),  # added for bonus
            }
            animals.append(animal_info)
        except KeyError:
            print("Test")
    return animals

def print_animal_details(details):
    """ print animal data - was part of the task so it will stay """
    for animal in details:
        for key, value in animal.items():
            print(f"{key.capitalize()}: {value}") #capitalized here since the example output was like that
        print()

def format_animal_details(details):
    """Formats data from get_details to blocks for python, lists for html """
    animal_details_string = ""
    for animal in details:
        animal_details_string += '<li class="cards__item">\n'
        animal_details_string += f'  <div class="card__title">{animal["name"]}</div>\n'
        animal_details_string += '<p class="card__text two-columns">\n' # made the class to make it in 2 columns for nice output 
        for key, value in animal.items():
           if key != "name":  # skip name since its already in the title
                animal_details_string += f'<strong>{key.capitalize()}:</strong> {value}<br/>\n' # add key, value with strong key
        animal_details_string += '  </p>\n'
        animal_details_string += '</li>\n' 
    animal_details_string = animal_details_string.rstrip()  # removed last empty line
    return animal_details_string
    #print(f"{animal_details_string}")       # testing only        

def main():
    file_path = "/home/coder/Zootopia/animals_data.json"
    filepath_to_html = "/home/coder/Zootopia/animals_template.html"
    data = load_data(file_path)
    details = get_details(data)
    formatted_details = format_animal_details(details)
    html = load_html(filepath_to_html)
    write_new_html(html, formatted_details)

main()