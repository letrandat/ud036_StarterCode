import json

import requests

import constants


class TheMovieDB(object):
    """
    Simple API manager to query data from The Movie DB
    """
    def __init__(self, api_key):
        """
            Init API Key
        """
        self.api_key = api_key

    def discover_movies(self, sort_by=None):
        """
            Return list of `sort_by` movies
            params:
                sort_by: can be either None or popularity.asc
            return: success, list_of_movies
        """
        payload = {
            'api_key': self.api_key
        }
        if sort_by:
            payload['sort_by'] = sort_by
        response = requests.request("GET", constants.DISCOVER_URL, data=payload)

        success = False
        if response.status_code == 200:
            success = True
            content = json.loads(response.content)
            result = content.get('results', [])
            return success, result

        return success, []

    def get_movie_trailer(self, movie_id):
        """
        Return Youtube video trailer
        :param movie_id:
        :return:
            success, url
            * empty if the not youtube or no trailer at all
        """
        url = constants.GET_VIDEO_URL.format(movie_id=movie_id)
        payload = {
            'api_key': self.api_key
        }
        response = requests.request("GET", url, data=payload)
        success = False
        if response.status_code == 200:
            success = True
            content = json.loads(response.content)
            result = content.get('results', [])
            youtube_url = "https://www.youtube.com/watch?v=" + result[0]["key"]
            return success, youtube_url

        return success, ''
