import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WELCOME_MESSAGE = """🧪 Welcome to Uzorak Lab!

Professional peptide testing with LC-MS technology.

✓ Detailed impurity analysis
✓ Certificate of Analysis (COA)
✓ Beyond standard UV-HPLC results

📍 Based in Zagreb, Croatia

Choose an option below:"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with inline keyboard when /start is issued."""
    # Send GIF animation first
    with open('uzorak_demo.gif', 'rb') as gif_file:
        await update.message.reply_animation(
            animation=gif_file,
            caption="📊 Sample COA Report Preview (GIF)"
        )

    # Send MP4 video second
    with open('uzorak_demo.mp4', 'rb') as video_file:
        await update.message.reply_video(
            video=video_file,
            caption="📊 Sample COA Report Preview (Video)"
        )

    # Send welcome message with buttons
    keyboard = [
        [InlineKeyboardButton("📢 Uzorak Channel", url="https://t.me/uzorak")],
        [InlineKeyboardButton("🌐 Uzorak.com", url="https://uzorak.com")],
        [InlineKeyboardButton("📄 Sample COA Report", url="https://uzorak.com/#/verify/GYHLVP")]
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
