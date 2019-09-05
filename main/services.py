from pocket import Pocket
from pinboard import Pinboard
from pylast import LastFMNetwork
import logging

logger = logging.getLogger('django.main')


class PocketService:
    def __init__(self, consumer_key, access_token):
        self.consumer_key = consumer_key
        self.access_token = access_token

    def get_read_articles(self, count=5):
        pocket = Pocket(
            consumer_key=self.consumer_key,
            access_token=self.access_token
        )

        logger.info('fetching pocket articles')
        pocket_result = pocket.get(
            state='archive',
            detailType='complete',
            count=count
        )
        all_articles = pocket_result[0]['list']

        return [
            a for a in all_articles.values()
            if 'tags' not in a or 'private' not in a['tags']
        ]


class PinboardService:
    def __init__(self, token):
        self.token = token

    def get_bookmarks(self, count):
        pb = Pinboard(self.token)

        logger.info('fetching pinboard posts')
        pinboard_result = pb.posts.recent()

        return [p for p in pinboard_result['posts'][:count] if p.shared is True]


class LastfmService:
    def __init__(self, api_key, api_secret, username):
        self.api_key = api_key
        self.api_secret = api_secret
        self.username = username

    def get_recent_tracks(self, count):
        lastfm = LastFMNetwork(
            api_key=self.api_key,
            api_secret=self.api_secret,
            username=self.username
        )

        logger.info('fetching last.fm tracks')
        user = lastfm.get_authenticated_user()

        return user.get_recent_tracks(limit=count, cacheable=False)
