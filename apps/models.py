
from google.appengine.ext import ndb
from rest_gae.users import User


class MyUser(User):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()


class Message(ndb.Model):
    sent_by = ndb.KeyProperty(kind=MyUser)
    sent_to = ndb.KeyProperty(kind=MyUser)
    subject = ndb.StringProperty()
    message = ndb.StringProperty()
    sent_date = ndb.DateTimeProperty(auto_now_add=True)
    sender_read = ndb.BooleanProperty(default=False)
    receiver_read = ndb.BooleanProperty(default=False)

    class RESTMeta:
        user_owner_property = 'sent_by'
