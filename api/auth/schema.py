from api.auth.user import User
from api.common import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        dump_only = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth')
        load_only = ('password',)
        ordered = True
        load_instance = True
