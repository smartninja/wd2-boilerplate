from google.appengine.ext import ndb


class Topic(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)
