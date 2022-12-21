from django.db import models

class Post(models.Model):
    GENRE = (
        ('Detective', 'Detective'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy'),
        ('Comedy', 'Comedy'),
        ('Fiction', 'Fiction'),
        ('Thrillers', 'Thrillers'),
        ('Adventures', 'Adventures')

    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
