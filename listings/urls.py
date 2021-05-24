from django.urls import path
from listings.views import UnitViewSet



urlpatterns = [
    path('units/', UnitViewSet.as_view(), name='listing_search'),
]
