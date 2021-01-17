import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    inflation = []
    with open('inflation_russia.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            inflation.append(row)
    context['th'] = inflation[0]
    context['td'] = inflation[1:]

    return render(request, template_name,
                  context = context)