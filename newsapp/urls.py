from django.urls import path
from .views import home,update, about


urlpatterns = [
    path('', home, name="home"),
    path('update/', update, name="update"),
    path('about/', about, name = 'about'),
]
