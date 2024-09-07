import requests

from db import Base, SessionLocal, engine
from models import Pokemon
from schema import PokemonSchema

Base.metadata.create_all(bind=engine)


def capturar_pokemon(pokemon_id: int) -> PokemonSchema:
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(URL)
    if response.status_code == 200:
        dado = response.json()
        tipo_dados = dado["types"]
        lista_tipo = []

        for tipo_informacao in tipo_dados:
            lista_tipo.append(tipo_informacao["type"]["name"])

        tipos = ", ".join(lista_tipo)
        return PokemonSchema(nome=dado["name"], tipo=tipos)

    else:
        return None


def adicionar_pokemon_no_banco(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(nome=pokemon_schema.nome, tipo=pokemon_schema.tipo)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db.pokemon)

    return db_pokemon
