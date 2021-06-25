from myapp.exceptions.exceptions import BadRequest, Unauthorized
from myapp.infrastucture.hours import Hours


class GetHours:
    def __init__(self):
        self.hours = Hours()

    def execute(self, id_user, date_init, date_finish):
        if (id_user is None or id_user == '') or (date_init is None or date_init == '') or (date_finish is None or date_finish == ''):
            raise BadRequest
        results = self.hours.getHours(id_user, date_init, date_finish)
        return results
