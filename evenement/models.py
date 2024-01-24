from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns
from functools import cached_property
from django.urls.base import reverse
from django.db import models
import datetime, uuid

class EvenementModel(DjangoCassandraModel):
    __table_name__ = 'evenement_model'
    __connection__ = 'cassandra'

    evenement_id = columns.Text(primary_key=True)
    lang = columns.Text()
    titre = columns.Text()
    jour = columns.Integer()
    mois = columns.Text()
    annee = columns.Integer()
    date = columns.Text()
    heure = columns.Text()
    categorie = columns.Text()
    adresse = columns.Text()
    ville = columns.Text()
    organisateur = columns.Text()
    email = columns.Text()
    prix = columns.Text()
    devise = columns.Text()
    vues = columns.Text()
    ia_evenement = columns.Text()
    ia_lieu = columns.Text()

    ann_ancre = columns.Text()
    ann_url = columns.Text()

    def __str__(self):
        return f'{self.lang}'
    
    class Meta:
        get_pk_field = 'evenement_id'
        verbose_name = 'Evenement'


