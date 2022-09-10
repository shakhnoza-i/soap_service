from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AddView, add_post

urlpatterns = [
    path('add/', AddView.as_view(), name='add-api'),
    # path('add/', add_post, name='add-api'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html','xml'])
