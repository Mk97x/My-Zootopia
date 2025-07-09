import json

def load_data(file_path):
    """ Loads JSON file """
    with open(file_path, "r") as data:
        return json.load(data)

def get_details(data):
    animals = []
    for animal in data:
        try:
            animal_info = {
                "name": animal.get("name", "Unknown"), # trying out get since not all animals have all keys 
                "diet": animal.get("characteristics", {}).get("diet", "Unknown"), #"appends" empty dict in first check for characteristics, if key not there (wasnt necessary)
                "location": animal.get("locations", "Unknown"),
                "type": animal.get("characteristics", {}).get("type", "Unknown"),
            }
            animals.append(animal_info)
        except KeyError:
            print("Test")
    return animals

def print_animal_details(details):
    for animal in details:
        for key, value in animal.items():
            print(f"{key}: {value}")
        print()
        

def main():
    file_path = "/home/coder/Zootopia/animals_data.json"
    data = load_data(file_path)
    details = get_details(data)
    print_animal_details(details)

main()