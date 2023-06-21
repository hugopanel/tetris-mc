import os
import json

from main import Tetromino
from main import load, empty

L = Tetromino("L", 0, 0, 0, 0)


def load_tetrimino(file: str) -> Tetromino:
    """Charge un tetrimino depuis un fichier"""
    data = load(file)
    #todo : mettre cette fonction dans la class tetrimino
    if data:
        tetrinino = Tetromino(
            data["name"], data["rotation"], data["color"], data["x"], data["y"]
        )
        return tetrinino
    return False


L2 = load_tetrimino("save.json")

print(L2)

L.save("save.json")
