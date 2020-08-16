from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router=DefaultRouter()
# DefaultRouter
# This router is similar to SimpleRouter as above,
# but additionally includes a default API root view, that returns a response containing hyperlinks to all the list views.
# It also generates routes for optional .json style format suffixes.

# 출처 : https://www.django-rest-framework.org/api-guide/routers/#defaultrouter

router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name='recipe'

urlpatterns=[
    path('', include(router.urls))
]
