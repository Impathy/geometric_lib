import circle
import square
import rectangle
import triangle

figs = ['circle', 'square', 'rectangle', 'triangle']
funcs = ['squareArea', 'squarePerimeter', 'circleArea', 'circlePerimeter',
    'rectangleArea', 'rectanglePerimeter', 'triangleArea', 'trianglePerimeter']
sizes = {}


def calc(fig, func, size):


<< << << < HEAD
   if not (fig in figs):
        raise not_a_fig
    if not (func in funcs):
        raise not_a_func
    if not (all([type(x) == int for x in size])):
        raise not_an_int

        return eval(f'{fig}.{func}(*{size})')

== =====
   if not(fig in figs):
        raise ValueError
    if not (func in funcs):
        raise ValueError
    if not (all([type(x) == int for x in size])):
        raise ValueError
    return eval(f'{fig}.{func}(*{size})')
>>>>>> > e909d1f3642b7e19bedc42439c764c07689ee57e

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)
