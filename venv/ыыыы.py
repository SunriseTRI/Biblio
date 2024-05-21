
Чтобы создать новую функцию просмотра, которая вызывает функцию load_fb2_document с объектом запроса и объектом файла, а также создать новый шаблон HTML для отображения информации о книге, вы можете выполнить следующие шаги:

1.
Создайте новый шаблон URL-адреса в файле urls.py для обработки новой функции просмотра.
from django.urls import path
from .views import *

urlpatterns = [
    # ... other URL patterns ...
    path('load_fb2_document/<int:pk>/', load_fb2_document, name='load_fb2_document'),
]

2.
Создайте новую функцию просмотра под названием load_fb2_document в файлеviews.py. Эта функция должна принимать в качестве входных данных объект запроса и файловый объект и вызывать функцию load_fb2_document с этими аргументами.
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *
from .utils import *
from fb2parser import *

def load_fb2_document(request, file):
    try:
        # Call the load_fb2_document function with the request and file objects
        return load_fb2_document(request, file)
    except Exception as e:
        # If an error occurs while parsing the fb2 document, return a 404 Not Found response
        return HttpResponseNotFound("Error processing the fb2 document")

3.
Создайте новый HTML-шаблон с именем book_page.html в каталоге шаблонов. Этот шаблон должен содержать HTML-код для отображения информации о книге.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Information</title>
</head>
<body>
    <h1>Book Information</h1>
    <div id="book-info">
        {{ book_info }}
    </div>
</body>
</html>

4.
Наконец, обновите функцию load_fb2_document в файлеviews.py, чтобы отображать информацию о книге с помощью функции рендеринга и шаблона book_page.html.
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *
from .utils import *
from fb2parser import *

def load_fb2_document(request, file):
    try:
        # Parse the fb2 document
        book = fb2parser.parse(file.read())

        # Get the title, authors, and summary of the book
        title = book.title
        authors = [author.name for author in book.authors]
        summary = book.summary

        # Render the book information as a dictionary
        context = {"book_info": f"Title: {title}\nAuthors: {', '.join(authors)}\nSummary: {summary}"}

        # Render the book information as an HTML page
        html_page = render(request, "book_page.html", context)

        # Return the HTML page as a response
        return HttpResponse(html_page, content_type="text/html")

    except Exception as e:
        # If an error occurs while parsing the fb2 document, return a 404 Not Found response
        return HttpResponseNotFound("Error processing the fb2 document")

 tURL-адрес /load_fb2_document/<int:pk>/ в вашем браузере отобразит информацию о книге в файле fb2 с заданным идентификатором.