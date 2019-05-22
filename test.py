from random import randint

_width = 500
_height = 500


def generateRandomPoint():
    x = randint(_width)
    y = randint(_height)
    return (x, y)


def generateRandomPoints() -> list:
    return [generateRandomPoint() for _ in range(500)]


if __name__ == "__main__":
    print(generateRandomPoints())
