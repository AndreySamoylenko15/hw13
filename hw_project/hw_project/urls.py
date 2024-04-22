from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path("users/",include("users.urls")),
    #path('authors/', list_authors, name='list_authors'),
    
]