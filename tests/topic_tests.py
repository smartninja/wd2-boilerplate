import os
import unittest
import uuid
import webapp2
import webtest

from google.appengine.ext import testbed
from google.appengine.api import memcache
from handlers.topics import TopicAdd, TopicDetails
from models.topic import Topic


class TopicTests(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication(
            [
                webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
                webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
            ])

        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        """ Uncomment the stubs that you need to run tests. """
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # self.testbed.init_mail_stub()
        # self.testbed.init_taskqueue_stub()
        self.testbed.init_user_stub()
        # ...

        """ Uncomment if you need user (Google Login) and if this user needs to be admin. """
        os.environ['USER_EMAIL'] = 'some.user@example.com'
        # os.environ['USER_IS_ADMIN'] = '1'

    def tearDown(self):
        self.testbed.deactivate()

    def test_topic_add_handler(self):
        # GET
        get = self.testapp.get('/topic/add')  # do a GET request
        self.assertEqual(get.status_int, 200)

        # POST
        csrf_token = str(uuid.uuid4())  # create a CSRF token
        memcache.add(key=csrf_token, value=True, time=600)  # save token to memcache

        title = "Some new topic"
        text = "This is a new topic. Just for testing purposes."

        params = {"title": title, "text": text, "csrf_token": csrf_token}

        post = self.testapp.post('/topic/add', params)  # do a POST request
        self.assertEqual(post.status_int, 302)  # 302 means "redirect" - this is what we do at the end of POST method in TopicAdd handler

        topic = Topic.query().get()  # get the topic create by this text (it's the only one in this fake database)
        self.assertTrue(topic.title, title)  # check if topic title is the same as we wrote above
        self.assertTrue(topic.content, text)
