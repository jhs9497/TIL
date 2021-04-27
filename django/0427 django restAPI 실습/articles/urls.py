from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="조현식",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_id>/', views.article_detail),

    path('comments/', views.comment_list),
    path('comments/<int:comment_id>/', views.comment_detail),

    path('articles/<int:article_id>/comments/', views.create_comment),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]