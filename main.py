from random import randint

_width = 500
_height = 500


def generateRandomPoint():
    x = randint(0, _width)
    y = randint(0, _height)
    return (x, y)


def generateRandomPoints() -> list:
    return [generateRandomPoint() for _ in range(500)]

