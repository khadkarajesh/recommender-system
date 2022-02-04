from werkzeug.security import check_password_hash

from api.auth.schema import UserSchema
from api.auth.user import User


def login(username, password):
    user = User.query.filter(User.username == username).first()
    if not user: return {'message': "Invalid user"}, 400
    if check_password_hash(user.password, password):
        user_schema = UserSchema()
        return user_schema.dump(user)
    return {'message': "Username/password doesn't match"}, 400
