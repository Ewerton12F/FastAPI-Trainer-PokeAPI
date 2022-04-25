from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    trainer_id: int