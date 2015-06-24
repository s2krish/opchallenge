import os

import webapp2
from webapp2_extras import auth
from webapp2_extras import sessions
from webapp2_extras.auth import InvalidAuthIdError, InvalidPasswordError
from google.appengine.ext.webapp import template

from models import Message
from models import MyUser


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def template_path(self):
        return os.path.dirname(os.path.dirname(__file__))

    @webapp2.cached_property
    def user_model(self):
        return self.auth.store.user_model

    @webapp2.cached_property
    def auth(self):
        return auth.get_auth()

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    @webapp2.cached_property
    def user(self):
        return self.auth.get_user_by_session()

    @webapp2.cached_property
    def messages(self):
        return self.session.get_flashes(key='_messages')

    def add_message(self, message, level=None):
        self.session.add_flash(message, level, key='_messages')


class MessageListHandler(BaseHandler):
    def get(self):
        m = Message.query().fetch()
        # message = m.query.query()

        self.response.write(m)


class MessageReadHandler(BaseHandler):
    def get(self, message_id):
        self.response.write('tuk tuk readign message!')


class MessageSendHandler(BaseHandler):
    def get(self):
        user = MyUser.get_by_auth_id('krish5@gmail.com')
        # self.response.write(user)
        m = Message(
            sent_by=user.key,
            sent_to=user.key,
            subject='Message Subject',
            message='Message Body'
        )
        m.put()

    def post(self):
        # send message from here
        pass


class RegisterHandler(BaseHandler):
    def get(self):
        self.response.write('Register!!!')

    def post(self):
        u = self.user_model()
        u.create_user(
            'krish1@gmail.com',
            ['email'],
            email='krish1@gmail.com',
            password_raw='12121212'
        )
        u.put()


class LoginHandler(BaseHandler):
    def get(self):

        from rest_gae.users import User
        # u = User()
        # u.create_user('krish2@gmail.com', ['email'], email='krish2@gmail.com', password_raw='12121212')
        # u.put()

        u2 = User.get_by_auth_id('krish1@gmail.com')
        self.response.write(u2)

        user = self.user_model.get_by_auth_id('krish1@gmail.com')
        if user:
            auth_id = user.auth_ids[0]
        else:
            raise InvalidAuthIdError

        password = '12121212'

        try:
            self.auth.get_user_by_password(
                auth_id,
                password,
                remember=True
            )
        except (InvalidAuthIdError, InvalidPasswordError), e:
            # Returns error message to self.response.write in
            # the BaseHandler.dispatcher
            message = "username or password is incorrect."
            self.add_message(message, 'danger')
            # self.redirect_to('login', continue_url=continue_url) if continue_url else self.redirect_to('login')
            self.response.write("error here")

    def post(self):
        pass


class LogoutHandler(BaseHandler):
    def get(self):
        self.auth.unset_session()
        self.response.write("at logout!")


class HomeRequestHandler(BaseHandler):
    def get(self):
        path = os.path.join(self.template_path, 'index.html')
        self.response.out.write(template.render(path, {}))
