import sys
import praw
import warnings


warnings.filterwarnings("ignore") # otherwise python complains about SSL

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

black  = '30'
red    = '31'
green  = '32'
yellow = '33'
blue   = '34'
purple = '35'
lblue  = '36'
white  = '37'


def color(colour, string):
    return "\033[" + colour + "m" + string + "\033[0m"

def list_posts(posts):
    length = 80
    for post in posts:
        words = str(post).split(' :: ')
        print(color(purple, '-' * length))
        print(color(white, words[1] + color(blue,' :: ')+ color(red, words[0])))
        print(color(green , post.url))
        print(len(post.comments))
    print(color(purple, '-' * length))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: reddit-cli SUBREDDIT")
        exit()
    list_posts(get_subreddit_posts(r.get_subreddit(sys.argv[1])))
