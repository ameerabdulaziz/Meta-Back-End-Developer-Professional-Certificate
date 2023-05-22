from django.db import IntegrityError
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Book


@csrf_exempt
def books(request):
    print(request.method)
    if request.method == 'GET':
        books = Book.objects.all()
        data = {
            'books': [model_to_dict(book) for book in books]
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        title = request.POST.GET('title')
        author = request.POST.GET('author')
        price = request.POST.GET('price')
        book = Books.objects.create(title=title, author=author, price=price)
        try:
            book.save()
        except IntegrityError():
            return JsonResponse({
                'error':'true','message':'required field missing'
            }, status=400)
        return JsonResponse(data=model_to_dict(books), status=201)
