from django.urls import path
from . import views

app_name = 'speakers'
urlpatterns = [
    path('', views.index, name='index'),
    # path('jado', views.jado)
    # path('<str:speaker_name>', views.create, name='create')
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete')
]