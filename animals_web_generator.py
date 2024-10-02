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
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics']['diet']}\n"
    output += f"Location: {animal['locations'][0]}\n"
    try:
      output += f"Type: {animal['characteristics']['type']}\n\n"
    except:
      pass

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as f:
  f.write(new_html_content)