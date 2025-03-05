from movies.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True) #serializer method field é sempr eum campo calculado

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj): #essa função é a que vai calcular o method field, ele tem o nome de rate porque o nome da variavel la no serializer é rate
        return 5

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('O ano de lançamento do filme não pode ser menor que 1900.')
        return value
    
    def validate_resume(self, value):
        if value.resume > 250:
            raise serializers.ValidationError('O resumo não pode ser maior que 250 caracteres.')
        return value