from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    birth_year = models.IntegerField("Год рождения", null=True, blank=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField("Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField("Год публикации")
    price = models.DecimalField("Стоимость", max_digits=8, decimal_places=2)
    is_available = models.BooleanField("В наличии", default=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
