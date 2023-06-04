from rest_framework import viewsets
from .serializers import *
from .models import *
from .permissons import *


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (MyPermission,)


class AlbumViewSet(BaseViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class ArtistViewSet(BaseViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ContractViewSet(BaseViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventViewSet(BaseViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GenreViewSet(BaseViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ManagerViewSet(BaseViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class PartnerViewSet(BaseViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class RecordViewSet(BaseViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
