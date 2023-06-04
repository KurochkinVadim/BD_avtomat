from rest_framework import serializers

from .models import \
    Album, Artist, Contract, Record, \
    Event, Genre, Manager, Partner


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id_album', 'name', 'year_of_release', 'id_artist', 'sales']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id_artist', 'id_genre', 'id_contract', 'id_manager', 'fcs', 'nickname')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id_contract', 'date_of_signing', 'validity']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id_event', 'start_time', 'venue', 'id_artist', 'name')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id_genre', 'name')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id_manager', 'fcs', 'mail', 'contact_number')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id_partner', 'organization', 'id_event')


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id_record', 'name', 'year_of_release', 'sales', 'auditions', 'id_album')

