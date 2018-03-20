# student-discord-bot

Imagine if you're a student, and you want to get important information about your studies anytime and anywhere at the tip of your fngertips.
This is what this project is all about, the objective of which is to show how can a system consisting of the Discord platform
together with a bot can be used to present information to the students. This project uses Python and 
[discord.py](https://github.com/Rapptz/discord.py/) - the API wrapper for Discord written in Python.

[![PyPI](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![PyPI](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)

## Prerequisites
- Python 3.4.2+
- `aiohttp` library
- `websockets` library

## Installation
- Python 3.4.2+ can be downloaded [here](https://www.python.org/)
- You can install the discord.py library without full voice support by running this on your command:
```
python3 pip install discord.py
```

## Code
Note: In Python 3.4 you use:
- `@asyncio.coroutine` instead of `async def` and 
- `yield from` instead of `await`

## Update Bot Configuration
- `bot_token`
- `bot_channel_id`

## Run
```sh
$ python bot.py
```
