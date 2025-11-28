# e-commerce-platform

A comprehensive e-commerce platform with modern design and robust features.

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: FastAPI + SQLAlchemy
- **Design**: Figma ([View Design](https://www.figma.com/design/FfnnHRPoygOhto1mMckkHd/Wedding-Service-Website--Community-?node-id=1-1389&t=sqxqeENx42iYCZay-1))

## Project Structure

```
e-commerce-platform/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- Product browsing and searching
- Shopping cart and checkout
- Order management and tracking
- Password reset and recovery
- User profile and account management
- Admin dashboard and analytics

## API Endpoints

- `GET /api/products` - Get a list of all products
- `GET /api/products/{product_id}` - Get a product by ID
- `POST /api/cart` - Add a product to the cart
- `GET /api/cart` - Get the cart
- `POST /api/checkout` - Checkout
- `POST /api/register` - Register a new user
- `POST /api/login` - Log in a user
- `POST /api/reset-password` - Reset a user's password

## License

MIT
