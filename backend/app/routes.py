from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Product, User, Order

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserInDB(User):
    hashed_password: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hashed_password = pwd_context.hash(kwargs['password'])

    def check_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/register')
async def register(username: str, email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail='Username already exists')
    new_user = UserInDB(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'user_id': new_user.id, 'username': new_user.username, 'email': new_user.email}

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.check_password(form_data.password):
        raise HTTPException(status_code=401, detail='Invalid username or password')
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}

@router.get('/products')
async def get_products(db: SessionLocal = Depends(get_db)):
    products = db.query(Product).all()
    return {'products': products}

@router.get('/products/{product_id}')
async def get_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'category': product.category}

@router.post('/cart')
async def add_to_cart(product_id: int, quantity: int, db: SessionLocal = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == 1, Order.product_id == product_id).first()
    if order:
        order.quantity += quantity
    else:
        order = Order(user_id=1, product_id=product_id, quantity=quantity, total=0, shipping_address='Address')
        db.add(order)
    db.commit()
    db.refresh(order)
    return {'cart': [{'product_id': order.product_id, 'quantity': order.quantity}]}