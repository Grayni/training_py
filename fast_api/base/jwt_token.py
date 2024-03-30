import jwt_oauth2

SECRET_KEY = 'mysecretkey'
ALGORITHM = 'HS256'

USERS_DATA = [
    {'username': 'admin', 'password': 'pass1234'}
]


# func jwt token
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get('sub')
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass


def get_user(username: str):
    for user in USERS_DATA:
        if user.get('username') == username:
            return user
    return None


token = create_jwt_token({'sub': 'admin'})
print(token)

username = get_user_from_token(token)
print(username)

current_user = get_user(username)
print(current_user)
