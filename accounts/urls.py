from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('',views.app,name='app'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('track/',views.track,name='track'),
]
