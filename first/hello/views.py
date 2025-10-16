from django.shortcuts import render
from .models import *
from django.db.models import Count, Avg, Min, Max

# Задание 1
def index(request):
    books = Book.objects.filter(is_available=True).order_by('title')
    return render(request, 'index.html', {'books': books})

#Задние 2

def author_books(request, author_id):

    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author).order_by('-publication_year')
    return render(request, 'author_books.html', {
        'author': author,
        'books': books
    })

#Задание 3

def statistics(request):

    total_books = Book.objects.count()
    
    avg_price_result = Book.objects.aggregate(avg_price=Avg('price'))
    avg_price = avg_price_result['avg_price']
    if avg_price:
        avg_price = round(avg_price, 2)
    
    years = Book.objects.aggregate(
        earliest_year=Min('publication_year'),
        latest_year=Max('publication_year')
    )
    
    authors_with_multiple_books = Author.objects.annotate(
        book_count=Count('book')
    ).filter(book_count__gt=1).order_by('-book_count')
    
    context = {
        'total_books': total_books,
        'avg_price': avg_price,
        'earliest_year': years['earliest_year'],
        'latest_year': years['latest_year'],
        'authors_with_multiple_books': authors_with_multiple_books,
    }
    
    return render(request, 'statistics.html', context)

#Задание 4

def old_books(request):
    books = Book.objects.filter(
    price__gt=1000,
    publication_year__lt=1980
).order_by('-price')
    
    return render(request, 'old_books.html', {'books': books})

# Задание 1.

# Создайте функцию, которая должна: 

#     получить все книги, которые в наличии и отсортируйте их по названию в алфавитном порядке,
#     передать список книг в шаблон.
     
# В шаблоне: 

#     отобразите заголовок «Книги в наличии»,
#     выведите таблицу с колонками: Название, Автор, Год издания, Цена (формат 2 знака после запятой используя фильтр),
#     если книг нет — покажите сообщение: «Нет доступных книг».
     
# Подсказка: {% empty %} - если нет данных



# Задание 2

# Создайте функцию, которая должна: 

#     получить автора по author_id,
#     получить все книги этого автора, отсортированные по году издания (от новых к старым),
#     передать в шаблон самого автора и его книги.
     
# В шаблоне: 

#     отобразите заголовок: «Книги автора: author»,
#     выведите список книг в виде нумерованного списка,
#     для каждой книги укажите: название, год издания и цену,
#     если у автора нет книг — напишите: «У этого автора пока нет книг в каталоге».
 
# Подсказка: Для получения всех книг автора можно обращаться по id Book.objects.filter(author=author_id).



# Задание 3

# Создайте функцию, которая должна с помощью агрегатных функций и аннотаций получить: 

#     Общее количество книг в каталоге.
#     Среднюю цену всех книг (округлена до 2 знаков).
#     Самый ранний и самый поздний год издания.
#     Список авторов, у которых более одной книги, с указанием количества их книг.
     
# В шаблоне : 

#     отобразите раздел «Общая статистика»:
#         «Всего книг: X»
#         «Средняя цена: Y»
#         «Годы издания: от A до B»
         
#     ниже — раздел «Авторы с несколькими книгами»:
#         если таких авторов нет — напишите «Таких авторов нет»,
#         иначе выведите таблицу: Имя автора | Количество книг.

# Подсказка: используйте from django.db.models import Count, Avg, Min, Max.
# Для пункта 4 методы сравнения: value__cond, где value - переменная, cond - оператор
# Самые популярные операторы:
# gt - больше чем
# gte- больше чем и равно
# lt - меньше чем
# lte - меньше чем и равно



# Задание 4

# Создайте функцию, которая должна: 

#     выбрать книги, которые одновременно:
#         дороже 1000 рублей,
#         опубликованы до 1980 года,     
#     отсортировать их по убыванию цены,
     
# В шаблоне: 

#     заголовок: «Дорогие старые книги»,
#     таблица с колонками: Название, Автор, Год, Цена
#     если таких книг нет — сообщение: «Не найдено дорогих старых книг».