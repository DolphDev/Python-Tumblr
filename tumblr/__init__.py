from requests_oauthlib import OAuth1Session


class API_OAUTH2_URL(object):
    request_token_url = "https://www.tumblr.com/oauth/request_token" #POST
    authorize_url = "https://www.tumblr.com/oauth/authorize"
    access_token = "https://www.tumblr.com/oauth/access_token" #POST


class Api(object):

    def __init__(self, consumer_key=None, secret_key=None):
        self.has_api_key = bool(consumer_key)
        self.has_oauthkey = bool(consumer_key) and bool(secret_key)
        if self.has_api_key and self.has_oauthkey:
            oauth = OAuth1Session(consumer_key, client_secret=secret_key)
    
    def blog(self, blogname, external_url=False):
        self._blog(name)

