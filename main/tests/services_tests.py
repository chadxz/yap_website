from main.services import PocketService, PinboardService, LastfmService
from mock import patch


class TestPocketService:

    @staticmethod
    @patch(target="pocket.Pocket.get")
    def test_defaults(mock_get, twelve_pocket_articles):
        mock_get.return_value = twelve_pocket_articles
        pocket_client = PocketService('fake_consumer_key', 'fake_access_token')

        result = pocket_client.get_read_articles()

        mock_get.assert_called_with(detailType='complete', state='archive')
        assert len(result) == 5, "Incorrect length of items using default args"
        assert [r['item_id'] for r in result] == [
            '2675608289', '2712302873', '2485170985', '2121396419', '340082513'
        ], "Unexpected result contents"

    @staticmethod
    @patch(target="pocket.Pocket.get")
    def test_custom_count(mock_get, twelve_pocket_articles):
        mock_get.return_value = twelve_pocket_articles
        pocket_client = PocketService('fake_consumer_key', 'fake_access_token')

        result = pocket_client.get_read_articles(10)

        mock_get.assert_called_with(detailType='complete', state='archive')
        assert len(result) == 10, "Incorrect length of items using default args"
        assert [r['item_id'] for r in result] == [
            '2675608289', '2712302873', '2485170985', '2121396419', '340082513',
            '2708991016', '2535530830', '2705079041', '2700843201', '2692536740'
        ], "Unexpected result contents"

class TestPinboardService:

    @staticmethod
    @patch(target="pinboard.Pinboard.posts")
    def test_defaults(mock_recent, eight_pinboard_posts):
        mock_recent.return_value = eight_pinboard_posts
        pinboard_client = PinboardService('fake_token')

        pinboard_client.get_bookmarks()

        mock_recent.assert_called()
