from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template

def movie_recommendation_view(request):
    if request.method == "GET":
        context = generate_movies_context()
        return render(request, 'movierecommender/movie_list.html', context)

def generate_movies_context():
    context = {}
    recommended_count = Movie.objects.filter(
        recommended=True
    ).count()

    if recommended_count == 0:
        movies = Movie.objects.filter(watched=False).order_by('-vote_count')[:30]
    else:
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended=False
        ).order_by('-vote_count')[:30]

    context['movie_list'] = movies
    context['recommended_count'] = movies.count()
    return context
