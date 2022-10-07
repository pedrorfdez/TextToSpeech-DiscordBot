# Setup Guide

## PIP packages

Install required pip packages with:

```
pip install asyncio discord discord.py gTTS python-dotnev
```

## Include your Discord Token

At line 12 in **textToSpeech.py** file:

```
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
```

Change `os.getenv('DISCORD_TOKEN')` to your own Discord Token.

> **REMEMBER:** your Token is a **string**, so don't forget your **'quotes'**!

## Run & Enjoy! ^^
