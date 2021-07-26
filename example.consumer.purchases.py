import asyncio
from dataclasses import dataclass, field
import json

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic


BROKER_URL = "PLAINTEXT://localhost:29092"
TOPIC_NAME = "up.tcc.example.purchases"



        
def main():
    """Checks for topic and creates the topic if it does not exist"""
    try:
        asyncio.run(produce_consume())
    except KeyboardInterrupt as e:
        print("shutting down")

    
async def produce_consume():
    """Runs the Producer and Consumer tasks"""
    t2 = asyncio.create_task(_consume(TOPIC_NAME))

    await t2

  
async def _consume(topic_name):
    """Consumes data from the Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])
    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(2.5)

if __name__ == "__main__":
    main()
