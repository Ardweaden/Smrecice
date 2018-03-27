# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:31:07 2018

@author: Jan Jezersek
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]