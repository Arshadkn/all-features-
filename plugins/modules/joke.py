
import os
import requests
import json
from info import LOG_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('😉 Hello 😊', url='https://t.me/Htgtoolv4bot')]])
A = """Hi, {} with user id:- {} used /joke command."""


@Client.on_message(filters.command("jokes"))
async def jokeapibot(bot, update):
    await update.reply_chat_action("typing")
    koshik = await update.reply_text("**Processing...⏳**", quote=True)
    px = "https://v2.jokeapi.dev/joke/Any?type=single"
    request = requests.get(px)
    result = request.json()
    joke = result['joke']
    gett_joke = f"""
🤣Here is Your Joke :\n\n **{joke}**
\n**Powered by:** @Htgtoolv4bot"""
    await bot.send_message(LOG_CHANNEL, A.format(update.from_user.mention, update.from_user.id))
    await koshik.edit_text(
        text=gett_joke,
        reply_markup=BUTTONS,
        disable_web_page_preview=True)
