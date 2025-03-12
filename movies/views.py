from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission


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
        return response.Response(
            data={'message' : 'Funcionou'},
            status=status.HTTP_200_OK,
        )