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
                "skin_type": animal.get("characteristics", {}).get("skin_type", "Unknown"),  # i only realized the underline at the end.. And i dont know how to remove them quickly everywhere :( 
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
    """Formats data from get_details to HTML list items"""
    animal_details_string = ""
    for animal in details:
        animal_details_string += '<li class="cards__item">\n'
        animal_details_string += f'  <div class="card__title">{animal["name"]}</div>\n'
        animal_details_string += '  <div class="card__text">\n'
        animal_details_string += '    <ul class="card__details">\n'
        for key, value in animal.items():
            if key != "name":
                animal_details_string += f'      <li class="card__detail-item"><strong>{key.capitalize()}:</strong> {value}</li>\n'
        animal_details_string += '    </ul>\n'
        animal_details_string += '  </div>\n'
        animal_details_string += '</li>\n'
    return animal_details_string.rstrip()       

def get_user_input(formatted_details, data, details, html):
    print_menu()
    while True:
        
        choice = input("What do you wanna do? ")
        if choice == "q":
            return
        try:
            choice = int(choice)
            if choice == 1:
                filtered_animals = filter_animals_by_skin_type(details)
                if filtered_animals:
                    formatted_filtered = format_animal_details(filtered_animals)  # ← Neu: Formatierung
                    write_new_html(html, formatted_filtered)
                else:
                    print("Error parsing skin types, seems to be empty")
            elif choice == 2:
                write_new_html(html, formatted_details) 
            else:
                print("invalid input. Choose 1, 2 or q")
        except ValueError:
            print("Please enter a number or 'q'")

def print_menu():
    """ prints menu options """
    print("\n" + "="*50)
    print("ZOOTOPIA ANIMAL DATABASE")
    print("="*50)
    print("1 - Filter animals by skin type")
    print("2 - Show all animals and create HTML")
    print("q - Quit")
    print("="*50)

def get_skin_type_input():
    skintype = input("Type in skin type\n >>")
    return skintype

def get_available_skin_types(details):
    skin_types = set()
    for animal in details:
        skin_type = animal.get("skin_type", "Unknown")
        if skin_type:  # optional: ignoriere leere Strings
            skin_types.add(skin_type)
    return sorted(skin_types)

def filter_animals_by_skin_type(data, formatted_data, skintype="Unknown"):
    found_animals = []
    skintype = get_skin_type_to_search_input()
    for animal in details:
        for key, values in aninimal.items():
            try:
                animal_info = {
                    "name": animal.get("name", "Unknown"), # trying out get since not all animals have all keys, giving back "Unknown" if key is not found
                    "diet": animal.get("characteristics", {}).get("diet", "Unknown"), #"appends" empty dict in first check for characteristics, if key not there (wasnt necessary)
                    "location": ", ".join(animal.get("locations", ["Unknown"])), #join for nicer output and getting rid of the list brackets
                    "type": animal.get("characteristics", {}).get("type", "Unknown"),
                    "weight": animal.get("characteristics", {}).get("weight", "Unknown"),  # added for bonus
                    "lifespan": animal.get("characteristics", {}).get("lifespan", "Unknown"),  # added for bonus
                    "skin_type": animal.get("characteristics", {}).get("skin_type", "Unknown"),  # added for bonus
                }
                animals.append(animal_info)
            except KeyError:
                print("Test")

def filter_animals_by_skin_type(details):
    skin_types = get_available_skin_types(details)
    
    print("\nAvailable skin types:")
    for i, s in enumerate(skin_types, 1): # enumerate for nice and easy listing
        print(f"{i}. {s}")

    user_input = input("\nPlease enter a number (1-{}) or skin type name: ".format(len(skin_types))).strip()
    
    # check if input is a number
    try:
        choice_num = int(user_input)
        if 1 <= choice_num <= len(skin_types):
            selected = skin_types[choice_num - 1]  # convert number to actual skin type name
        else:
            print(f"Please enter a number between 1 and {len(skin_types)}")
            return []
    except ValueError:
        # if input not a number, its probably the written word, so i handle it like that
        selected = user_input

    filtered_animals = [a for a in details if a.get("skin_type", "Unknown").lower() == selected.lower()]

    if not filtered_animals:
        print(f" No animals found with skin type '{selected}'.")
    else:
        print(f"✅ Found {len(filtered_animals)} animals with skin type '{selected}':")
        for animal in filtered_animals:
            print(f"  - {animal['name']}")

    return filtered_animals

def main():
    file_path = "/home/coder/Zootopia/animals_data.json"
    filepath_to_html = "/home/coder/Zootopia/animals_template.html"

    try:
        data = load_data(file_path)
        details = get_details(data)
        formatted_details = format_animal_details(details)
        html = load_html(filepath_to_html)
        
        print(f"Loaded {len(details)} animals from database.")
        
        get_user_input(formatted_details, data, details, html)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    
main()