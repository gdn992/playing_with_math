class Vertex:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


def lagrange_interpolation(vertex_list: list[Vertex]):
    sub_polinom_list: list[function] = []

    for vertex in vertex_list:
        sub_polinom_list.append(
            lambda X, x=vertex.x, y=vertex.y: get_subpolinoms(
                X, x, y, vertex_list
            )
        )

    def sum(x: float):
        result = 0
        for polinom in sub_polinom_list:
            result += polinom(x)
        return result

    return sum


def get_subpolinoms(X: float, x: float, y: float, vertex_list: list[Vertex]):
    L: float = 1
    for vertex in vertex_list:
        if x != vertex.x:
            L *= (X-vertex.x)/(x-vertex.x)
    return L * y


def lagrange_interpolation_str(vertex_list: list[Vertex]):

    result = ('-' * 10) + 'subPolinoms' + ('-' * 10) + '\n'

    for vertex in vertex_list:
        result += get_subpolinoms_str(vertex.x, vertex.y, vertex_list)

    result = result[:-2] + '\n' + ('-' * 31)

    return result


def get_subpolinoms_str(x: float, y: float, vertex_list: list[Vertex]):

    result = '('

    for vertex in vertex_list:
        if x != vertex.x:
            result += get_subpolinom_str(x, vertex.x)

    result = result[:-1] + ') * (' + str(y) + ') +\n'

    return result


def get_subpolinom_str(x, vertex_x):
    return replace_nn_p(
        ' ((x-' + str(vertex_x) + ')/(' + str(x) + '-' + str(vertex_x) + ')) *'
    )


def replace_nn_p(string: str): return string.replace('--', '+')
