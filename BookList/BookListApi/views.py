from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
# from django.db import IntegrityError
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import model_to_dict
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    


# # API with functions Django Rest Framework 
# @api_view(['GET', 'POST'])
# def books(request):
#     return Response('List of books', status=status.HTTP_200_OK)


# # API with pure Django
# @csrf_exempt
# def books(request):
#     if  request.method == 'GET':
#         books = Book.objects.all().values()
#         return JsonResponse({'books': list(books)})
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory')

#         book = Book(title=title, author=author, price=price, inventory=inventory)
#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({'error':'true','message':'required field missing'}, status=400)
        
#     return JsonResponse(model_to_dict(books), status=201)


# # Attempt to debug the following code, but it is not working
# def display_even_numbers(request):
#     response = ""
#     numbers = [x for x in range(1, 10)]
#     for i in numbers:
#         reminder = i % 2
#         if reminder == 0:
#             response += str(i) + "<br/>"

#     return HttpResponse(response)


