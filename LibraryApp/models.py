from django.db import models


class ViewName:
    def __str__(self) -> str:
        return self.name


class Category(ViewName, models.Model):
    name = models.CharField(max_length=20)


class Author(ViewName, models.Model):
    name = models.CharField(max_length=40)


class Book(ViewName, models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_public = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    communication = models.CharField(max_length=50)
