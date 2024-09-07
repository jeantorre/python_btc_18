from pydantic import BaseModel


class PokemonSchema(BaseModel):
    nome: str
    tipo: str

    class Config:
        from_atributes = True
