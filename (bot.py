import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import subprocess

TOKEN = os.getenv("BOT_TOKEN")

async def convert_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.video.get_file()
    input_path = "input.mp4"
    output_path = "output.mp4"

    await file.download_to_drive(input_path)

    subprocess.run([
        "ffmpeg",
        "-i", input_path,
        "-vf", "crop='min(iw,ih)':'min(iw,ih)',scale=512:512",
        "-t", "60",
        output_path
    ])

    await update.message.reply_video_note(video_note=open(output_path, "rb"))

    os.remove(input_path)
    os.remove(output_path)

app = ApplicationBuilder().token(TOKEN).build()
app.add
