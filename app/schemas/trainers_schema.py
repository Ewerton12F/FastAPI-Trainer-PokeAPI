def TrainerSerializer(trainer) -> dict:
    return {
        "id": str(trainer["_id"]),
        "nickname": trainer["nickname"],
        "first_name": trainer["first_name"],
        "last_name": trainer["last_name"],
        "email": trainer["email"],
        "password": str(trainer["password"]),
        "team": trainer["team"],
        "pokemons_owned": str(trainer["pokemons_owned"]),
    }

def TrainersSerializer(trainers) -> list:
    return [TrainerSerializer(trainer) for trainer in trainers]