from django.urls import path
from . import views


app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('fbpage-list/', views.FbpageView.as_view(), name="fbpage_list"),
    path('fbpage_image/', views.FbimageView, name="fbpage_image"),
    path('fbpage_detail/<int:pk>/', views.FbpageDetailView.as_view(), name="fbpage_detail"),

]
