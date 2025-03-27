import bcrypt


def hash_password(password):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())
    return hashed_password.decode('utf-8')

