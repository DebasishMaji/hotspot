from django.conf import settings
import requests


class YouTubeV3Data(object):
    API_KEY = "AIzaSyD2M7OqRsXGYLH2zR9ieZMSJ2lKoxXPVgA"
    BASE_URL = "https://www.googleapis.com/youtube/"

    def __init__(self):
        self.API_KEY = settings.API_KEY
        self.BASE_URL = settings.BASE_URL

    @staticmethod
    def get_latest_videos(publishedAfter):
        query = {
            "type": "video",
            "order": "date",
            "key": "AIzaSyD2M7OqRsXGYLH2zR9ieZMSJ2lKoxXPVgA"
            # "publishedAfter": publishedAfter
        }

        try:
            r = requests.post(
                url="https://www.googleapis.com/youtube/v3/search",
                params=query,
                timeout=5
            )
            print(r.json())
        except (requests.Timeout, requests.RequestException, requests.HTTPError, requests.ConnectionError):
            raise Exception("Request Error. Query - {query}".format(query=str(query)))
        except TypeError:
            raise Exception(
                "Payload could not be converted to valid JSON. Query - {query}".format(query=str(query)))
        except Exception:
            raise Exception("Unknown Exception caught")

        if not r.ok:
            raise Exception(
                "Search failed with status_code:{status_code} and response: {response}".format(
                    status_code=r.status_code, response=r.text))

        return r.json()
