import uuid
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from evenement.models import EvenementModel
from back.models import BodyModel, MentionsModel, PageAjoutModel, PageAjoutOptionModel
from django.db.models import Q
from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string


def IndexGet(request, lang=None):
    lang = lang or 'fr'
    r = request.GET.get('r')
    l = request.GET.get('l')
    if r and l: 
        return HttpResponseRedirect(f'/{lang}/r?r={r}&l={l}')
    elif r:
        return HttpResponseRedirect(f'/{lang}/r?r={r}')
    elif l:
        return HttpResponseRedirect(f'/{lang}/r?l={l}')

    context = {'body':BodyModel.objects.get(lang=lang)}
    response = render(request, "a1-index.html", context)
    response['Link'] = f'<{request.build_absolute_uri(request.path)}>; rel="canonical"'
    response['Content-Language'] = lang
    return response



def RechercheGet(request, lang=None):
    r = request.GET.get('r','')
    l = request.GET.get('l','')
    lang = lang or 'fr'

    if request.user_agent.is_pc or request.user_agent.is_bot:
            template_name = "b1-ordinateur.html"
    elif request.user_agent.is_mobile or request.user_agent.is_tablet:
            template_name = "b1-mobile.html"
    body = BodyModel.objects.get(lang=lang)
    
    up1 = EvenementModel.objects.filter()
    #ui = EvenementModel.objects.filter(lang=lang, Q(ia__search=r) | Q(ia__icontains=r))

    context = {'r':r,'l':l,'up1':up1,'count':up1.count(), 'body':body ,'include_menu': render_to_string(template_name, {'body': body,'r':r,'l':l })}
    return render(request, "a2-recherche.html", context)

def MentionsGet(request, slug, lang=None):
    lang = lang or 'fr'
    r = request.GET.get('r', '')
    l = request.GET.get('l', '')
    if r and l: 
        return HttpResponseRedirect(f'/{lang}/r?r={r}&l={l}')
    elif r:
        return HttpResponseRedirect(f'/{lang}/r?r={r}')
    elif l:
        return HttpResponseRedirect(f'/{lang}/r?l={l}')

    if request.user_agent.is_pc or request.user_agent.is_bot:
            template_name = "b1-ordinateur.html"
    elif request.user_agent.is_mobile or request.user_agent.is_tablet:
            template_name = "b1-mobile.html"
    body = BodyModel.objects.get(lang=lang)

    context = {'ui': MentionsModel.objects.get(slug=slug), 'body':body ,
    'include_menu': render_to_string(template_name, {'body': body})}
    
    response = render(request, "a1-mentions.html", context)
    response['Link'] = f'<{request.build_absolute_uri(request.path)}>; rel="canonical"'
    response['Content-Language'] = lang
    return response


class AjoutView(View):

    def get(self, request, lang=None):
        lang = lang or 'fr'

        if request.user_agent.is_pc or request.user_agent.is_bot:
            template_name = "b1-ordinateur.html"
        elif request.user_agent.is_mobile or request.user_agent.is_tablet:
            template_name = "b1-mobile.html"
        body = BodyModel.objects.get(lang=lang)
    
        context = {'ui': PageAjoutModel.objects.get(lang=lang), 'body':body ,
        'include_menu': render_to_string(template_name, {'body': body})}
        return render(request, "a2-ajout.html", context)

def AjoutReponseGet(request, lang=None):
    lang = lang or 'fr'
    r = request.GET.get('r', '')
    l = request.GET.get('l', '')
    if r and l: 
        return HttpResponseRedirect(f'/{lang}/r?r={r}&l={l}')
    elif r:
        return HttpResponseRedirect(f'/{lang}/r?r={r}')
    elif l:
        return HttpResponseRedirect(f'/{lang}/r?l={l}')

    if request.user_agent.is_pc or request.user_agent.is_bot:
            template_name = "b1-ordinateur.html"
    elif request.user_agent.is_mobile or request.user_agent.is_tablet:
            template_name = "b1-mobile.html"
    body = BodyModel.objects.get(lang=lang)

    context = {'body':body ,'include_menu': render_to_string(template_name, {'body': body})}
    return render(request, "a2-reponse.html", context)

