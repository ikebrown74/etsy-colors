from webcolors import name_to_hex, hex_to_name
from django.http import Http404
from etsy import Etsy
from annoying.decorators import render_to
from django.conf import settings
from django.views.decorators.cache import cache_page

@cache_page(20 * 60)
@render_to('etsy_listings.html')
def etsy_colors(request, color):
    try:
        color_hex = name_to_hex(color)
    except ValueError:
        raise Http404('Color not valid')
    
    etsy = Etsy(settings.ETSY_CONSUMER_KEY, settings.ETSY_SHARED_SECRET)

    response = etsy.show_listings(color=color_hex)
    results = response['results']
    
    if not results:
        raise Http404('no results')
    
    listings = []
    for item in results:
        listing = {}
        listing['url'] = item['url']
        listing['title'] = item['title']
        result = etsy.get_image_for_listing(item['listing_id'])
        image_url = result['results'][0]['url_170x135']
        listing['image_url'] = image_url
        listings.append(listing)
        
    return {'listings': listings, 'color': color}