from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>',views.detail,name='detail'),
    path('add',views.addItem,name='add_item'),
    path('<int:item_id>/update',views.editItem,name='edit'),
    path('<int:item_id>/delete',views.delete,name='delete')
]
