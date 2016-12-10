from google.appengine.ext import ndb


class Comment(ndb.Model):
    content = ndb.TextProperty()
    author_id = ndb.IntegerProperty()
    author_full_name = ndb.StringProperty()
    topic_id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)
