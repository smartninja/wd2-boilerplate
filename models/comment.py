from google.appengine.ext import ndb
from google.appengine.api import taskqueue


class Comment(ndb.Model):
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    topic_id = ndb.IntegerProperty()
    topic_title = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def create(cls, content, user, topic):
        comment = Comment(content=content, author_email=user.email(), topic_id=topic.key.id(), topic_title=topic.title)
        comment.put()

        # run background task to send email to topic author
        taskqueue.add(url='/task/email-new-comment', params={"topic_author_email": topic.author_email,
                                                             "topic_title": topic.title,
                                                             "topic_id": topic.key.id()})

        return comment
