import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def share_link(text: str) -> str:
    return "**Successfully Generated Your Sharing Text✈️**\n\nhttps://t.me/share/url?url=" + quote(text)

@Client.on_message(filters.private & filters.command(["share"]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Join My group**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "My Group", url="https://t.me/songdownload_group")
                    ]                
                ]
            ),
            reply_to_message_id=reply_id
        )
        return
    await message.reply_text(share_link(input_text), reply_to_message_id=reply_id)
        
