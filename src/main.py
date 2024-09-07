import random
import time

from controller import adicionar_pokemon_no_banco, capturar_pokemon


def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = capturar_pokemon(pokemon_id)

        if pokemon_schema:
            print(f"Adicionado {pokemon_schema.nome} ao banco de dados")
            adicionar_pokemon_no_banco

        else:
            print(f"Não foi possível obter dados para o pokemon com ID {pokemon_id}")
        time.sleep(10)


if __name__ == "__main__":
    main()
