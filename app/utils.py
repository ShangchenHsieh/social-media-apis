from passlib.context import CryptContext

pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # schemes is telling it which hashing algo. to use, and bcrypt is a kind of algo.


def hash(password: str):
    return pw_context.hash(password)


def hash(password: str):
    return pw_context.hash(password)


def verify(plain_password, hashed_password):
    return pw_context.verify(plain_password, hashed_password)
