#!/usr/bin/env python

__author__ = 'Rodrigo Augosto (@coto)'

import os
import sys

# Third party libraries path must be fixed before importing webapp2
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendors'))

# path to our app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

import webapp2

import routes

from config import config

from rest_gae.users import UserRESTHandler
from rest_gae import *

from models import MyUser
from models import Message

app = webapp2.WSGIApplication([
        RESTHandler(
          '/api/messages', # The base URL for this model's endpoints
          Message, # The model to wrap
          permissions={
            'GET': PERMISSION_ANYONE,
            'POST': PERMISSION_LOGGED_IN_USER,
            'PUT': PERMISSION_OWNER_USER,
            'DELETE': PERMISSION_ADMIN
          },

          # Will be called for every PUT, right before the model is saved (also supports callbacks for GET/POST/DELETE)
          get_callback=lambda data, user: [row for row in data if row.sent_to == user.key]
        ),
        UserRESTHandler(
            '/api/users',
            user_model=MyUser,
            user_details_permission=PERMISSION_ANYONE,
            verify_email_address=False,
            email_as_username=True,
        )
    ],
    debug=True,
    config=config
)

routes.add_routes(app)
