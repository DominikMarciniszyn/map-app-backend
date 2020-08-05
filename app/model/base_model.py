from peewee import Model, PostgresqlDatabase
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


db = PostgresqlDatabase(
    config['postgres']['name'],
    user=config['postgres']['user'],
    password=config['postgres']['passwd'],
    host=config['postgres']['host'],
    port=config['postgres']['port']
)


class BaseModel(Model):
    class Meta:
        database = db
