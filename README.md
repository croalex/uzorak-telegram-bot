# Uzorak Lab Telegram Bot

Professional peptide testing service bot for [Uzorak Lab](https://uzorak.com).

## Features

- Welcome message with company information
- Quick access buttons to:
  - Uzorak Telegram Channel
  - Uzorak.com website
  - Sample Certificate of Analysis (COA)

## Deployment

This bot is deployed on Railway.app for 24/7 availability.

### Local Testing

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your bot token:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_token_here"
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

### Railway.app Deployment

1. Connect your GitHub repository to Railway.app
2. Add environment variable: `TELEGRAM_BOT_TOKEN`
3. Deploy automatically from main branch

## Environment Variables

- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token from @BotFather

## Tech Stack

- Python 3.11
- python-telegram-bot library (v21.0.1)
- Railway.app for hosting

## About Uzorak Lab

Based in Zagreb, Croatia, Uzorak Lab provides professional peptide testing using LC-MS technology with detailed impurity analysis and Certificate of Analysis (COA) reports.
