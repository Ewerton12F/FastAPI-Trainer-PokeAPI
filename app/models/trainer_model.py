from pydantic import BaseModel

class Trainer(BaseModel):
    nickname: str
    first_name: str
    last_name: str
    email: str
    password: str
    team: str
    pokemons_owned: int