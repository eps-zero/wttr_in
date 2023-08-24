import requests

url_template = "https://wttr.in/{}?nTqum&lang=ru"

london_url = url_template.format("Лондон")
sheremetyevo_url = url_template.format("Шереметьево")
cherepovec_url = url_template.format("Череповец")

london_responce = requests.get(london_url)
sheremetyevo_responce = requests.get(sheremetyevo_url)
cherepovec_responce = requests.get(cherepovec_url)

print(london_responce.text)
print(sheremetyevo_responce.text)
print(cherepovec_responce.text)