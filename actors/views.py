from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,) #função nativa do rest permissions, que pede a autenticação na hora de consultar uma view, somente os users que passarem o token terão acesso.
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
