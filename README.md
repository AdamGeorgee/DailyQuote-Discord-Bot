# DailyQuote Discord Bot 🤖

A Python Discord bot that automatically selects a random message from a designated "quotes" channel and posts it to a "Quote of the Day" channel once every 24 hours.

## 🚀 Features
* **Automated Scheduling:** Uses `discord.ext.tasks` to run a 24-hour loop.
* **Random Selection:** Fetches message history and picks a quote at random.
* **Cloud Ready:** Optimized for 24/7 hosting on a VPS (Oracle Cloud/Ubuntu) using PM2.
* **Environment Security:** Uses `.env` files to keep Discord tokens and Channel IDs private.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Library:** [discord.py](https://github.com/Rapptz/discord.py)
* **Process Manager:** [PM2](https://pm2.keymetrics.io/)
* **Hosting:** Oracle Cloud (Ubuntu 24.04)

## 📋 Setup & Installation

### Local Configuration
1. Clone the repository
2. Create a .env file in the root directory:
  * DISCORD_TOKEN = your_token_here
  * QUOTES_CHANNELID = your_quotes_channel_id
  * DAILY_QUOTE_CHANNELID = your_daily_quote_channel_id
4. Run python main.py
