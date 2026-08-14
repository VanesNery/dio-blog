import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'sqlite:///dio_blog.sqlite'
)

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')