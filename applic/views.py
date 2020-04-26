from django.shortcuts import render
from django.http import HttpResponse
from .models import Message, Person


def index(request):

    # Генерация "количеств" некоторых главных объектов
    num_messages = Message.objects.all().count()
    num_Person = Person.objects.all().count()
    mess = Message.objects.all()
    peop = Person.objects.all()
    # return render(request, 'webapp/index.html')
    return render(
        request,
        'webapp/index.html',
        context={'num_messages': num_messages, 'num_peson': num_Person, "mess": mess[0], "peop": peop[0]},
    )