from django.conf.urls import patterns, url

urlpatterns = patterns('network.views',
    url(r'^receive/data$', 'receive_data'),
)