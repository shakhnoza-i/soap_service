from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MathView, add_post

urlpatterns = [
    path('math/', MathView.as_view(), name='math-api'),
    # path('add/', add_post, name='add-api'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html','xml'])
