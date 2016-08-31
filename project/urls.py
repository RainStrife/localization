from django.conf.urls import url, include
from django.contrib import admin
import core.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(core.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n'))
]
