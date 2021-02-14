from django.urls import path
from basic_app.views import SchoolListView, SchoolDetailView

app_name = 'basic_app'

urlpatterns = [
    path('schools/', SchoolListView.as_view(), name='school_list'),
    path('schools/<int:pk>', SchoolDetailView.as_view(), name='school_detail'),
]
