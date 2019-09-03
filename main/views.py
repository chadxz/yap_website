from django.shortcuts import render
from dynaconf import settings
import pylast
import pinboard
from pocket import Pocket


# Create your views here.
def main(request):
    # articles
    pocket = Pocket(
        consumer_key=settings.get('pocket_consumer_key'),
        access_token=settings.get('pocket_access_token')
    )
    pocket_result = pocket.get(state='archive', detailType='complete', count=5)
    all_articles = pocket_result[0]['list']
    articles = [
        a for a in all_articles.values()
        if 'tags' not in a or 'private' not in a['tags']
    ]

    # bookmarks
    pb = pinboard.Pinboard(settings.get('pinboard_token'))
    pinboard_result = pb.posts.recent()
    bookmarks = [p for p in pinboard_result['posts'][:5] if p.shared is True]

    # tracks
    lastfm = pylast.LastFMNetwork(
        api_key=settings.get('lastfm_api_key'),
        api_secret=settings.get('lastfm_api_secret'),
        username=settings.get('lastfm_api_username')
    )
    user = lastfm.get_authenticated_user()
    tracks = user.get_recent_tracks(limit=5, cacheable=False)

    return render(request, 'main.html', {
        'bookmarks': bookmarks,
        'tracks': tracks,
        'articles': articles,
        'pinboard_profile_url': settings.get('pinboard_profile_url'),
        'lastfm_profile_url': settings.get('lastfm_profile_url')
    })
