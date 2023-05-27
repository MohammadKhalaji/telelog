#! /usr/bin/python3

from telethon import TelegramClient, events, sync
import os
import subprocess

hostname = subprocess.check_output("hostname").decode("utf-8").replace("\n", "")
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
recipient = os.getenv("TELEGRAM_RECIPIENT")
telelog_dir = os.getenv("TELELOG_DIR")

with TelegramClient(f'{telelog_dir}/telegram_sessions/{hostname}.session', api_id, api_hash) as client:
    client.start(bot_token=bot_token)