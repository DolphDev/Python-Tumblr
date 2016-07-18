from requests_oauthlib import OAuth1Session

class API_OAUTH1_URL(object):
    request_token_url = "https://www.tumblr.com/oauth/request_token" #POST
    authorize_url = "https://www.tumblr.com/oauth/authorize"
    access_token = "https://www.tumblr.com/oauth/access_token" #POST
    callback_url = 'https://127.0.0.1/callback'

def setup_oauth():
    client_key = input("Consumer Key: ")
    client_key_secret = input("Consumer Key: Secret: ")
    oauth = OAuth1Session(client_key, client_secret=client_key_secret)
    fetch_response = oauth.fetch_request_token(API_OAUTH1_URL.request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    authorization_url = oauth.authorization_url(API_OAUTH1_URL.authorize_url)
    print('Please go here and authorize,', authorization_url)
    redirect_response = input('Paste the full redirect URL here: ')
    oauth_response = oauth.parse_authorization_response(redirect_response)
    verifier = oauth_response.get('oauth_verifier')
    oauth = OAuth1Session(client_key,
                          client_secret=client_key_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)