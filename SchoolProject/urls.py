from django.contrib import admin
from django.urls import include, path
from StudentApp import views
from django.conf import settings
urlpatterns = [
    path('student/', views.studentApi),
    path('profesor/', views.profesorApi),
    path('curso/', views.cursoApi),
    path('student/<int:id>/', views.studentApi),
    path('profesor/<int:id>/', views.profesorApi),
    path('curso/<int:id>/', views.cursoApi),
    path('admin/', admin.site.urls),
    
    
    path('', include('django.contrib.auth.urls')),
    
]


#conf extend media
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)