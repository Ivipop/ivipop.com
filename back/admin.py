from django.contrib import admin
from evenement.models import EvenementModel
from back.models import BodyModel, MentionsModel, PageAjoutModel

admin.site.register([EvenementModel, BodyModel, MentionsModel, PageAjoutModel, PageAjoutOptionModel])