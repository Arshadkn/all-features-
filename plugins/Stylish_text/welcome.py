from pyrogram import filters, Client
from pyrogram.types import Message


WEL_GIF = "https://telegra.ph/file/b616d3a126715d9b1aa46.mp4"

@Client.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
        await m.reply_animation(WEL_GIF,caption="hello! dear **{}**, and welcome to **{}** group!".format(m.from_user.first_name,m.chat.title))
        
@Client.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
        await m.reply("oof! dear {}\nlefted the chat".format(m.from_user.first_name))
