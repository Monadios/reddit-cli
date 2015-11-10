import praw

r = praw.Reddit(user_agent='reddit-cli')
sub = r.get_subreddit('linux')
comments = []

def get_subreddit_posts(subreddit, post_limit):
    posts = []
    for post in subreddit.get_hot(limit=post_limit):
        posts.append(str(post))
    return posts

def list_posts(posts):
    for post in posts: print(post)
