from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    click = []
    if request.GET['from-landing'] == 'original':
        click.append('original')
        counter_click.update(click)
    elif request.GET['from-landing'] == 'test':
        click.append('test')
        counter_click.update(click)

    return render(request, 'index.html')


def landing(request):
    show = []
    if request.GET['ab-test-arg'] == 'original':
        show.append('original')
        counter_show.update(show)
        return render(request, 'landing.html')
    else:
        show.append('test')
        counter_show.update(show)
        return render(request, 'landing_alternate.html')

def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    if counter_show['test'] != 0:
        test_stats = counter_click['test'] / counter_show['test']
    else:
        test_stats = 0
    if counter_show['original'] != 0:
        original_stats = counter_click['original'] / counter_show['original']
    else:
        original_stats = 0

    return render(request, 'stats.html', context={
        'test_conversion': test_stats,
        'original_conversion': original_stats,
    })
