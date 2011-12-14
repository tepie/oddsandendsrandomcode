#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import memcache

import social_keys
import model
import os,logging,json
import datetime,time

from tweepy.auth import OAuthHandler
from tweepy.auth import API
from tweepy.error import TweepError

class DailyMixHandler(webapp.RequestHandler):
    def get(self): pass

def main():
    application = webapp.WSGIApplication([('/', DailyMixHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
