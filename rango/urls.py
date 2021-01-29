# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:27:17 2021

@author: mic5r
"""
from django.urls import path
from rango import views

app_name= 'rango'
urlpatterns= [path('',views.index, name='index'), 
              path('about/', views.about, name='about'),
              path('category/<slug:category_name_slug>/', views.show_category,
                   name= 'show_category')
              ]
