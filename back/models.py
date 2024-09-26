from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
import datetime, uuid
from functools import cached_property
from django.urls.base import reverse

class BodyModel(models.Model):
    lang = models.CharField(primary_key=True)
    pays = models.CharField(null=True, blank=True)
    header_accueil_url = models.CharField(null=True, blank=True)
    header_accueil_ancre = models.CharField( null=True, blank=True)
    header_ajout_ancre = models.CharField(null=True, blank=True)
    header_ajout_url = models.CharField(null=True, blank=True)
    header_recherche_evenement = models.CharField(null=True, blank=True)
    header_recherche_lieu = models.CharField(null=True, blank=True)
    recherche_resultat_ancre = models.CharField(null=True, blank=True)
    recherche_resultat_aucun_ancre = models.CharField(null=True, blank=True)
    footer_mentions_ancre = models.CharField(null=True, blank=True)
    footer_mentions_url = models.CharField(null=True, blank=True)
    
    titre = models.CharField(null=True, blank=True)
    index_titre = models.CharField(null=True, blank=True)
    index_texte = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.lang}'

    class Meta:
        verbose_name = 'body'

class PageImplementationModel(models.Model):
    noindex = models.IntegerField(null=True, blank=True, default=1)
    titre = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, max_length=2050)
    img = models.CharField(null=True, blank=True)
    date = models.DateField(null=True, auto_now_add=True)
    templates = models.CharField(null=True, blank=True)
    texte = models.TextField(null=True,max_length=10050)
    vues = models.IntegerField(default=0, null=True, blank=True)
    ancre1 = models.CharField(null=True, blank=True)
    ancre2 = models.CharField(null=True, blank=True)
    h1 = models.CharField(null=True, blank=True)
    h2 = models.CharField(null=True, blank=True)
    
    class Meta:
        abstract = True

class MentionsModel(PageImplementationModel):
    lang = models.CharField(primary_key=True)
    slug = models.CharField(null=True, blank=True)

    def __str__(self):
        return f'{self.lang} {self.slug} {self.titre}'

    class Meta:
        verbose_name = 'mentions'

class PageAjoutModel(PageImplementationModel):
    lang = models.CharField(primary_key=True)
    href_physique_ancre = models.CharField(null=True, blank=True)
    href_ligne_ancre = models.CharField(null=True, blank=True)
    placeholde_titre = models.CharField(null=True, blank=True)
    placeholde_adresse = models.CharField(null=True, blank=True)
    placeholde_ville = models.CharField(null=True, blank=True)
    placeholde_prix = models.CharField(null=True, blank=True)
    placeholde_categorie = models.CharField(null=True, blank=True)
    placeholde_organisateur = models.CharField(null=True, blank=True)
    placeholde_email = models.CharField(null=True, blank=True)
    boutton = models.CharField(null=True, blank=True)
    suggestion_option = models.CharField(null=True, blank=True)

    def __str__(self):
        return f'{self.lang} {self.titre}'

    class Meta:
        verbose_name = 'page ajout'
