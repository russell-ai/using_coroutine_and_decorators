"""This program has two function one is couroutine and the other is decorator.
    It produce the power of given number"""
import math


def coroutine(gfn):
    def inner(*args, **kwargs):
        gen = gfn(*args, **kwargs)
        next(gen)
        return gen
    return inner


@coroutine
def power(p):
    result = None
    while True:
        received = yield result
        result = math.pow(received, p)


if __name__ == "__main__":
    squares = power(2)
    cubes = power(3)
    quadro = power(4)

    print(squares.send(4))
    print(cubes.send(4))
    print(quadro.send(4))
