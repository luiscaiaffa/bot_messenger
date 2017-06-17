from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include('bot.urls', namespace="bot")),
    url(r'^admin/', include(admin.site.urls)),
]
