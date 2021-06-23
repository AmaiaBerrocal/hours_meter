'''
clase Login
metodo execute
1. recibe usuario y contraseña (por parametro)
2. si ususario o contraseña vacio/nulo responde con excepcion BAD REQUEST
3. si el par usuario contraseña no esta en bbdd responder con error UNAUTORIZED
4. si todo bien devolver ID USUARIO
'''
from myapp.exceptions.exceptions import BadRequest, Unautorized
from myapp.infrastucture.users import Users


class Login:
    def __init__(self):
        self.users = Users()

    def execute(self, user_name, password):
        if ((user_name == None or user_name == "") or (password == None or password == "")):
            raise BadRequest
        user = self.users.retrieveUser(user_name, password)
        if user is None:
            raise Unauthorized()
        return user.id_user

