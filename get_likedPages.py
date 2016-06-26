#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import requests

access_token = "EAACEdEose0cBADEQC2MnrmS0iZAVjbFEUbtI5KxNZBw0Tm4D4Xm7RQlx0I8pmOO2uS5VXzolZBc3Mtl9ABeZC5B2U23S3CPgnMrzPzHuHzko0e8iEHxWXBiIkadLpuk83pvL2SrYoZAZCLsMkKqRX1y5ZATUNeZB9kUMQqUj3xFZBrwZDZD"

graph = facebook.GraphAPI(access_token)

pages = graph.get_connections('me', 'likes')

count = 0


if "paging" in pages:

    while "next" in pages["paging"]:
        for page in pages["data"]:
            count+=1
            print page["name"]

            f.write(page["name"]

            # Attempt to make a request to the next page of data, if it exists.
        pages=requests.get(pages['paging']['next']).json()


#for last set of pages
for page in pages["data"]:
    count+=1
    print page["name"]

#print total number of pages liked
print "total", count

