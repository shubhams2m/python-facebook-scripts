import facebook
import requests

access_token = "EAACEdEose0cBAIEY2JMIHL3SI9t63tHWoBeL7Uq51RIL64mTNbh7R8JwRe8D65oqGOctA6MjZBxnUyLLqrlOZA8WzbtJ3vjYyZAt5zrZAlwrzluMK4eZA5MWoZCETgUEZAqEBVc87csqvWHr3Y0tdBfVwIWvkR0YUO1fOJHBjFmZCwZDZD"

graph = facebook.GraphAPI(access_token)

pages = graph.get_connections('me', 'likes')

count = 0


if "paging" in pages:

    while "next" in pages["paging"]:
        for page in pages["data"]:
            count+=1
            print page["name"]
            # Attempt to make a request to the next page of data, if it exists.
        pages=requests.get(pages['paging']['next']).json()


#for last set of pages
for page in pages["data"]:
    count+=1
    print page["name"]

#print total number of pages liked
print "total", count

