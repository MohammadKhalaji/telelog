#! /usr/bin/python3

from telethon import TelegramClient, events, sync
import os 
import subprocess
import redis 
from datetime import datetime

hostname = subprocess.check_output("hostname").decode("utf-8").replace("\n", "")
telelog_dir = os.getenv("TELELOG_DIR")
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
recipient = os.getenv("TELEGRAM_RECIPIENT")
channel_name = os.getenv("TELEGRAM_REDIS_CHANNEL")

redis_client = redis.Redis(host='localhost', port=6379, db=0)
pubsub = redis_client.pubsub()
pubsub.subscribe(channel_name)

with TelegramClient(f'{telelog_dir}/telegram_sessions/{hostname}.session', api_id, api_hash) as client:
    client.start()
    
    for message in pubsub.listen(): 
        if message['type'] != 'message': 
            continue
        message = message['data'].decode('utf-8')
        client.send_message(recipient, f"{hostname} - {datetime.now()}\n`{message}`")