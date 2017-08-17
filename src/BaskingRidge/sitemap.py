from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class HarperSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'home_static',
            
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {'views': HarperSitemap}
