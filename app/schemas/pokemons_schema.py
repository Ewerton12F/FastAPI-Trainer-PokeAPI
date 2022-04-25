def PokemonSerializer(pokemon) -> dict:
    return {
        "id": str(pokemon["_id"]),
        "name": pokemon["nickname"],
        "base_experience": str(pokemon["base_experience"]),
        "height": str(pokemon["height"]),
        "is_default": pokemon["is_default"],
        "order": str(pokemon["order"]),
        "weight": str(pokemon["weight"]),
        "trainer_id": str(pokemon["trainer_id"]),
    }

def PokemonsSerializer(pokemons) -> list:
    return [PokemonSerializer(pokemon) for pokemon in pokemons]