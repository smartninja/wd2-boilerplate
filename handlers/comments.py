from handlers.base import BaseHandler
from google.appengine.api import users
from models.comment import Comment
from models.topic import Topic
from utils.decorators import validate_csrf


class CommentAdd(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        text = self.request.get("comment-text")
        topic = Topic.get_by_id(int(topic_id))

        comment = Comment(content=text, author_email=user.email(), topic_id=topic.key.id(), topic_title=topic.title)
        comment.put()

        return self.redirect_to("topic-details", topic_id=topic.key.id())
