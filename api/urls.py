from django.contrib import admin
from django.urls import path, include, re_path

from statistics.views import CreateStatistic, StatisticsList, ResetStatistics

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('social_django.urls', namespace='social')),
    path('api/v1/create_statistics/', CreateStatistic.as_view(), name='create'),
    path('api/v1/list_statistics/', StatisticsList.as_view(), name='list'),
    path('api/v1/reset_statistics/<int:pk>/', ResetStatistics.as_view(), name='reset'),
]
