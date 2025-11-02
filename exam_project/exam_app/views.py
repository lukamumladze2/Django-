from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def films(request):
    films = [
        {"title": "Inception (2010)", "imdb": 8.8},
        {"title": "Everything Everywhere All at Once (2022)", "imdb": 7.9},
        {"title": "Spirited Away (2001)", "imdb": 8.6},
        {"title": "The Godfather (1972)", "imdb": 9.2},
        {"title": "La La Land (2016)", "imdb": 8.0},
        {"title": "Parasite (2019)", "imdb": 8.5},
        {"title": "Interstellar (2014)", "imdb": 8.6},
        {"title": "Alien (1979)", "imdb": 8.5},
        {"title": "Venom (2018)", "imdb": 6.6},
        {"title": "Jurassic World: Fallen Kingdom (2018)", "imdb": 6.1},
        {"title": "Suicide Squad (2016)", "imdb": 5.9},
    ]
    return render(request, 'films.html', {"films": films})
