#-*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import serializers
from models import LabLoggerResult


def home(request):
    """ This is the home page where we list labs """
    return render(request, "ui/index.html", {'date': datetime.now()})
# end home


def list_experiences(request, lab_name):
    """
    View that show a lab by lab name.
    :param request:
    :param id_article:
    :return:
    """
    return HttpResponse(
        "You asked the lab {0}".format(lab_name)
    )
# end view_lab


def list_instances(request, lab_name, exp_name):
    """
    List all instances of an experience.
    :param request:
    :param lab_name:
    :param exp_name:
    :return:
    """
    return HttpResponse(
        "Vous avez demandé les instances de {0} du lab {1}".format(exp_name, lab_name)
    )
# end list_instances


# API endpoint that allows result to be viewed and inserted
class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or inserted.
    """
    queryset = LabLoggerResult.objects.all()
    serializer_class = serializers.ResultSerializer
# end ResultViewSet
