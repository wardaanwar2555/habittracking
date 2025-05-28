from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('habits/', views.login, name='login'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname/', include('appname.urls'))  # Change 'person.url' to 'person.urls'
]
