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
    final_html = html.replace("__REPLACE_ANIMALS_INFO__", formatted_details) # replacing place holder with formatted information
    output_path = "/home/coder/Zootopia/animals.html" # 
    with open(output_path, "w") as output_file:
        output_file.write(final_html)
    print(f"HTML file created: {output_path}")
    



def get_details(data):
    animals = []
    for animal in data:
        try:
            animal_info = {
                "name": animal.get("name", "Unknown"), # trying out get since not all animals have all keys, giving back "Unknown" if key is not found
                "diet": animal.get("characteristics", {}).get("diet", "Unknown"), #"appends" empty dict in first check for characteristics, if key not there (wasnt necessary)
                "location": ", ".join(animal.get("locations", ["Unknown"])), #join for nicer output and getting rid of the list brackets
                "type": animal.get("characteristics", {}).get("type", "Unknown"),
            }
            animals.append(animal_info)
        except KeyError:
            print("Test")
    return animals

def print_animal_details(details):
    for animal in details:
        for key, value in animal.items():
            print(f"{key.capitalize()}: {value}") #capitalized here since the example output was like that
        print()

def format_animal_details(details):
    animal_details_string = ""
    for animal in details:
        for key, value in animal.items():
           animal_details_string += f"{key.capitalize()}: {value}\n" # animal details in blocks
        animal_details_string += "\n" # extra line between animals
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