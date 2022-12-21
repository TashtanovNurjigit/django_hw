from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def book_view(request):
    post = models.Post.objects.all()
    return render(request, 'book.html', {'post_object': post})


def book_details_view(request, id):
    show = get_object_or_404(models.Post, id=id)
    return render(request, 'book_details.html', {'show_object': show})


def add_book_views(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>Фильм успешно добавлен</h1>')
    else:
        form = forms.ShowForm()

    return render(request, 'create_book.html', {'form': form})