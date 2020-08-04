from contextvars import ContextVar

import peewee


DB_NAME = 'map_app_db'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = '127.0.0.1'
PORT = 5430


db_state_default = {
    'closed': None,
    'conn': None,
    'ctx': None, 
    'transactions': None
}
db_state = ContextVar('db_state', default=db_state_default)


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__('state', db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(
    DB_NAME,
    USER,
    PASSWORD,
    HOST,
    PORT,
    check_same_thread=False
)

db._state = PeeweeConnectionState()
