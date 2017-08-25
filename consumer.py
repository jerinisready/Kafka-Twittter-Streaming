#########################################
#  AUTHER : jerinisready		#
#  DATE : 20th AUGUST 2017		#
#  PYTHON PACKAGE FILE			#
#  CODE SNIPPETS			#
#########################################



import re
import sys
import json
from kafka import KafkaConsumer
from kafka import TopicPartition
import happybase

############## DATA STORE ###############
## SERVER ##
MASTER = 'localhost'
PORT = 9090
BOOTSTRAP_SERVERS = 'localhost:9092,localhost:9093,localhost:9094'

## HBASE TABLE SPECIFIC ##
LISTENING_TOPIC = 'myWorld'
HBASE_TABLE_NAME = 'tweet-table'
HBASE_TABLE_COLUMN_FAMILY_NAME = "json"
HBASE_TABLE_COLUMN_NAME = "data"

COLUMN = b"%s:%s" % ( HBASE_TABLE_COLUMN_FAMILY_NAME, HBASE_TABLE_COLUMN_NAME )

# kafka_attributes = "topic partition offset timestamp timestamp_type timestamp_type key value checksum serialized_key_size serialized_value_size".split()

#########################################


connection = happybase.Connection(MASTER)
twitter_stream_from_kafka_consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                     value_deserializer=lambda v: json.dumps(v.decode('string_escape')).decode('string_escape').decode('string_escape') )

twitter_stream_from_kafka_consumer.subscribe([LISTENING_TOPIC])
counter = 1

########### DATA TABLE STRUCTURE ########################################################################
# DEBUG #     table = connection.table(TABLE)
# DEBUG #     table.put( "row",{ b"col-family:column" : b"DUMMY DATA  TO BE STORED AT HBASE"  }  )
# DEBUG #     print(connection.tables())
#########################################################################################################


hbase_table = connection.table(HBASE_TABLE_NAME)

for tweet in twitter_stream_from_kafka_consumer:

    # print u"  TOPIC :  {0}".format( tweet.topic )
    # print u"  PARTITION :  {0}".format( tweet.partition )
    # print u"  OFFSET :  {0}".format( tweet.offset )
    # print u"  TIMESTAMP :  {0}".format( tweet.timestamp )
    # print u"  TIMESTAMP TYPE {0}".format( tweet.timestamp_type )
    # print u"  KEY :  {0}".format( tweet.key )
    # print u"  CHECKSUM :  {0}".format( tweet.checksum )
    # print u"  SERIALIZED KEY SIZE :  {0}".format( tweet.serialized_key_size )
    # print u"  SERIALIZED VALUE SIZE :  {0}".format( tweet.serialized_value_size )
    # print u"  VALUE :  {0}".format( tweet.value.decode('string_escape') )
    # print " . "
    row_name = "row%d" % counter
    hbase_table_row = hbase_table.put(row_name, { COLUMN : b"%s" % tweet.value })
    counter+=1


# RECEIEVE TWEETS FROM PRODUCER.
# for tweet in twitter_stream_from_kafka_consumer:
#      print (tweet)
#      row_name = "row-%s" % counter
#      hbase_table_row = hbase_table.put(row_name, { COLUMN : b"%s" % tweet })
