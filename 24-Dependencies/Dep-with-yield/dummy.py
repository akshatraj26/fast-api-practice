from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBSession:
    def __init__(self):
        engine = create_engine('sqlite:///mydatabase.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close(self):
        self.session.close()



class DepA:
    pass

class DepB:
    pass

def generate_dep_a():
    pass


def generate_dep_b():
    pass


def generate_dep_c():
    pass


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_b(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
