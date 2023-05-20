class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


def lagrange_interpolation(point_list: list[Point]):
    sub_polinom_list = []

    for point in point_list:
        sub_polinom_list.append(
            lambda X, x=point.x, y=point.y: get_subpolinoms(
                X, x, y, point_list
            )
        )

    def sum_polinoms(x: float):
        result = 0
        for polinom in sub_polinom_list:
            result += polinom(x)
        return result

    return sum_polinoms


def get_subpolinoms(X: float, x: float, y: float, point_list: list[Point]):
    L: float = 1
    for point in point_list:
        if x != point.x:
            L *= (X-point.x)/(x-point.x)
    return L * y


def lagrange_interpolation_str(point_list: list[Point]):

    result = ('-' * 10) + 'subPolinoms' + ('-' * 10) + '\n'

    for point in point_list:
        result += get_subpolinoms_str(point.x, point.y, point_list)

    result = result[:-2] + '\n' + ('-' * 31)

    return result


def get_subpolinoms_str(x: float, y: float, vertex_list: list[Point]):

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
