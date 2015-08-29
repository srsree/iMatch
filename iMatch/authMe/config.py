# config.py

from authomatic.providers import oauth2, oauth1, openid

CONFIG = {
    
    'tw': { # Your internal provider name
        
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1489782111336102',
        'consumer_secret': '5f05e77c19c63fa955b1863bf5d2a82a',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    
    'oi': {
           
        # OpenID provider dependent on the python-openid package.
        'class_': openid.OpenID,
    }
}
