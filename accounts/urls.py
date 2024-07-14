from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('',views.app,name='app'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about/',views.about,name='about'),
    path('login/',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    path('new_shipment/',views.new_shipment,name='new_shipment'),
    path('my_shipment/',views.my_shipment,name='my_shipment'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('track/', views.track, name='track'),
    path('track/<int:shipment_id>/', views.track, name='track_details'),

]
