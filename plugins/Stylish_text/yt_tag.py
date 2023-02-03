
import os
import pyrogram
from pyrogram import filters, Client
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags # https://pypi.org/project/youtubetags
from YoutubeTags import videotags

BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('↗️Share↗️', url='https://t.me/share/url?url=Hi%20Bro%20%F0%9F%91%8B%2C%0AToday%20I%20found%20an%20AmaZing%20Multi-Purpose%20Bot%3A-%20%40Htgtoolv4bot%0A....%0AU%20also%20use%20this%20bot%20and%20enjoy'),
            InlineKeyboardButton('😉 Hello', url='https://telegram.me/Htgtoolv4bot')
        ]
    ]
)

@Client.on_message(filters.command("yttags"))
async def yttags(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("**Reply to some Youtube link...**")
    if not message.reply_to_message.text:
        return await message.reply_text("**Reply to some Youtube link...**")
    link = message.reply_to_message.text
    tags = videotags(link)
    if tags=="":
         await message.reply_text("No Tags Found")
    else:
         await message.reply_text(text=f"**These are the Tags that I Found** \n\n ` {tags} ` \n\n\n**Powered by: @Htgtoolv4bot**",reply_markup=BTNS)
  
