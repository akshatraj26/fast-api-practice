from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBSession:
    def __init__(self):
        engine = create_engine('sqlite:///mydatabase.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close(self):
        self.session.close()


class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager as db:
        yield db

