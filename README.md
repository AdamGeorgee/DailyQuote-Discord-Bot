# DailyQuote Discord Bot 🤖

A Python Discord bot that automatically selects a random message from a designated "quotes" channel and posts it to a "Quote of the Day" channel once every 24 hours.

## 🚀 Features
* **Automated Scheduling:** Uses `discord.ext.tasks` to run a 24-hour loop.
* **Random Selection:** Fetches message history and picks a quote at random.
* **Environment Security:** Uses a `.env` file to keep Discord tokens and Channel IDs private.
* **Cloud Ready:** Optimized for 24/7 hosting on a VPS (Oracle Cloud/Ubuntu) using PM2.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Library:** [discord.py](https://github.com/Rapptz/discord.py)
* **Process Manager:** [PM2](https://pm2.keymetrics.io/)
* **Hosting:** Oracle Cloud (Ubuntu 24.04)

## 📋 Setup & Installation

### Local Configuration

**A. Discord Developer Portal Setup**
1. Create a new Application at the [Discord Developer Portal](https://discord.com/developers/applications).
2. Under the Bot tab:
   * Privileged Gateway Intents: Toggle **ON** the `Message Content Intent`.
   * Reset/Copy your Bot Token for the next step.
3. Under the OAuth2 > URL Generator tab:
   * Scopes: Select `bot`.
   * Bot Permissions: Select `View Channels`, `Send Messages`, and `Read Message History`.
   * Use the generated URL to invite the bot to your server.

**B. Project Environment**
1. Clone the repository
2. Create a .env file in the root directory:  
```text
DISCORD_TOKEN = your_token_here
QUOTES_CHANNELID = your_quotes_channel_id
DAILY_QUOTE_CHANNELID = your_daily_quote_channel_id
```


4. Run python main.py
