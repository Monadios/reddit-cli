import sys
import praw
import warnings


warnings.filterwarnings("ignore")

r = praw.Reddit(user_agent='reddit-cli')
sub = r.get_subreddit('linux')
comments = []

def get_subreddit_posts(subreddit, post_limit=None):
    if post_limit == None:
        post_limit = 10
        
    posts = []
    for post in subreddit.get_hot(limit=post_limit):
        posts.append(post)
    return posts

def list_posts(posts):
    for post in posts:
        words = str(post).split(' :: ')
        length = 80
        print(words[1] + ' :: ' + words[0])
        print(post.url)
        print('-' * length)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: reddit-cli URL")
        exit()
    list_posts(get_subreddit_posts(r.get_subreddit(sys.argv[1])))
