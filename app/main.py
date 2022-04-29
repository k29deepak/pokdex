from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

def fetch_pokemon_data(name):
    # resp = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name}").json

    resp = pokemon_db().get(name)


    if not resp:
        raise HTTPException(status_code=404,
                            detail=f"Pokemon with name {name} not invented yet. Please try searching other pokemon.")

    #subset response to get desired values
    habitat = resp.get("habitat")
    habitat = habitat if isinstance(habitat, str) else habitat.get("name")

    #fetch description
    description = ''
    for txt in resp['flavor_text_entries']:
        if txt.get('language').get('name') == 'en':
            description = txt.get('flavor_text')
            break

    new_response = {"name": name,
                    "description": description,
                    "habitat": habitat,
                    "isLegendary": resp.get("is_legendary")}
    return new_response


def pokemon_db():
    return json.load(open('poke_db.json'))


@app.get("/pokemon/{name}")
async def get_pokemon(name):
    response = fetch_pokemon_data(name)
    return response

@app.get("/pokemon/translated/{name}")
async def get_translated_pokemon(name):
    response = fetch_pokemon_data(name)
    if response['isLegendary'] or response['habitat'] == 'cave':
        description = response['description'].replace(' ',"_")
    else:
        description = response['description'].replace(' ',"-")

    response['description'] = description

    return response
