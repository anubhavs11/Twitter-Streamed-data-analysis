#!/usr/bin/env python
import json
import sys
import re

 
tweets_data = []
tweets_file = sys.stdin
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

for text in tweets_data:
	
	tweet = text['text'].lower()
	
	if(re.search("java",tweet)):
		print("java",1)

	if(re.search("python",tweet)):
		print("python",1)

	if(re.search("cpp",tweet)):
		print("cpp",1)
    
    
