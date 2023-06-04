# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year_of_release = models.DateField()
    id_artist = models.ForeignKey('Artist', models.DO_NOTHING, db_column='id_artist')
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    id_genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='id_genre')
    id_contract = models.ForeignKey('Contract', models.DO_NOTHING, db_column='id_contract')
    id_manager = models.ForeignKey('Manager', models.DO_NOTHING, db_column='id_manager')
    fcs = models.CharField(db_column='FCs', max_length=35)  # Field name made lowercase.
    nickname = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'artist'


class Contract(models.Model):
    id_contract = models.AutoField(primary_key=True)
    date_of_signing = models.DateField()
    validity = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'contract'


class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    venue = models.CharField(max_length=45)
    id_artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='id_artist')
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'event'


class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'genre'


class Manager(models.Model):
    id_manager = models.AutoField(primary_key=True)
    fcs = models.CharField(db_column='FCs', max_length=35)  # Field name made lowercase.
    mail = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'manager'


class Partner(models.Model):
    id_partner = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=15)
    id_event = models.ForeignKey(Event, models.DO_NOTHING, db_column='id_event')

    class Meta:
        managed = False
        db_table = 'partner'


class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year_of_release = models.DateField()
    sales = models.BigIntegerField()
    auditions = models.BigIntegerField()
    id_album = models.ForeignKey(Album, models.DO_NOTHING, db_column='id_album')

    class Meta:
        managed = False
        db_table = 'record'
