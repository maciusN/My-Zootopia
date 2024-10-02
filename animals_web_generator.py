import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r") as f:
    html_content = f.read()


animals_data = load_data('animals_data.json')

output = ""

for animal in animals_data:
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal['name']}</div></br>'
    output += '<p class="card__text">'
    output += f"<strong>Location:</strong> {animal['locations'][0]}</br>"
    try:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}</br>"
    except:
        pass
    output += f"<strong>Diet:</strong> {
        animal['characteristics']['diet']}</br>"
    output += '</p>'
    output += '</li>'

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as f:
    f.write(new_html_content)
