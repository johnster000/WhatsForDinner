
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls), 
    path('accounts/', include('django.contrib.auth.urls')), 

    path('dinners/', views.dinners, name='dinners'),
    path('dinners/<int:pk>', views.DinnerDetailView, name='dinner_detail'),
    path('dinners/create', views.DinnerCreateView, name='dinner_create'),
    path('dinners/<int:pk>/update', views.DinnerUpdateView, name='dinner_update'),

    path('ajax/getdinner', views.ajax_getdinner, name = 'ajax_getdinner'),
    path('ajax/getselecteddinner', views.ajax_getselecteddinner, name = 'ajax_getselecteddinner'),
    path('ajax/getrandomdinner', views.ajax_getrandomdinner, name = 'ajax_getrandomdinner'),
    path('ajax/getalldinner', views.ajax_getalldinner, name = 'ajax_getalldinner'),
    path('ajax/saveselecteddinner', views.ajax_saveselecteddinner, name = 'ajax_saveselecteddinner'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.PROD == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
