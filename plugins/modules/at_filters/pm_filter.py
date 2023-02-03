import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import(
   del_all,
   find_filter,
   get_filters,
)


import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}
FILTER_MODE = {}

@Client.on_message(filters.group & filters.command('autofilter') | filters.private & filters.command('pm_autofilter'))
async def fil_mod(client, message):
      mode_on = ["yes", "on", "true"]
      mode_of = ["no", "off", "false"]

      try:
         args = message.text.split(None, 1)[1].lower()
      except:
         return await message.reply("Command is incomplete.")

      m = await message.reply("Processing...")

      if args in mode_on:
          FILTER_MODE[str(message.chat.id)] = "True"
          await m.edit("Auto filter enabled for this chat")

      elif args in mode_of:
          FILTER_MODE[str(message.chat.id)] = "False"
          await m.edit("Auto filter disabled for this chat")
      else:
          await m.edit("Use: `/autofilter on` or `/autofilter off`")

@Client.on_message(filters.private & filters.text & filters.incoming | filters.group & filters.text & filters.incoming)
async def give_filter(client,message):
    group_id = message.chat.id
    name = message.text

    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await message.reply_text(reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await message.reply_text(
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button)
                            )
                    elif btn == "[]":
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or ""
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button)
                        )
                except Exception as e:
                    print(e)
                break 

    else:
        if FILTER_MODE.get(str(message.chat.id)) is "False":
            return
        else:
            await auto_filter(client, message) 


@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(f"👋 Hello {query.from_user.first_name}\n\nThis Is Not For You 😔\n\n⚠️ Note : If You Want This You Can Request Your Own", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.",show_alert=True)
        return

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'files#{file.file_id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if 0 < offset <= 7:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 7
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"), InlineKeyboardButton(f"📃 Pages {round(int(offset)/7)+1} / {round(total/7)}", callback_data="pages")]
        )
    elif off_set is None:
        btn.append([InlineKeyboardButton("ɴᴇxᴛ ⌦", callback_data=f"next_{req}_{key}_{n_offset}"), InlineKeyboardButton(f"📘 {round(int(offset)/7)+1} / {round(total/7)}", callback_data="pages")])
    else:
        btn.append(
            [
                InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"📖 {round(int(offset)/7)+1} / {round(total/7)}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⌦", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    try:
        await query.edit_message_reply_markup( 
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()

@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("okDa", show_alert=True)
    if movie_  == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.message_id)
    if not movies:
        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Checking for Movie in database...')
    k = await manual_filters(bot, query.message, text=movie)
    if k==False:
        files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
        if files:
            k = (movie, files, offset, total_results)
            await auto_filter(bot, query, k)
        else:
            k = await query.message.edit('ᴛʜɪs ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ')
            await asyncio.sleep(10)
            await k.delete()

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!",show_alert=True)

    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Thats not for you!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        
        act = query.data.split(":")[2]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title

        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return

    elif "disconnect" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
        return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
        return
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)

    if query.data.startswith("file"):
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
            f_caption=f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"
            
        try:
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer(url=f"https://t.me/Htgtoolv4bot?start={file_id}")
                return
            elif P_TTI_SHOW_OFF:
                await query.answer(url=f"https://t.me/Htgtoolv4bot?start={file_id}")
                return
            else:
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(
           [[
           InlineKeyboardButton("⭐ ᴄʜᴀɴɴᴇʟ ⭐", url="https://t.me/tg_galaxy")
           ]]
        )
                    )
                await query.answer('Check PM, I have sent files in pm',show_alert = True)
        except UserIsBlocked:
            await query.answer('Unblock the bot mahn !',show_alert = True)
        except PeerIdInvalid:
            await query.answer(url=f"https://t.me/Htgtoolv4bot?start={file_id}")
        except Exception as e:
            await query.answer(url=f"https://t.me/Htgtoolv4bot?start={file_id}")

    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{title}"
        await query.answer()
        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption,
            reply_markup=InlineKeyboardMarkup(
           [[
           InlineKeyboardButton("⭐ ᴄʜᴀɴɴᴇʟ ⭐", url="https://t.me/tg_galaxy")
           ]]
        )
            )

    elif query.data == "pages":
        await query.answer()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton("✨ ᴀʙᴏᴜᴛ", callback_data="about")
            ],[
            InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀᴛ!", url="http://t.me/HTGToolV2Bot?startgroup=botstart"),
            InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", url="https://t.me/songdownload_group")
            ],[
            InlineKeyboardButton("⚙️ sᴇᴛᴛɪɴɢs", callback_data="mohelp"),
            InlineKeyboardButton("🤖 ᴍʏ ʙᴏᴛ's", callback_data="mybots")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    
    elif query.data == "mohelp":

        reply1 = await query.message.reply_text("Loading.\n▰▱▱▱")
        await asyncio.sleep(0.1)

        reply2 = await reply1.edit("Loading..\n▰▰▱▱")
        await asyncio.sleep(0.1)

        reply3 = await reply2.edit("Loading...\n▰▰▰▱")
        await asyncio.sleep(0.1)

        reply4 = await reply3.edit("Loading....\n▰▰▰▰")
        await asyncio.sleep(0.1)
     
        await reply4.delete()

        buttons = [[
            InlineKeyboardButton('Extra Commands', callback_data='exmd'),
            InlineKeyboardButton('Autofilter Commands', callback_data='atfs')
            ],[
            InlineKeyboardButton('player Commands', callback_data='player')
            ],[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MODULS_SET,
            reply_markup=reply_markup
        )

    elif query.data == "exmd":
        buttons = [[
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀ-ɪᴅ", callback_data="stck"),
            InlineKeyboardButton("ᴄʟᴇᴀɴ-sᴍ", callback_data="clsm"),
            InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴘʜ-ᴜᴘ", callback_data="tgph")
            ],[
            InlineKeyboardButton("sᴇᴀʀᴄʜ-ʏᴛ", callback_data="srch"),
            InlineKeyboardButton("ᴊsᴏɴ", callback_data="jsn"),
            InlineKeyboardButton("ᴍᴘ𝟺_2ᴍᴘ𝟹", callback_data="conv")
            ],[
            InlineKeyboardButton("ʟʏʀɪᴄs-ᴅʟ", callback_data="lyrc"),
            InlineKeyboardButton("sᴏɴɢ-ᴅʟ", callback_data="sdl"),
            InlineKeyboardButton("ᴊɪᴏ-sᴀᴀᴠɴ", callback_data="saavndl"),
            InlineKeyboardButton("ᴠɪᴅᴇᴏ-ᴅʟ", callback_data="vdl")
            ],[
            InlineKeyboardButton("ɢᴛʀᴀɴsʟᴀᴛᴏʀ", callback_data="gtra"),
            InlineKeyboardButton("ғᴜɴ", callback_data="Fns"),
            InlineKeyboardButton("ɪᴅ-ɪɴғᴏ", callback_data="inid"),
            InlineKeyboardButton("ᴊᴏᴋᴇ", callback_data="jkor")
            ],[
            InlineKeyboardButton("ʏᴛ-ᴛʜᴜᴍʙ", callback_data="ytthumb"),
            InlineKeyboardButton("ᴘᴀsᴛᴇ", callback_data="past"),
            InlineKeyboardButton("ᴛᴛs", callback_data="tts"),
            InlineKeyboardButton("ɪɴsᴘɪʀᴇ", callback_data="inspar")
            ],[
            InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data="mohelp"),
            InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
            InlineKeyboardButton("ɴᴇxᴛ ⌦", callback_data="xmd2")
            ],[
            InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTAMODS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "xmd2":
        buttons = [[
            InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="gith"),
            InlineKeyboardButton("ᴄᴏᴠɪᴅ", callback_data="covi"),
            InlineKeyboardButton("ғᴏʀᴡᴀʀᴅɪɴɢ", callback_data="forw"),
            InlineKeyboardButton("ᴘᴜʀɢᴇ", callback_data="prgs")
            ],[
            InlineKeyboardButton("ᴀɴɪᴍᴇ", callback_data="plat"),
            InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", callback_data="repo"),
            InlineKeyboardButton("ɢᴏ-ғɪʟᴇ", callback_data="gofl"),
            InlineKeyboardButton("ᴍᴇᴍᴇs", callback_data="mems")
            ],[
            InlineKeyboardButton("ᴀɴɪᴍᴇ-sғᴡ", callback_data="must"),
            InlineKeyboardButton("sʜᴀᴢᴀᴍ", callback_data="shaz"),
            InlineKeyboardButton("ᴀɴᴏɴғɪʟᴇs", callback_data="anfl"),
            InlineKeyboardButton("ᴡɪᴋɪ", callback_data="wikis")
            ],[
            InlineKeyboardButton("ʏᴛ-ᴛᴀɢ", callback_data="yttf"),
            InlineKeyboardButton("ғɪʟᴇ𝟸-ᴠɪᴅᴇᴏ", callback_data="fltv"),
            InlineKeyboardButton("ᴠɪᴅᴇᴏ𝟸-ғɪʟᴇ", callback_data="cv2f"),
            InlineKeyboardButton("ᴛɪᴍᴇ", callback_data="timz")
            ],[
            InlineKeyboardButton("ᴘɪɴɢ", callback_data="pinj"),
            InlineKeyboardButton("ᴘᴀss ɢᴇɴᴇʀᴀᴛ", callback_data="pasg"),
            InlineKeyboardButton("ɪᴍᴅʙ", callback_data="imbd"),
            InlineKeyboardButton("ʙᴀʏ-ғɪʟᴇ", callback_data="bayfa")
            ],[
            InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data="exmd"),
            InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
            InlineKeyboardButton("ɴᴇxᴛ ⌦", callback_data="xmd3")
            ],[
            InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTAMODS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "xmd3":
        buttons = [[
            InlineKeyboardButton("sᴛʏʟɪsʜ-ᴛxᴛ", callback_data="styl"),
            InlineKeyboardButton("ʜᴀɴᴅᴡʀɪᴛ", callback_data="handwr"),
            InlineKeyboardButton("ᴀʟɪᴠᴇ", callback_data="aliv"),
            InlineKeyboardButton("ɪᴍɢ-𝟸ᴘᴅғ", callback_data="imtp")
            ],[
            InlineKeyboardButton("ᴘᴅғ-2ᴛᴇxᴛ", callback_data="pdft"),
            InlineKeyboardButton("ᴀᴜᴅɪᴏʙᴏᴏᴋ", callback_data="audi"),
            InlineKeyboardButton("ᴄᴀʀʙᴏɴ", callback_data="crbn"),
            InlineKeyboardButton("ᴀᴛᴛᴀᴄʜ-ʟɪɴᴋ", callback_data="attal")
            ],[
            InlineKeyboardButton("ᴛʀɪᴍ", callback_data="timu"),
            InlineKeyboardButton("ɴᴏ-ʟɪɴᴋ", callback_data="nlng"),
            InlineKeyboardButton("sᴛɪᴋʀ-2ɪᴍɢ", callback_data="stki"),
            InlineKeyboardButton("ᴀɴɪᴍᴇ-ɪɴғᴏ", callback_data="aninfg")
            ],[
            InlineKeyboardButton("ᴡᴀ-sʜᴀʀᴇ", callback_data="washar"),
            InlineKeyboardButton("ᴛɢ-sʜᴀʀᴇ", callback_data="shar"),
            InlineKeyboardButton("ᴜʀʟ-sʜᴏʀᴛ", callback_data="urls"),
            InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ", callback_data="taga")
            ],[
            InlineKeyboardButton("s-sʜᴏᴛ", callback_data="sshot"),
            InlineKeyboardButton("ᴜɴᴢɪᴘᴇʀ", callback_data="unzp"),
            InlineKeyboardButton("ʀᴇɴᴀᴍᴇʀ", callback_data="rnmr"),
            InlineKeyboardButton("ǫᴜᴏᴛᴇs", callback_data="quot")
            ],[
            InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data="xmd2"),
            InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
            InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTAMODS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "bayfa":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BEYFILS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "inspar":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.INSPIRE_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "jkor":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.JOKES_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "imtp":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.IMG2PDF_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "attal":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ATTACHLINK_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "quot":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.QUOTES_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "aninfg":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ANIIN_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "stck":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.STICKER_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "clsm":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CLEANSERV_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "timz":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TIMZO_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "wikis":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.WIKIPDS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "mems":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MEMESS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "tgph":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TELEGRAPH_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "srch":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.YTSEARCH_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "jsn":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.JASON_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "prgs":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PURGS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "washar":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.WHATSAPPS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "conv":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONVERT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "mybots":
        buttons = [[
            InlineKeyboardButton("𝟙. Stylish Text bot", url="https://t.me/StylishText_X_Bot")
            ],[
            InlineKeyboardButton("𝟚. Youtube Dl bot", url="https://t.me/YouTubeDownloader7Bot")
            ],[
            InlineKeyboardButton("𝟛. Mention All bot", url="https://t.me/Mentionalltgtbot")
            ],[
            InlineKeyboardButton("𝟜. URL Uploader bot", url="https://t.me/UrlUploader_Xrobot")
            ],[
            InlineKeyboardButton("𝟝. Music Dl bot", url="https://t.me/Musicx_dlbot")
            ],[
            InlineKeyboardButton("𝟞. Google Translator bot", url="https://t.me/GTranslatorRobBot")
            ],[
            InlineKeyboardButton("𝟟. AntiChannel Ban", url="https://t.me/AntiChannelBan_xbot")
            ],[
            InlineKeyboardButton("𝟠. YouTube-playlist-dl-bot", url="https://t.me/YoutubePlaylistdowntgbot")
            ],[
            InlineKeyboardButton("𝟡. Spotify Dl bot", url="https://t.me/spotifysavetgbot")
            ],[
            InlineKeyboardButton("𝟙𝟘. All-in-one-MusicDl-bot", url="https://t.me/All_in_one_songdownloaderbot")
            ],[
            InlineKeyboardButton("𝟙𝟙. Shazam bot", url="https://t.me/ShazamX_robot")
            ],[
            InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data="start"),
            InlineKeyboardButton("✗ ᴇxɪᴛ ✗", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MYBOTS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "lyrc":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.LYRICS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "saavndl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SAAVNDL_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "sdl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SONGDLR_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "vdl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDEODLR_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "gtra":
        buttons = [[
            InlineKeyboardButton("ʟɪsᴛ ᴏғ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs", url="https://cloud.google.com/translate/docs/languages"),
            ],[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GTRANCE_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "Fns":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FUNNY_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "inid":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.INFORMATION_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "ytthumb":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.YTTHUMB_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "past":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PASTER_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "tts":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='exmd')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TTS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "gith":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GITHUB_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "covi":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.COVID_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "forw":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FORWERD_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "plat":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PLAYST_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "repo":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.REPORTS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "gofl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GOFILES_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "must":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2'),
            InlineKeyboardButton('ᴍᴏʀᴇ ⎆', callback_data='jiff')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MUSICTAG_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "jiff":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='must')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.JIFFUN_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "shaz":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SHAZAM_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "anfl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ANONFILS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "yttf":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.YTTAGFY_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "fltv":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FILTOVID_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "cv2f":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDTOFIL_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "pinj":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PINGS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "pasg":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PASSWED_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "imbd":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.IMDBS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "styl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.STYLISHT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "styl":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.STYLISHT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "handwr":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HANDWRIT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "aliv":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ALIVED_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "pdft":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PDFTOTXT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "audi":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUDIOBOOK_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "crbn":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CARBON_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "nlng":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.NOLINKS_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "stki":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.STIKERPH_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "shar":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SHARET_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "urls":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.URLSHORT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "taga":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TAGALL_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "unzp":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.UNZIPER_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "rnmr":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.RENAMEER_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "sshot":
        buttons = [[
            InlineKeyboardButton('« ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SCRESHOT_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "timu":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='xmd3')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TRIMER_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "player":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='mohelp')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PLAYRER_TXT,
            reply_markup=reply_markup
        )

    elif query.data == "atfs":
        buttons = [[
            InlineKeyboardButton('ᴍᴀɴᴜᴀʟ ꜰɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ', callback_data='autofilter')
            ],[
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct'),
            InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin')
            ],[
            InlineKeyboardButton('ꜰɪʟᴇ sᴛᴏʀᴇ', callback_data='fstore'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats')
            ],[
            InlineKeyboardButton("⌫ ʙᴀᴄᴋ", callback_data="mohelp"),
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
#================================
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('✗ ᴇxɪᴛ ✗', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup
        )
    elif query.data == "soue":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs'),
            InlineKeyboardButton('∆ Buttons', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='manuelfilter')
        ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('« ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('👮‍♂️ ᴀᴅᴍɪɴ', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "infohelp":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.INFO_TXT,
            reply_markup=reply_markup
        )
    elif query.data == "fstore":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FSTORE_TXT,
            reply_markup=reply_markup
        )

    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs'),
            InlineKeyboardButton('ʀᴇꜰʀᴇsʜ 🔄', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "rfrsh":
        await query.answer("Fetching MongoDb DataBase")
        buttons = [[
            InlineKeyboardButton('⌫ ʙᴀᴄᴋ', callback_data='atfs'),
            InlineKeyboardButton('ʀᴇꜰʀᴇsʜ 🔄', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
      )
    

async def auto_filter(client, msg, spoll=False):
    if not spoll:
        message = msg
        if message.text.startswith("/"): return # ignore commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if 2 < len(message.text) < 100:
            search = message.text
            files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
            if not files:
                if SPELL_CHECK_REPLY:
                    return await advantage_spell_chok(msg)
                else:
                    return
        else:
            return
    else:
        message = msg.message.reply_to_message # msg will be callback query
        search, files, offset, total_results = spoll
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'files#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [InlineKeyboardButton(text=f"📘 1/{round(int(total_results)/7)}",callback_data="pages"), InlineKeyboardButton(text="ɴᴇxᴛ ⌦",callback_data=f"next_{req}_{key}_{offset}")]
        )
    else:
        btn.append(
            [InlineKeyboardButton(text="📘 1/1",callback_data="pages")]
        )
    imdb = await get_poster(search, file=(files[0]).file_name) if IMDB else None
    if imdb:
        cap = IMDB_TEMPLATE.format(
            query = search,
            request = message.from_user.mention if message.from_user else 0,
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url'],
            **locals()
        )
    else:
        cap = f"Here is what i found for your query {search}"
    if imdb and imdb.get('poster'):
        try:
            await message.reply_photo(photo=imdb.get('poster'), caption=cap, reply_markup=InlineKeyboardMarkup(btn))
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=poster, caption=cap, reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            logger.exception(e)
            await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    if spoll:
        await msg.message.delete()
        

async def advantage_spell_chok(msg):
    query = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)", "", msg.text, flags=re.IGNORECASE) # plis contribute some common words 
    query = query.strip() + " movie"
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        k = await msg.reply("I couldn't find any movie in that name.")
        await asyncio.sleep(8)
        await k.delete()
        return
    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE) # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)', '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*", re.IGNORECASE) # match something like Watch Niram | Amazon Prime 
        for mv in g_s:
            match  = reg.match(mv)
            if match:
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed)) # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True) # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist)) # removing duplicates
    if not movielist:
        k = await msg.reply("I couldn't find anything related to that. Check your spelling")
        await asyncio.sleep(8)
        await k.delete()
        return
    SPELL_CHECK[msg.message_id] = movielist
    btn = [[
                InlineKeyboardButton(
                    text=movie.strip(),
                    callback_data=f"spolling#{user}#{k}",
                )
            ] for k, movie in enumerate(movielist)]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spolling#{user}#close_spellcheck')])
    await msg.reply("I couldn't find anything related to that\nDid you mean any one of these?", reply_markup=InlineKeyboardMarkup(btn))
    

async def manual_filters(client, message, text=False):
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await client.send_message(group_id, reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await client.send_message(
                                group_id, 
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id = reply_id
                            )
                    elif btn == "[]":
                        await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id = reply_id
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id = reply_id
                        )
                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False
