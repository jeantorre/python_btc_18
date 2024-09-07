import requests
from pydantic import BaseModel


class PokemonSchema(BaseModel):
    nome: str
    tipo: str

    class Config:
        from_atributes = True


def capturar_pokemon(id: int) -> PokemonSchema:
    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)
    dado = response.json()
    tipo_dados = dado["types"]
    lista_tipo = []

    for tipo_informacao in tipo_dados:
        lista_tipo.append(tipo_informacao["type"]["name"])

    tipos = ", ".join(lista_tipo)
    return PokemonSchema(nome=dado["name"], tipo=tipos)


if __name__ == "__main__":
    print(capturar_pokemon(15))
    print(capturar_pokemon(22))
