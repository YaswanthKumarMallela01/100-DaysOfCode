class User:
    def __init__(self, user):
        self.user = user
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(*args, **kwargs)
        else:
            return "User is not logged in"
    return wrapper


@is_authenticated
def create_blog_post(username):
    return f"{username.user} created a new blog post."


new_user = User("Yaswanth")
# new_user.is_logged_in = True
print(create_blog_post(new_user))

"""Advanced decorators are decorators that add **real control/logic** to a function (like authentication, logging, caching) 
and work with **any inputs** using `*args` and `**kwargs`.
Here `@is_authenticated` wraps `create_blog_post()` and first checks if the given `User` object is logged in.
If `is_logged_in` is `True` it runs the function, otherwise it blocks it and returns `"User is not logged in"`.
"""

