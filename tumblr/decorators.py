from core import exceptions

def api_key_required(f):
    def wrapper(obj, *args, **kwargs):
        if obj.api_mother.has_api_key is False:
            raise exceptions.AuthenticationError("An API key is required for this endpoint")
        return f(*args, **kwargs)
    return wrapper

def oauth_required(func):
    def wrapper(obj, *args, **kwargs):
        if obj.api_mother.has_oauthkey is False:
            raise exceptions.AuthenticationError("Oauth1 connection is required for this endpoint")
        return f(*args, **kwargs)
    return wrapper
