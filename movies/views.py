from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from movies.models import Movie
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):  #esse é o tipo de view que você usa quando você quer criar a sua própria view na mão, é o mais generico possivel
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    

    def get(self,request):
        total_movies = self.queryset.count() #capturando o total de filmes
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id')) #dois __ eu busco o value do que eu quero, por exemplo genre__name, eu quero so o name do genre. o annotate count vai informar quantos filmes tem de cada genre. ex.: ação: 4
        total_reviews = Review.objects.count() #quantidade total de reviews
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
               ' total_movies' : total_movies,
               'movies_by_genre' : movies_by_genre,
               'total_reviews' : total_reviews,
               'average_stars' : round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )