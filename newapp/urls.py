from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from newapp import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('feed', views.Feed, name='feed')

]
