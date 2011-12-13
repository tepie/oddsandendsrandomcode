from google.appengine.ext import db

class SocialKeysForUsers(db.Model):
    user_id = db.StringProperty(required=True)
    access_token_key = db.StringProperty()
    access_token_secret = db.StringProperty()
    request_token_key = db.StringProperty()
    request_token_secret = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
class SocialPostsForUsers(db.Model):
    social_user = db.ReferenceProperty(SocialKeysForUsers,collection_name='social_user',required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    text = db.StringProperty(required=True)