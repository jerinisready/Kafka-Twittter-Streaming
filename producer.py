#########################################
#  AUTHER : jerinisready		#
#  DATE : 20th AUGUST 2017		#
#  PYTHON PACKAGE FILE			#
#  CODE SNIPPETS			#
#########################################




# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import json
import api_keys
from requests_oauthlib import OAuth1Session
import json
import sys


########## DATA STORE ##########
## SERVER ##
MASTER = 'localhost'
PORT = 9090
BOOTSTRAP_SERVERS = 'localhost:9092'

## HBASE TABLE SPECIFIC ##
TOPIC = 'myWorld'
TABLE = 'tweet-table'
COLUMN_FAMILY = "json"
COLUMN_NAME = "data"


################################

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,)

hashtag = "twitter"
twitter = OAuth1Session(api_keys.KEY,
                        client_secret=api_keys.SECRET,
                        resource_owner_key=api_keys.TOKEN,
                        resource_owner_secret=api_keys.TOKEN_SECRET)

r = twitter.post( 'https://stream.twitter.com/1.1/statuses/filter.json', data={ 'track': hashtag }, stream=True )

for line in r.iter_lines():
    if line:
        producer.send('myWorld', key="post", value=b'%s'%line).get(timeout=60)
        # print line
producer.flush()
