from google.appengine.ext import ndb
from google.appengine.api import mail


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

        mail.send_mail(sender="my.name@gmail.com",  # add here YOUR email address (the owner of Ninja Tech Forum)
                       to=topic.author_email,  # receiver is the person who created the topic
                       subject="New comment on your topic",
                       body="""Your topic {0} received a new comment.

                       Click <a href="http://your-domain.org/topic/{1}">on this link</a> to see it""".format(topic.title,
                                                                                                             topic.key.id()))

        return comment
