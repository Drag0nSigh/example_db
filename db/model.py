from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genre'
    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)
    books = relationship("Book", backref="genre")

class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)
    books = relationship("Book", backref="author")

class Step(Base):
    __tablename__ = 'step'
    step_id = Column(Integer, primary_key=True)
    name_step = Column(String)


class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)
    clients = relationship("Client", backref="city")

class Client(Base):
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    email = Column(String)
    city_id = Column(Integer, ForeignKey('city.city_id'))

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    genre_id = Column(Integer, ForeignKey('genre.genre_id'))
    price = Column(Integer)
    amount = Column(Integer)