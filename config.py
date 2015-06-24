config = {

    # webapp2 sessions
    'webapp2_extras.sessions': {'secret_key': '_PUT_KEY_HERE_YOUR_SECRET_KEY_'},

    # webapp2 authentication
    'webapp2_extras.auth': {'user_model': 'webapp2_extras.appengine.auth.models.User',
                            'cookie_name': 'session'},

    # application name
    'app_name': "OP Challenge",

    # the default language code for the application.
    'app_lang': 'en',
}