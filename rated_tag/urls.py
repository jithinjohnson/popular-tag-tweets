
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^home/(?P<tag_name>.*)/$', views.check, name='details'),
    url(r'^home/$', views.home, name='home'),

]
