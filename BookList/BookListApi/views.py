from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

@csrf_exempt
def books(request):
    if  request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')

        book = Book(title=title, author=author, price=price, inventory=inventory)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'}, status=400)
        
    return JsonResponse(model_to_dict(books), status=201)
