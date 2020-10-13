from django.shortcuts import render
import csv
import os
from task1.app import settings


def inflation_view(request):

    template_name = 'inflation.html'
    CSV_FILE = os.path.join(settings.BASE_DIR, 'inflation_russia.csv')

    # чтение csv-файла и заполнение контекста
    with open(CSV_FILE, encoding='utf8') as file:
        result = csv.DictReader(file, delimiter=';')
        data = list(result)
        context = {'rows': data}

    return render(request, template_name, context)