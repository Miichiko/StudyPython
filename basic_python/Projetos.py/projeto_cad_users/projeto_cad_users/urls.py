
from django.urls import path
from projeto_cad_usuarios import views
urlpatterns = [
    path('', views.home, name='home'),
]

# se eu quiser usar um link pra página inicial use o home ( nome q eu especifiquei no name= )
