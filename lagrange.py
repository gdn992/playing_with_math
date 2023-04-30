class Vertex:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


def lagrange_interpolation(vertex_list: list[Vertex]):
    sub_polinom_list: list[function] = []

    for i, vertex in enumerate(vertex_list):
        x = vertex.x
        y = vertex.y
        sub_polinom_list.append(
            lambda X, x=x, y=y: get_subpolinoms(X, x, y, vertex_list)
        )

    def sum(x: float):
        result = 0

        print(('-' * 10) + 'subPolinoms' + ('-' * 10))
        for polinom in sub_polinom_list:
            result += polinom(x)
        print('-' * 31)

        return result

    return sum


def get_subpolinoms(X: float, x: float, y: float, vertex_list: list[Vertex]):
    L: float = 1
    Ln: list[str] = []
    for pont in vertex_list:
        if x != pont.x:
            Ln.append('((x-'+str(pont.x)+')/('+str(x)+'-'+str(pont.x)+'))')
            L *= (X-pont.x)/(x-pont.x)
    print('*'.join(Ln).replace('--', '+'))
    return L * y
