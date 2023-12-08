# myproject/fastapi_app.py
import os
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
from faker import Faker
from pydantic import BaseModel
from typing import List

app = FastAPI()
fake = Faker()

class ItemResponse(BaseModel):
    items: List[dict]

def generate_fake_data():
    return [{"name": fake.word(), "description": fake.text()} for _ in range(100)]

@app.get("/api/get-data", response_model=ItemResponse)
async def get_data(page: int = 1):
    # Import Django setup locally
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from django import setup
    setup()

    # Import Django models locally
    from myapp.models import Item

    items_per_page = 10
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    fake_data = generate_fake_data()
    items = fake_data[start_idx:end_idx]
    
    # Wrap the items in the ItemResponse Pydantic model
    return ItemResponse(items=items)

# Mount FastAPI app onto the Django app at the specified route
django_app = get_wsgi_application()
app.mount('/', WSGIMiddleware(django_app))
