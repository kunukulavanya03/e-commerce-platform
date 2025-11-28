from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    orders = relationship('Order', backref='product')

    def __repr__(self):
        return f'Product(id={self.id}, name={self.name})'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    orders = relationship('Order', backref='user')

    def __repr__(self):
        return f'User(id={self.id}, username={self.username})'

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    shipping_address = Column(String, nullable=False)

    def __repr__(self):
        return f'Order(id={self.id}, user_id={self.user_id}, product_id={self.product_id})'