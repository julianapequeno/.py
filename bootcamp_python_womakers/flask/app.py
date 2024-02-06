from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)


@app.route('/')  # define a rota, logo na página inicial aquii
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)  # abrir a url
    data = response.read()
    dictionary = json.loads(data)

    return render_template('character.html', characters=dictionary["results"])


@app.route('/profile/<id>')  # define a rota, logo na página inicial aquii
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)  # abrir a url
    data = response.read()
    dictionary = json.loads(data)

    return render_template('profile.html', profile=dictionary)


@app.route('/lista')  # define a rota, logo na página inicial aquii
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)  # abrir a url
    characters = response.read()  # lê as informações
    dictionary = json.loads(characters)  # transformo para formato json

    # criando um json de resultados
    characters = []

    for character in dictionary["results"]:
        character = {
            'name': character["name"],
            "status": character["status"],
            "image": character["image"],
            "location": character["location"]["name"]
        }

        characters.append(character)

    return {"characters": characters}
