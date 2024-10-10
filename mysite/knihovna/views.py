from django.shortcuts import render, redirect
from django.http import HttpResponse

def main_page(request):
    return HttpResponse("<h1>Vítejte na hlavní stránce!</h1>")

def writers(request):
    # Vypíšeme seznam spisovatelů
    spisovatele = ['Franz Kafka', 'Leo Tolstoy', 'George Orwell', 'Virginia Woolf']
    output = "<h1>Seznam spisovatelů:</h1><ul>"
    for spisovatel in spisovatele:
        output += f"<li>{spisovatel}</li>"
    output += "</ul>"
    return HttpResponse(output)

def books(request):
    # Vypíšeme seznam nejlepších knih
    knihy = ['1984 - George Orwell', 'Anna Karenina - Leo Tolstoy', 'Proměna - Franz Kafka']
    output = "<h1>Seznam nejlepších knih:</h1><ul>"
    for kniha in knihy:
        output += f"<li>{kniha}</li>"
    output += "</ul>"
    return HttpResponse(output)

def author_detail(request, author_name):
    # Informace o spisovatelích
    author_info = {
        'Hemingway': 'Ernest Hemingway byl americký spisovatel a novinář. Autor mnoha známých knih jako "Stařec a moře".',
        'Shakespeare': 'William Shakespeare byl anglický dramatik a básník. Známý pro díla jako "Hamlet" a "Romeo a Julie".'
    }
    
    # Pokud je spisovatel nalezen, zobrazíme jeho informace
    if author_name in author_info:
        return HttpResponse(f"<h1>{author_name}</h1><p>{author_info[author_name]}</p>")
    
    # Pokud spisovatel není nalezen, přesměrujeme na stránku se seznamem spisovatelů
    return redirect('writers')


