from google.appengine.ext import ndb


class Comment(ndb.Model):
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    topic_id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)
