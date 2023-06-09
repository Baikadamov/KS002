# Generated by Django 4.1.7 on 2023-04-26 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(help_text='Enter a book Author', max_length=200)),
            ],
            options={
                'verbose_name': 'Авторы книг',
                'verbose_name_plural': 'Автор книги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
            options={
                'verbose_name': 'Жанры книг',
                'verbose_name_plural': 'Жанры книг',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название книги')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='messenger.author')),
                ('genre', models.ManyToManyField(help_text='Select a genre for this book', to='messenger.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Список книг',
                'verbose_name_plural': 'Список книг',
                'ordering': ['name'],
            },
        ),
    ]
