from django.shortcuts import render, get_object_or_404
from . import models


def book_view(request):
    post = models.Post.objects.all()
    return render(request, 'book.html', {'post_object': post})


def book_details_view(request, id):
    show = get_object_or_404(models.Post, id=id)
    return render(request, 'book_details.html', {'show_object': show})
