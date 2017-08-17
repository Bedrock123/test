from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.sitemaps.views import sitemap
from django.http.response import HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.views.decorators.cache import cache_page

from BaskingRidge.sitemap import HarperSitemap
from BaskingRidge.views import (contact_static, home_static, menus_static, gallery_static, gallery_static, vendors_static, wedding_promo_static)


def handler404(request):
    # You need to create a 500.html template.
    t = loader.get_template('404.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def handler500(request):
    # You need to create a 500.html template.
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response('./common/403.html', ctx)


sitemaps = {
    'static_pages': HarperSitemap()
}

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/logout', logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^hijack/', include('hijack.urls')),
    url(r'^logout/$', logout, {'next_page': '/'},
        name='logout'),  # Log out view
    # https://godjango.com/23-robots-and-sitemaps/ Tutorial
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),


]

'''
Static Urls that serve as the frontend content. To be placed into the sitemap
'''
urlpatterns += [
    url(r'^$', home_static,
    name='home_static'),
    url(r'^menus/$', menus_static,
    name='menus_static'),
    url(r'^gallery/$', gallery_static,
    name='gallery_static'),
    url(r'^vendors/$', vendors_static,
    name='vendors_static'),
    url(r'^wedding-promo/$', wedding_promo_static,
    name='wedding_promo_static'),
    url(r'^contact/$', contact_static,
    name='contact_static'),
]

# DJANGO DEBUG TOOLBAR URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
