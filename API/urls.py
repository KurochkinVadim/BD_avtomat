from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Album', views.AlbumViewSet)
router.register(r'Artist', views.ArtistViewSet)
router.register(r'Contract', views.ContractViewSet)
router.register(r'Event', views.EventViewSet)
router.register(r'Genre', views.GenreViewSet)
router.register(r'Manager', views.ManagerViewSet)
router.register(r'Partner', views.PartnerViewSet)
router.register(r'Record', views.RecordViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
