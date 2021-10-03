import json
from datetime import date, datetime

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from sweetify import sweetify

from web.models import Curriculo, Skill, Education, Experience, Portifolio, Mensagem


def index(request):
    curriculo = Curriculo.objects.first()
    skils = Skill.objects.filter(person=curriculo)
    educations = Education.objects.filter(person=curriculo)
    experiences = Experience.objects.filter(person=curriculo)
    portfifolio1 = Portifolio.objects.filter(
        person=curriculo, categoria='Web')[0:2]
    portfifolio2 = Portifolio.objects.filter(
        person=curriculo, categoria='Web')[2:4]
    portfifolio3 = Portifolio.objects.filter(
        person=curriculo, categoria='Photo')[0:2]
    portfifolio4 = Portifolio.objects.filter(
        person=curriculo, categoria='Photo')[2:4]
    portfifolio5 = Portifolio.objects.filter(
        person=curriculo, categoria='Graphic')[0:2]
    portfifolio6 = Portifolio.objects.filter(
        person=curriculo, categoria='Graphic')[2:4]

    context = {
        'curriculo': curriculo,
        'skils': skils,
        'educations': educations,
        'experiences': experiences,
        'portfifolio1': portfifolio1,
        'portfifolio2': portfifolio2,
        'portfifolio3': portfifolio3,
        'portfifolio4': portfifolio4,
        'portfifolio5': portfifolio5,
        'portfifolio6': portfifolio6,
    }
    return render(request, 'web/index.html', context)


def email(request):
    if request.POST:
        m = Mensagem()
        m.nome = request.POST['name']
        m.email = request.POST['email']
        m.assunto = request.POST['assunto']
        m.mensagem = request.POST['message']

        m.save()

        contato = request.POST['email']

        msg = EmailMultiAlternatives(
            subject="Mensagem Enviada com Sucesso",
            body="InovAção Afro - CESAR - SHARE RH",
            from_email="Claudio Marcio @blogdomarcio -  <naoresponda@marcioweb.com.br>",
            to=[contato],
            reply_to=["Suporte <blogdomarcio@live.com>"])

        # Include an inline image in the html:
        # logo_cid = attach_inline_image_file(msg, "fotos/educa.png")
        html = """"

        <p>Olá {responsavel},</p>
        <p> A sua mensagem foi enviada! </p>
        <hr>
        <p><strong>@blogdomarcio</strong></p>
        <p> blogdomarcio@live.com | (77)77999641685
        <br>
        <p></p>""".format(responsavel=request.POST['name'])
        msg.attach_alternative(html, "text/html")

        # Optional Anymail extensions:
        msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
        msg.tags = ["activation", "onboarding"]
        msg.track_clicks = True

        # Send it:
        msg.send()

        sweetify.success(request, 'Email Enviado com sucesso')

        return redirect('/')
