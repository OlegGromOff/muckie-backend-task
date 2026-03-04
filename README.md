# Muckie GmbH Backend Task

## Tech Stack
- Python 3.x
- Django
- Django Rest Framework
- django-cors-headers

## Installation

1. Clone repository
2. Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies
   pip install -r requirements.txt
4. Run migrations
   python manage.py migrate
5. Start server
   python manage.py runserver

Server runs at:
http://localhost:8000/

## Endpoints

GET /api/products/
→ Returns 5 products

GET /api/products/1/
→ Returns product with ID 1

PUT /api/products/1/
→ Updates product

DELETE /api/products/1/
→ Deletes product

POST /api/products/create/
→ Creates new product

## Notes
- Separate Stock model implemented
- CORS enabled
- Docstrings included
- Tested with Postman
