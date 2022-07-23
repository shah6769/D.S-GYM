
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.views.static import serve
 
from django.conf.urls.static import static

admin.site.site_header = "D.S GYM"
admin.site.site_title = "D.S GYM PORTAL"
admin.site.index_title = "WELCOME TO OUR GYM WEBSITE PORTAL"

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('home.urls')),
#      url(r'^media/(?P<path>.*)$', serve,{'document_root':         settings.MEDIA_ROOT}), 
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
 ]
