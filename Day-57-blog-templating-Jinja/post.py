class Post:
    def __init__(self, post_id, blog_posts) -> None:
        self.blog_title = blog_posts[post_id-1]['title']
        self.blog_subtitle = blog_posts[post_id-1]["subtitle"]
        self.blog_body = blog_posts[post_id-1]["body"]