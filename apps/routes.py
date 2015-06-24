from webapp2_extras.routes import RedirectRoute
import handlers


secure_scheme = 'https'

_routes = [
    RedirectRoute('/login/', handlers.LoginHandler, name='login',
                  strict_slash=True),
    RedirectRoute('/logout/', handlers.LogoutHandler, name='logout',
                  strict_slash=True),
    RedirectRoute('/register/', handlers.RegisterHandler, name='register',
                  strict_slash=True),
    RedirectRoute('/messages/', handlers.MessageListHandler, name='messages',
                  strict_slash=True),
    RedirectRoute('/message/<message_id>', handlers.MessageReadHandler,
                  name='message_read', strict_slash=True),
    RedirectRoute('/messages/send', handlers.MessageSendHandler,
                  name='message_send', strict_slash=True),
    RedirectRoute('/', handlers.HomeRequestHandler, name='home',
                  strict_slash=True)
]


def get_routes():
    return _routes


def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
