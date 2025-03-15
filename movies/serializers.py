from movies.models import Movie
from rest_framework import serializers
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('O ano de lançamento do filme não pode ser menor que 1900.')
        return value
    
    def validate_resume(self, value):
        if value.resume > 500:
            raise serializers.ValidationError('O resumo não pode ser maior que 250 caracteres.')
        return value
    

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True) #serializer method field é sempr eum campo calculado

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj): #essa função é a que vai calcular o method field, ele tem o nome de rate porque o nome da variavel la no serializer é rate
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']  #fazendo a média das avaliações com as funcs ja prontas do django

        if rate:
            return round(rate, 1) #retornando somente com uma casa decimal
        
        return None