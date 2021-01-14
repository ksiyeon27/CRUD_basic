from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.post_list, name='list'),  # url 이름이 list


]
