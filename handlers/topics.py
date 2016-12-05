from google.appengine.api import users
from handlers.base import BaseHandler
from models.comment import Comment
from models.topic import Topic
from utils.decorators import validate_csrf


class TopicAdd(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("topic_add.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        title = self.request.get("title")
        text = self.request.get("text")

        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()  # put() saves the object in Datastore

        return self.redirect_to("topic-details", topic_id=new_topic.key.id())


class TopicDetails(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).order(Comment.created).fetch()

        params = {"topic": topic, "comments": comments}

        return self.render_template_with_csrf("topic_details.html", params=params)
