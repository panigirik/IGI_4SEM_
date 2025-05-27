from django.urls import path
from . import views
from .views import stats_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('travel-news', views.travel_news, name='travel_news'),  # <--- ДОБАВЛЕНО
    path('stats/', views.stats_page, name='stats_page'),
    path('search/', views.search_destinations, name='search_destinations'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destinations', views.destinations, name='destinations'),
    path('stats/image/', views.stats_image, name='stats_image'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
