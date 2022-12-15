from django.shortcuts import render
from . import models


def book_view(request):
    post = models.Post.objects.all()
    return render(request, 'book.html', {'post_object': post})
