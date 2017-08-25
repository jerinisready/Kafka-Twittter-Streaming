# Kafka-Twittter-Streaming
Simple Kafka Twittter Streaming  Which Streams in from Apache Kafka And Stores Data into HBASE inside HDFS File System


### ENVIRONMENT
###### Make Sure That You Have Configured :
  1. HADOOP & HDFS
  2. HBASE (localhost:9000)
  3. YARN
  4. ZOOKEEPER 
  5. KAFKA 

###### Make Sure That You Have Turned On :
  1. HADOOP HBASE
  2. YARN 
  3. HBASE Server
  4. Zookeeper (localhost:2181)
  5. Hbase Thrift
  6. KAFKA SERVER FOR PRODUCER **Streaming to TOPIC ['myWorld']**
  7. KAFKA PRODUCER CONSOLE @ localhost:9092   **Streaming to TOPIC ['myWorld']**
  8. KAFKA CONSUMER CONSOLE listining in to zookeeper @ localhost:2181 for  **Streaming to TOPIC ['myWorld']**


###### RUN THE PROGRAM
*create an ***api-keys.py*** file in the directory as per ( YOU CAN RENAME 'api-keys.py.example')*
```
KEY = 'wjRs...............fKef'    
SECRET = '3xB5n................................GWEV6HMDbPhth'
TOKEN = '14959................................7QwUIBKyRZB2QN'
TOKEN_SECRET = 'ysLFG2v..............................CA8p1GXo'

```
 ###### HAVE YOUR OWN TOKENS BY CREATING A TWITTER APP FROM [https://apps.twitter.com/]APPS.TWITTER.COM

 ###### Make Sure your installed 'requrirements.txt' contents -:  ``` pip install -r requirements.txt ```  

**Run** *( EACH ON EACH TERMINAL )* 
1. Zookeeper  [ ``` ./$ZOOKEEPER_HOME/bin/zkServer.sh  start ``` ], 
2. Kafka Server [``` ./$KAFKA_HOME/bin/kafka-server-start.sh config/server.properties  ```],
3. Create Kafka Topic [  ``` bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic myWorld ``` ]
4. Kafka Producer Console [``` ./$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic myWorld  ```  ] ,  
5. Kafka Consumer Console [``` ./$KAFKA_HOME/bin/kafka-console-consumer.sh --zookeeper localhost:2181  --topic myWorld ```  ],
6. Hbase Thrift [ ```$HBASE_HOME/bin/hbase thrift start```  ]
7. Producer : [ ``` python producer.py ``` ]
8. Consumer : [ ``` python consumer.py ``` ]


###### Make Sure You Have A table with :     [CONFIGURABLE] 
|TOPIC | 'myWorld' |
|---|---|
|TABLE NAME   | 'tweet-table' |
|COLUMN FAMILY | 'json' |
|COLUMN NAME | 'data' |



| --- |COLUMN FAMILY|
| --- | --- |
| KEY | COLUMN NAME |
| ------- | ------------------------------------------------- |
| row 1 | Data 1 |
| row 2 | Data 2 |
| row 3 | Data 3 |

HBASE STORAGE STRUCTURE
