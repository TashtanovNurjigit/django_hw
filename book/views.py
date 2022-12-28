from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.all()
# def book_view(request):
#     post = models.Post.objects.all()
#     return render(request, 'book.html', {'post_object': post})


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


def update_book(request, id):
    show_object = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Пост успешно обновлен</h1>')
    else:
        form = forms.ShowForm(instance=show_object)
    return render(request, 'book_update.html', {'form': form, 'object': show_object})


def delete_book(request, id):
    show_object = get_object_or_404(models.Post, id=id)
    show_object.delete()
    return HttpResponse('<h1>Пост успешно удален</h1>')