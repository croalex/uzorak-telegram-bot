import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WELCOME_MESSAGE = """🚀 We just launched our Advanced Peptide Testing Service.


**99% Purity = Dangerous Lie.**


✴️ Don't believe? Check with ChatGPT ⬇️

✅ Follow @Uzorak channel for % and COA's ⬇️

✅ Check our sample Reta report below ⬇️

❇️ or Order your Test Analysis at uzorak.com ⬇️"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with inline keyboard when /start is issued."""
    # Send video demo first
    with open('uzorak_demo.mp4', 'rb') as video_file:
        await update.message.reply_video(
            video=video_file,
            caption="Don't trust your peptides. Verify."
        )

    # Send welcome message with buttons
    keyboard = [
        [InlineKeyboardButton("ChatGPT on 99%", url="https://chatgpt.com/share/679690bb-4c28-8012-b662-a293b83e1fcb")],
        [InlineKeyboardButton("📢 Uzorak Channel", url="https://t.me/uzorak")],
        [InlineKeyboardButton("📄 Sample COA Report", url="https://uzorak.com/#/verify/GYHLVP")],
        [InlineKeyboardButton("🌐 Uzorak.com", url="https://uzorak.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)
    logger.info(f"User {update.effective_user.id} started the bot")


def main() -> None:
    """Start the bot."""
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("Bot started successfully")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
