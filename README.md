# telelog

Telegram logger for long experiments. 

First, install the dependencies: 
* [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
* [Redis client for python](https://github.com/redis/redis-py)
* [Telethon](https://github.com/LonamiWebs/Telethon)
* Sqlite (required by Telethon)


Get your Telegram API working: 
 
* [Get API ID and API Hash from Telegram](https://my.telegram.org/)
* [Get a bot token from BotFather](https://telegram.me/BotFather)
* Start your bot in your Telegram. Bots cannot start conversations, so this step is necessary. 

Set the appropriate environment variables in `~/.bashrc`: 
```
export TELELOG_DIR="YOUR_PATH_TO_TELELOG"
export PATH=$TELELOG_DIR:$PATH
export TELEGRAM_API_ID="YOUR API ID"
export TELEGRAM_API_HASH="YOUR API HASH"
export TELEGRAM_BOT_TOKEN="YOUR BOT TOKEN ACQUIRED FROM BOTFATHER"
export TELEGRAM_RECIPIENT="YOUR RECIPIENT'S ID IN TELEGRAM"
export TELEGRAM_REDIS_CHANNEL="telegram_queue"
```

Make sure the redis server is running: 
```
redis-cli ping
```

Set the correct permissions: 
```
chmod +x init_telegram_client.py 
chmod +x telelog_worker.py
chmod +x telelog
chmod +w init_telegram_client.py
chmod +w telelog_worker.py
```


Initialize your telegram session (You will be asked to provide your phone number, password, and a verification code): 
```
python3 init_telegram_client.py
```


Make sure the telelog worker is running (This step can be skipped since the `telelog` command will run the worker if it's not already running): 
```
python3 telelog_worker.py &
```

You might want to use `taskset` to bind it to a specific processor. In this example, it is binded to the last one. 
```
taskset -c $((`nproc` - 1)) python3 telelog_worker.py & 
```


Netflix and log :)

From the command line: 
```
telelog "Hello world"
```

From a python script: 
```python3
import os
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

channel_name = os.getenv("TELEGRAM_REDIS_CHANNEL")
r.publish(channel_name, "Hello world")
```