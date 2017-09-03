# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ex1.models import Person


def test(request):
    print "test"
    print "nedir"
    s= Person.objects.filter(first_name="mesut");
    p = Person(first_name="mesut",last_name="davar")
    a = s.count()
    p.save()

    return render(request, 'index.html', {'name': p.last_name});

# Create your views here.
