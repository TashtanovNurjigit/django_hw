# Generated by Django 4.1.4 on 2022-12-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Detective', 'Detective'), ('Horror', 'Horror'), ('Fantasy', 'Fantasy'), ('Comedy', 'Comedy'), ('Fiction', 'Fiction'), ('Thrillers', 'Thrillers'), ('Adventures', 'Adventures')], max_length=100, null=True),
        ),
    ]
