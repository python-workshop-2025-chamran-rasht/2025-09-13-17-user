from secrets import token_urlsafe
from pathlib import Path

SECRET_KEY = token_urlsafe(64)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(__file__).parent.joinpath('app.db').absolute())
