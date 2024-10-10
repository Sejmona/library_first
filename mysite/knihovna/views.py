from django.shortcuts import render, redirect
from django.http import HttpResponse

# Rozšířený seznam spisovatelů a jejich knih, včetně roků
writers_books_data = {
    'Hemingway': {
        'name': 'Ernest Hemingway',
        'bio': 'Ernest Hemingway byl americký novinář, prozaik a spisovatel krátkých příběhů, nositel Nobelovy ceny za literaturu.',
        'books': [
            {
                'title': 'The Sun Also Rises',
                'year': 1926,
                'description': 'Román, který zobrazuje životy amerických a britských expatů v poválečné Evropě.'
            },
            {
                'title': 'For Whom the Bell Tolls',
                'year': 1940,
                'description': 'Příběh zasazený do španělské občanské války o lásce a obětech.'
            }
        ]
    },
    'Shakespeare': {
        'name': 'William Shakespeare',
        'bio': 'William Shakespeare byl anglický básník, dramatik a herec, často označován za největšího dramatika všech dob.',
        'books': [
            {
                'title': 'Romeo and Juliet',
                'year': 1597,
                'description': 'Tragický příběh lásky dvou mladých lidí.'
            },
            {
                'title': 'Hamlet',
                'year': 1603,
                'description': 'Slavná tragédie o princi Hamletovi a jeho dilematech pomsty.'
            }
        ]
    }
}

def main(request):
    return HttpResponse("<h1>Hlavní stránka</h1><p>Vítejte na hlavní stránce naší aplikace!</p>")

def writers(request):
    writer_name = request.GET.get('writers')
    year = request.GET.get('year')

    if writer_name and year:
        # Získáme informace o autorovi
        writer_info = writers_books_data.get(writer_name)
        if writer_info:
            # Filtrování knih podle roku
            books_by_year = [book for book in writer_info['books'] if str(book['year']) == year]
            if books_by_year:
                # Pokud najdeme knihy z daného roku, zobrazíme je
                books_list = "".join(f"<li>{book['title']} ({book['year']}) - {book['description']}</li>" for book in books_by_year)
                return HttpResponse(f"<h1>Knihy od {writer_info['name']} z roku {year}</h1><ul>{books_list}</ul>")
            else:
                # Pokud nejsou knihy z daného roku, přesměrujeme na stránku autora
                return redirect('writer_detail', name=writer_name)
        else:
            return redirect('writers')
    
    return HttpResponse("<h1>Spisovatelé</h1><p>Zadejte jméno spisovatele a rok.</p>")

def cities(request):
    writer_name = request.GET.get('writers')
    year = request.GET.get('year')

    if writer_name and year:
        # Získáme informace o autorovi
        writer_info = writers_books_data.get(writer_name)
        if writer_info:
            # Filtrování knih podle roku
            books_by_year = [book for book in writer_info['books'] if str(book['year']) == year]
            if books_by_year:
                # Pokud najdeme knihy z daného roku, zobrazíme je
                books_list = "".join(f"<li>{book['title']} ({book['year']}) - {book['description']}</li>" for book in books_by_year)
                return HttpResponse(f"<h1>Knihy od {writer_info['name']} z roku {year}</h1><ul>{books_list}</ul>")
            else:
                # Pokud nejsou knihy z daného roku, přesměrujeme na stránku autora
                return redirect('writer_detail', name=writer_name)
        else:
            return redirect('writers')
    
    return HttpResponse("<h1>Města</h1><p>Zadejte jméno spisovatele a rok.</p>")
