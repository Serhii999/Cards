from card_app.views import *
from django.urls import path, include
from rest_framework import routers
from card_app.API.resources import CardViewSet


router = routers.SimpleRouter()
router.register(r'cards', CardViewSet)
urlpatterns = router.urls


urlpatterns = [
    path('api/', include(router.urls)),
    path('', CardListView.as_view(), name='main'),
    path('card/create/', CardCreateView.as_view(), name='card_create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('card/delete/<int:pk>', DeleteCardView.as_view(), name='delete'),
    path('card/update/<int:pk>', UpdateCardView.as_view(), name='update'),
    path('card/search/', SearchResultsView.as_view(), name='search')
]