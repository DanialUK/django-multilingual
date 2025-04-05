# Pro Shop - Django E-commerce Platform

Modern e-commerce platform built with Django, PostgreSQL, and Tailwind CSS.

## 🚀 Features

- User authentication and authorization
- Product catalog with categories
- Shopping cart functionality
- Secure payment processing with Stripe
- Seller dashboard
- Order management
- User profiles
- Responsive design with Tailwind CSS

## 🛠 Tech Stack

- Django 4.2
- PostgreSQL
- Docker & Docker Compose
- Tailwind CSS
- Stripe Payment Integration
- Crispy Forms with Tailwind

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pro-shop.git
cd pro-shop
```

2. Create .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Build and run with Docker:
```bash
docker-compose up --build
```

4. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

5. Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

## 🌐 URLs

- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/
- Product catalog: http://localhost:8000/myapp/
- User profiles: http://localhost:8000/users/

## 💻 Development

1. Install development dependencies:
```bash
npm install
```

2. Run Tailwind build:
```bash
npm run build
```

3. Run tests:
```bash
docker-compose exec web python manage.py test
```

## 🔐 Environment Variables

Required environment variables:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `POSTGRESQL_DATABASE`
- `POSTGRESQL_USERNAME`
- `POSTGRESQL_PASSWORD`
- `STRIPE_PUBLISHABLE_KEY`
- `STRIPE_SECRET_KEY`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 