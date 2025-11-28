from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float
    shipping_address: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None