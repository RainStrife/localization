from django.conf.urls import url, include
from django.contrib import admin
import core.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(core.urls)),
]
