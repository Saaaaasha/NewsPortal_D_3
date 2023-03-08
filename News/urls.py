from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
