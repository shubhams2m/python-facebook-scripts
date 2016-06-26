#!/usr/bin/env python
# -*- coding: utf-8 -*-


import facebook
import requests

access_token = "EAACEdEose0cBAL502L0Wo5PaehnDKafUdSPirW00fdY1Hkj9rmTYk84dY4Kug4GzFTLoEFoNHRXkidrUxR89ZATGm2l6xATaDdntwZCRq0jrUlqbYKK0sAPsIZBMYgZBrJM44fBfPgqbqtAyQHplyW6bxpIqxcmixKqF3PZAQ6wZDZD"

graph = facebook.GraphAPI(access_token)

posts = graph.get_connections('me', 'posts')

count = 0


while "next" in posts["paging"]:
        for post in posts["data"]:
            if "message" in post:
                print post["message"]
                f = open("posts.txt", "a")
                f.write((post["message"]).encode("utf-8"))
                f.write("\n \n")
            # Attempt to make a request to the next page of data, if it exists.
        posts=requests.get(posts['paging']['next']).json()


#for last set of posts
for post in posts["data"]:
    if "message" in post:
        print post["message"]
        f = open("posts.txt", "a")
        f.write((post["message"]).encode("utf-8"))
        f.write("\n \n")
