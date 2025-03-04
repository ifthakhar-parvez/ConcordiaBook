
# textbooks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for home page
    path('textbooks/<str:course_code>/', views.textbooks_for_course, name='textbooks_for_course'),
]

