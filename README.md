# telelog

Telegram logger for long experiments. 

First, install the dependencies: 
* Redis
* Redis client for python
* Telethon 
* Sqlite (required by Telethon)

Make sure the redis redis server is running: 
```
redis-cli ping
```

Set the appropriate environment variables in `~/.bashrc`: 
```
export TELELOG_DIR="YOUR_PATH_TO_TELELOG"
export PATH=$TELELOG_DIR:$PATH
export TELEGRAM_API_ID="YOUR API ID"
export TELEGRAM_API_HASH="YOUR API HASH"
export TELEGRAM_RECIPIENT="YOUR RECIPIENT'S ID IN TELEGRAM"
export TELEGRAM_REDIS_CHANNEL="telegram_queue"

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

Netflix and log :)
```
telelog "Hello world"
```