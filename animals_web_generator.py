import json


def load_data(file_path):
    """
    Loads a JSON file from the given file path.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data as a dictionary.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serializes an animal dictionary into an HTML string.

    Args:
        animal (dict): The animal data.

    Returns:
        str: The serialized HTML string for the animal.
    """
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div></br>'
    output += '<p class="card__text">'
    output += f"<strong>Location:</strong> {animal_obj['locations'][0]}</br>"
    try:
        output += f"<strong>Type:</strong> {
            animal_obj['characteristics']['type']}</br>"
    except:
        pass
    output += f"<strong>Diet:</strong> {
        animal_obj['characteristics']['diet']}</br>"
    output += '</p>'
    output += '</li>'
    return output


def main():
    """
    Main function to generate the animals HTML file.
    It reads the template HTML, loads the animals data,
    serializes each animal's information, and writes the
    updated content to a new HTML file.
    """
    with open("animals_template.html", "r") as f:
        html_content = f.read()

    animals_data = load_data('animals_data.json')
    output = ""

    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(new_html_content)


if __name__ == "__main__":
    main()
