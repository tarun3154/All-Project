# myapp/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from faker import Faker
from .models import Item

fake = Faker()

def generate_fake_data():
    return [Item(name=fake.word(), description=fake.text()) for _ in range(100)]

def item_list(request):
    # Generate fake data for testing
    fake_data = generate_fake_data()

    paginator = Paginator(fake_data, 10, orphans=1)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, 'myapp/home.html', {'items': items})
