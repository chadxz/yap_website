from django.shortcuts import render
from dynaconf import settings
from main.services import PocketService, PinboardService, LastfmService


# Create your views here.
def main(request):
    pinboard = PinboardService(settings.get('pinboard_token'))

    pocket = PocketService(
        consumer_key=settings.get('pocket_consumer_key'),
        access_token=settings.get('pocket_access_token')
    )

    lastfm = LastfmService(
        api_key=settings.get('lastfm_api_key'),
        api_secret=settings.get('lastfm_api_secret'),
        username=settings.get('lastfm_username')
    )

    return render(request, 'main.html', {
        'bookmarks': pinboard.get_bookmarks(5),
        'tracks': lastfm.get_recent_tracks(5),
        'articles': pocket.get_read_articles(5),
        'pinboard_profile_url': settings.get('pinboard_profile_url'),
        'lastfm_profile_url': settings.get('lastfm_profile_url')
    })
