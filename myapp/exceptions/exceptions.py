


class BadRequest(Exception):
    # nos mandan datos incorrectos (nulos, vacios, no validos)
    pass


class Unauthorized(Exception):
    # datos no se encuentran en bbdd
    pass
