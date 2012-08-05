from django.conf.urls.defaults import *

urlpatterns = patterns('etsy_colors.views',
    url(r'^etsy-(?P<color>\w+)$', "etsy_colors", name="etsy_colors"),
)