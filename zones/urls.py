from django.urls import path
from . import views

urlpatterns = [
    path('zones/', views.fetch_zones, name='fetch_zones'),
    path('zones/create/', views.create_zone_view, name='create_zone'),
    path('zones/delete/<int:zone_id>/', views.delete_zone_view, name='delete_zone'),
]
