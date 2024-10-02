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
    output += f"Name: {animal['name']}</br>"
    output += f"Diet: {animal['characteristics']['diet']}</br>"
    output += f"Location: {animal['locations'][0]}</br>"
    try:
      output += f"Type: {animal['characteristics']['type']}</br>"
    except:
      pass
    output += '</li>'

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as f:
  f.write(new_html_content)