from sqlalchemy import Integer, String, Column, ForeignKey, DateTime, CheckConstraint, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String, nullable=False, unique=True)
    books = relationship('Book', backref='genre')

class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    name_author = Column(String, nullable=False, unique=True)
    books = relationship('Book', backref='author')

class Step(Base):
    __tablename__ = 'steps'
    step_id = Column(Integer, primary_key=True)
    name_step = Column(String, nullable=False, unique=True)
    buys = relationship('Buy', secondary='buy_steps', back_populates='steps')



class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    name_city = Column(String, nullable=False, unique=True)
    days_delivery = Column(Integer, nullable=False)
    clients = relationship('Client', backref='city')

class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    name_client = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False, ondelete='CASCADE')
    buys = relationship('Buy', backref='client')
    city = relationship('City', backref='clients')

class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.author_id'), nullable=False, ondelete='CASCADE')
    genre_id = Column(Integer, ForeignKey('genres.genre_id'), nullable=False, ondelete='CASCADE')
    price = Column(DECIMAL, CheckConstraint('price >= 0'), nullable=False)
    amount = Column(Integer, CheckConstraint('amount >= 0'), nullable=False)
    genre = relationship('Genre', backref='books')
    author = relationship('Author', backref='books')
    buys = relationship('Buy', secondary='buy_books', back_populates='books')

class Buy(Base):
    __tablename__ = 'buys'
    buy_id = Column(Integer, primary_key=True)
    buy_description = Column(String)
    client_id = Column(Integer, ForeignKey('clients.client_id'), nullable=False, ondelete='CASCADE')
    books = relationship('Book', secondary='buy_books', back_populates='buys')
    steps = relationship('Step', secondary='buy_steps', back_populates='buys')

class BuyStep(Base):
    __tablename__ = 'buy_steps'
    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buys.buy_id'), nullable=False, ondelete='CASCADE')
    step_id = Column(Integer, ForeignKey('steps.step_id'), nullable=False, ondelete='CASCADE')
    date_step_beg = Column(DateTime, server_default=func.now())
    date_step_end = Column(DateTime, nullable=True)
    buy = relationship('Buy', backref='step_associations')
    step = relationship('Step', backref='buy_associations')

class BuyBook(Base):
    __tablename__ = 'buy_books'
    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buys.buy_id'), nullable=False, ondelete='CASCADE')
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False, ondelete='CASCADE')
    amount = Column(Integer, CheckConstraint('amount >= 0'), nullable=False)
    buy = relationship('Buy', backref='book_associations')
    book = relationship('Book', backref='buy_associations')