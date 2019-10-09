from pocket import Pocket
from pinboard import Pinboard
from pylast import LastFMNetwork
from itertools import islice
import logging

logger = logging.getLogger('django.main')


class PocketService:
    def __init__(self, consumer_key, access_token):
        self.pocket_client = Pocket(
            consumer_key=consumer_key,
            access_token=access_token
        )

    def get_read_articles(self, count=5):
        logger.info('fetching pocket articles')
        pocket_result = self.pocket_client.get(
            state='archive',
            detailType='complete'
        )
        all_articles = pocket_result[0]['list']

        return list(islice((
            a for a in all_articles.values()
            if 'tags' not in a or 'private' not in a['tags']
        ), count))


class PinboardService:
    def __init__(self, token):
        self.pinboard_client = Pinboard(token)

    def get_bookmarks(self, count=5):
        logger.info('fetching pinboard posts')
        pinboard_result = self.pinboard_client.posts.recent()

        return list(islice((
            p for p in pinboard_result['posts'] if p.shared is True
        ), count))


class LastfmService:
    def __init__(self, api_key, api_secret, username):
        self.lastfm_client = LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username
        )

    def get_recent_tracks(self, count=5):
        logger.info('fetching last.fm tracks')
        user = self.lastfm_client.get_authenticated_user()

        return user.get_recent_tracks(limit=count, cacheable=False)
