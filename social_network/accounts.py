class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        self.following_users_posts = []
    
    def add_post(self, post):
        self.posts.append(post)
        post.user = self
        post_class = post.__class__
        post_class.user = post.user
        
    def get_timeline(self):
        posts = []
        for user in self.following:
            posts += user.posts
        return sorted(posts, key=lambda p: p.timestamp, reverse=False)
        
    def follow(self, other):
        self.following.append(other)