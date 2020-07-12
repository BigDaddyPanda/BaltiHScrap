# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:36:39 2020

@author: asus
"""

from tiktok_bot import TikTokBot

bot = TikTokBot()

# getting your feed (list of posts)
my_feed = bot.list_for_you_feed(count=25)

popular_posts = [post for post in my_feed if post.statistics.play_count > 1_000_000]

# extract video urls without watermark (every post has helpers)
urls = [post.video_url_without_watermark for post in popular_posts]

# searching videos by hashtag name
posts = bot.search_posts_by_hashtag("cat", count=50)
from pprint import pprint
pprint(posts)