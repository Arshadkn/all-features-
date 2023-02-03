from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from database.decorators import humanbytes


ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}


@Client.on_message(filters.private & filters.command(["song", "mp3"]))
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("`[▰▱▱▱▱▱]10%`\n\n🔎 ғɪɴᴅɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ...")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        duration = results[0]["duration"]
        channel = results[0]["channel"]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit(f"📜 __ʜᴇʏ {message.from_user.first_name} ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴄᴏᴍᴍᴀɴᴅ ᴀʀɢᴜᴍᴇɴᴛs, sᴏᴍᴇ ᴇxᴀᴍᴘʟᴇs ᴅᴏᴡɴ ʙᴇʟᴏᴡ__👇🏼\n__ᴘ𝗅𝖾𝖺𝗌𝖾 ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ sᴏɴɢ ɴᴀᴍᴇ ᴏ𝗋 s𝖾𝖺𝗋𝖼𝗁 𝖺𝗍 Google.com ғ𝗈𝗋 ᴄ𝗈𝗋𝗋𝖾𝖼𝗍 s𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗈𝖿 𝗍𝗁𝖾 sᴏɴɢ.__\n\n**ᴇxᴀᴍᴘʟᴇ:**\n- `/song Believer`\n- `/s Believer`")
        print(str(e))
        return
    m.edit("`[▰▰▰▱▱▱]50%`\n\n📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ғɪʟᴇ...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🔍**Song Downloaded**\n\n✒️ **Tɪᴛʟᴇ:** {title[:35]}\n⌚ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🎥 **ᴄʜᴀɴɴᴇʟ:** {channel}\n\n**📤 Uᴘʟᴏᴀᴅᴇᴅ ʙʏ: [Hydrix Tool Bot](https://t.me/Htgtoolv4bot)**\n❤️**My group:** [Music Galaxy](https://t.me/songdownload_group)"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("`[▰▰▰▰▰▱]95%`\n\n📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ...")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("#ERROR, ᴛʜᴇʀᴇ ɪs sᴏᴍᴇ ᴇʀʀᴏʀ. ᴘʟs ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ...")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(filters.private & filters.command(["video", "mp4"]))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **error:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **ᴜᴘʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)


