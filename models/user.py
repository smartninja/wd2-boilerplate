from google.appengine.ext import ndb


class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    admin = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_or_create(cls, email):
        user = User.query(User.email == email).get()  # check if user already exists in the database

        if not user:
            # if user does not exist yet, create a new one
            user = User(email=email)
            user.put()

        return user
