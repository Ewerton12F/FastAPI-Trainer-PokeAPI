from bson import ObjectId
from fastapi import APIRouter

from ..config.database import collection_name

from ..models.trainer_model import Trainer
from ..models.pokemon_model import Pokemon

from ..schemas.trainers_schema import TrainersSerializer
from ..schemas.pokemons_schema import PokemonsSerializer

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "Hello World"}

# RETRIEVE ---------------------------------------------------------------------
# ALL
@api_router.get("/trainer/")
async def get_trainers():
    trainers = TrainersSerializer(collection_name.find())
    return trainers
# BY ID
@api_router.get("/trainer/{id}/")
async def get_trainer(id: str):
    return TrainersSerializer(collection_name.find_one({"_id": ObjectId(id)}))
# RETRIEVE /

# POST -------------------------------------------------------------------------
@api_router.post("/trainer/")
async def create_trainer(trainer: Trainer):
    _id = collection_name.insert_one(dict(trainer))
    return TrainersSerializer(collection_name.find({"_id": _id.inserted_id}))
# POST /

# UPDATE -----------------------------------------------------------------------
@api_router.put("/trainer/{id}")
async def update_trainer(id: str, trainer: Trainer):
    collection_name.find_one_and_update({
        "_id": ObjectId(id)}, {
        "$set": dict(trainer)
    })
    return TrainersSerializer(collection_name.find({"_id": ObjectId(id)}))
# UPDATE /

# DELETE -----------------------------------------------------------------------
@api_router.delete("/trainer/{id}")
async def delete_trainer(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
# DELETE /

