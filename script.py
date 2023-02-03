class script(object):
    START_TXT = """
ʜᴇʏ {} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ.
ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ʜᴇʟᴘғᴜʟʟ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴍʏ ᴘᴍ
ʜɪᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛᴏ ᴍʏ ғᴜʟʟ ᴍᴏᴅᴜʟᴇs.
ᴀɴᴅ ɪ ᴘʀᴏᴠɪᴅᴇ sɪᴍᴘʟᴇ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ + ᴍᴀɴᴜᴀʟ ꜰɪʟᴛᴇʀ + ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
"""
    HELP_TXT = """🔰 ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs. ʜᴇʀᴇ ɪs ᴍʏ ᴀʟʟ ᴍᴏᴅᴜʟᴇs"""

    ABOUT_TXT = """
╭───•[ᴀʙᴏᴜᴛ]────⍟
│➪ **ʙᴏᴛ ɴᴀᴍᴇ** : [ʜʏᴅʀɪx ᴛᴏᴏʟ ʙᴏᴛ](t.me/Htgtoolv4bot)
│➪ **ᴅᴇᴠ ʙʏ** : [ʜʏᴅʀɪx](t.me/HydraLivegrambot)
│➪ **ɢʀᴏᴜᴘ** : [ᴍɢ](https://t.me/songdownload_group)
│➪ **ᴄʜᴀɴɴᴇʟ** : [ᴛɢɢ](https://t.me/Tg_galaxy)
│➪ **ʟᴀɴɢᴜᴀɢᴇ** : [ᴘʏᴛʜᴏɴ 3](https://www.python.org)
│➪ **ꜰʀᴀᴍᴇᴡᴏʀᴋ** : [ᴘʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
│➪ **ʜᴏsᴛᴇᴅ ᴏɴ** : [ʜᴇʀᴏᴋᴜ](heroku.com)
│➪ **ʙᴜɪʟᴅ sᴛᴀᴛᴜs** : v4.0.2 [ʙᴇᴛᴀ]
├──────────•
│➪ **ᴀᴜᴛᴏғɪʟᴛᴇʀ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:**am
├• [ᴇᴠᴀ ᴍᴇʀɪᴀ](https://github.com/EvamariaTG/EvaMaria)
├───────────•
│➪ **ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:**
├• [ʏᴜᴋᴋɪ ᴍᴜsɪᴄ](https://github.com/TeamYukki/YukkiMusicBot)
╰─────────────⍟
"""

    MANUELFILTER_TXT = """📚 <b>ғɪʟᴛᴇʀs</b>
➪ Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Hʏᴅʀɪx Tᴏᴏʟ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ.

<b>NOTE:</b>
𝟷. Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇs ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʀᴇᴘʟʏ ғɪʟᴛᴇʀs ɪɴ ᴄʜᴀᴛ.
𝟸. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
𝟹. Aʟᴇʀᴛ ʙᴏᴛᴛᴏɴ ᴀʀᴇ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡɪᴛʜ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀ.
4. Fɪʟᴛᴇʀs ᴅᴏᴇs sᴜᴘᴘᴏʀᴛ ᴀʟʟ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴀʀᴋᴅᴏᴡɴ, ᴍᴇᴅɪᴀ ᴀɴᴅ Bᴏᴛᴛᴏɴs.

<b>COMMANDS AND USAGE:</b>
• <code>/add</code> - ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ.
• <code>/viewfilters</code> - ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ.
• <code>/del</code> - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ.
• <code>/delall</code> - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)."""

    BUTTON_TXT = """📚 <b>ʙᴜᴛᴛᴏɴs</b>

➪ ʜʏᴅʀɪx sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>ɴᴏᴛᴇ:</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ʜʏᴅʀɪx sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:https://t.me/htgtoolv4bot)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """📚 <b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b>
    
➪ ᴛᴏ ᴜsᴇ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴍᴏᴅᴜʟᴇ sɪᴍᴘʟʏ ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ ᴛʜᴀᴛs ɪᴛ

<b>ɢʀᴏᴜᴘ ᴀᴜᴛᴏғɪʟᴛᴇʀ</b>
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs <code>/autofilter</code> ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴏғғ/ᴏɴ ᴅɪsᴀʙʟᴇ/ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏ ғɪʟᴛᴇʀɪɴɢ sʏsᴛᴇᴍ ɪɴ ɢʀᴏᴜᴘ's.
ᴜsᴇ <code>/autofilter off</code> To ᴅɪsᴀʙʟᴇ
ᴜsᴇ <code>/autofilter on</code> To ᴇɴᴀʙʟᴇ

<b>ᴘᴍ ᴀᴜᴛᴏғɪʟᴛᴇʀ</b>
ᴜsᴇ ᴛʜɪs <code>/pm_autofilter</code> ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴏғғ/ᴏɴ ᴅɪsᴀʙʟᴇ/ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏ ғɪʟᴛᴇʀɪɴɢ sʏsᴛᴇᴍ ɪɴ ᴍʏ ᴘᴍ
ᴊᴜsᴛ ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴏᴠᴇ/sᴇᴀʀɪᴇs ɴᴀᴍᴇ ʜᴇʀᴇ
ᴜsᴇ <code>/pm_autofilter off</code> To ᴅɪsᴀʙʟᴇ
ᴜsᴇ <code>/pm_autofilter on</code> To ᴇɴᴀʙʟᴇ

<b>ɴᴏᴛᴇ:</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""

    CONNECTION_TXT = """📚 <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

➪ ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. sᴇɴᴅ <code>/connect</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• <code>/connect</code>  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
• <code>/disconnect</code> - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀt
• <code>/connections</code> - ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs"""


    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of hydrix tools

<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """📚 <b>ᴀᴅᴍɪɴ ᴍᴏᴅs</b>

<b>ɴᴏᴛᴇ:</b>
➪ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs
<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
- <code>setskip</code> - skip corrent file to next
- <code>/logs</code> - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs
- <code>/stats`</code> - ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.
- <code>/delete</code> - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.
- <code>/users</code> - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.
- <code>/chats</code> - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs
- <code>/leave</code>  - ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
- <code>/disable</code>  - ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.
- <code>/ban</code>  - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.
- <code>/unban</code>  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.
- <code>/channel</code> - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs
- <code>/broadcast</code> - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs
- <code>/group_broadcast</code> - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs
- <code>/set_chat_title</code> - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.
- <code>/set_chat_photo</code> - ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.
- <code>/set_user_title</code> - ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ᴛɪᴛʟᴇ ᴏғ ᴀɴ ᴀᴅᴍɪɴ.

》 <b>Bot Status (Heroku)</b>

ɢᴇᴛ ᴛʜɪs ʙᴏᴛ's ʜᴇʀᴏᴋᴜ ᴅʏɴᴏ sᴛᴀᴛᴜs ᴀɴᴅ ɪᴛ's ᴜᴘᴛɪᴍᴇ.
- <code>/botstatus</code> - Just send here
"""

    STATUS_TXT = """
╭─────────────⎆
├⎆<b>ᴛᴏᴛᴀʟ ғɪʟᴇs :</b> <code>{}</code>
├─⍟
├⎆<b>ᴛᴏᴛᴀʟ ᴜsᴇʀs :</b> <code>{}</code>
├──⍟
├⎆<b>ᴛᴏᴛᴀʟ ᴄʜᴀᴛs :</b> <code>{}</code>
├───⍟
├⎆<b>ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ :</b> <code>{}</code>
├────⍟
├⎆<b>ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ :</b> <code>{}</code>
╰─────────────⎆
"""
    LOG_TEXT_G = """#NewGroup
╭──────────────⍟
├•👥 Group = {}(<code>{}</code>)
│
├•🎭 Total Members = <code>{}</code>
│
├•👮 Added BY - {}
│ @Htgtoolv4bot
╰──────────────⍟
"""
    LOG_TEXT_P = """#NewUser
╭──────────⍟
├•🆔 ID - <code>{}</code>
│
├•👤 Name - {}
│ @Htgtoolv4bot
╰──────────⍟
"""
    TIMZO_TXT = """
📚 **ᴛɪᴍᴇ ᴢᴏɴᴇ**

➪ I can find your time & date from here,
 just type `/time` this command.

**Exᴀᴍᴘʟᴇ:**
- /time
"""
    INFO_TXT = """**👤 User Information**

__A Module To Fetch Telegram User Info__

**📚 Avaible Commands**:

- /info :- __To Get User Information__

- /id :- __To Get Telegram User ID__

**⚠️ Note :** __This Commands Be Used In PM's And Groups__
"""

    FSTORE_TXT = """📚 **ғɪʟᴇ sᴛᴏʀᴇ**
➪ Wɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ I ᴄᴀɴ Sᴛᴏʀᴇ ғɪʟᴇ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴡɪᴛʜ ᴛʜɪs ʟɪɴᴋ I ᴄᴀɴ sʜᴀʀᴇ ᴛʜᴇɪʀ ғɪʟᴇ ʏᴏᴜ ɢɪᴠᴇ ᴍᴇ ғʀᴏᴍ ᴀɴʏ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴅɪɴɢ ᴍᴇ.

**Cᴏᴍᴍᴀɴᴅ Usᴀɢᴇ**
- <code>/link</code> - Rᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʟɪɴᴋ
- <code>/batch</code> - Usᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ʟɪɴᴋ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

**Exᴀᴍᴘʟᴇ:**
- <code>/link</code> :- __ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ__
- <code>/batch https://t.me/teamEvaMaria/2 https://t.me/teamEvaMaria/9</code>
"""

    MODULS_SET = """
ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""

    EXTAMODS_TXT = """
🔰 ɪ ᴄᴀɴ ɢᴜɪᴅᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ʜʏᴅʀɪx ᴛᴏᴏʟs ʙᴏᴛ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴘʀᴏᴘᴇʀʟʏ ᴜsᴇ ᴛʜᴇᴍ. ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɴᴀᴠɪɢᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀʟʟ ᴏғ ᴛʜᴇ ᴍᴏᴅᴜʟᴇs.
"""

    STICKER_TXT = """
**📚 sᴛɪᴄᴋᴇʀ ɪᴅ ᴄᴏᴍᴍᴀɴᴅs**

➪ __ʜᴇʀ ɪs sɪᴍᴘʟᴇ **sᴛɪᴄᴋᴇʀ ɪᴅ** ᴍᴏᴅᴜʟᴇ ғᴏʀ ʏᴏᴜ, ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ ғʀᴏᴍ ʜᴇʀᴇ,__
ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ **sᴛɪᴄᴋᴇʀ** , ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴅᴏᴡɴ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/stickerid` : ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
"""
    CLEANSERV_TXT = """
**📚 ᴄʟᴇᴀɴ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ**

➪ __ᴅᴇʟᴇᴛᴇ ᴀʟʟ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇs. ᴛʜᴏsᴇ ᴀʀᴇ ᴛʜᴇ ᴀɴɴᴏʏɪɴɢ 'x ᴊᴏɪɴᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ' ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs ʏᴏᴜ sᴇᴇ ᴡʜᴇɴ ᴘᴇᴏᴘʟᴇ ᴊᴏɪɴ.__
__ɪ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ᴀ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ʟɪᴋᴇ ᴊᴏɪɴ ʟᴇғᴛ ᴀɴᴅ ᴍᴏʀᴇ,
ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ɪᴛ.
"""

    TELEGRAPH_TXT = """
**📚 ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅᴇʀ ᴄᴏᴍᴍᴀɴᴅ**

➪ __ᴛʜɪs ɪs ᴀ **ᴛᴇʟᴇɢʀᴀᴘʜ** ᴜᴘʟᴏᴀᴅᴇʀ ᴍᴏᴅᴜʟᴇ, sᴇɴᴅ ᴍᴇ ᴜɴᴅᴇʀ 𝟻ᴍʙ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ, ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ I'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ɪɴᴛᴏ__ telegra.ph
ᴠɪᴅᴇᴏ ᴜᴘʟᴏᴀᴅᴇ ɴᴏᴛ sᴏᴘᴘᴏʀᴛ

**ᴇxᴀᴍᴘʟᴇ:**
- `/tgraph` : ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ ᴇᴛᴄ.
- `/telegraph` : ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ,ɢɪғ,ᴘɴɢ ᴇᴛᴄ.
"""

    YTSEARCH_TXT = """
**📚 ʏᴏᴜᴛᴜʙᴇ sᴇᴀʀᴄʜ ᴄᴏᴍᴍᴀɴᴅ**

➪ ᴛʜɪs ɪs ᴀ ʏᴏᴜᴛᴜʙᴇ sᴇᴀʀᴄʜ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴀɴ sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀʀɢᴜᴍᴇɴᴛs.

**ᴇxᴀᴍᴘʟᴇ:**
- `/ytsearch` ᴠɪᴅᴇᴏ ɴᴀᴍᴇ : sᴇᴀʀᴄʜ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏs
- `/ytsearch Alen Walker`
- `/search sorry justin bieber`
- `/search alone marshmallow`
"""

    ANIIN_TXT = """
📚 **ᴀɴɪᴍᴇ ɪɴғᴏ**

➪ This module for to get animes movies Informations.

- `/getvidinfo` - Reply to any video media file to get video information.
- `/search_anime` - To find anime 
**Example:** `/search_anime Attack on Titan`
- `/kitsu` - Reply to any anime message or any other things, this command also work in group.

"""
    JASON_TXT = """
**📚 ᴊsᴏɴ ᴄᴏᴍᴍᴀɴᴅ**

➪ __ɪ ᴄᴀɴ sʜᴏᴡ ʏᴏᴜ ᴊsᴏɴ ʀᴀᴡ ᴅᴀᴛᴀ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴀssᴀɢᴇ. ɪᴛ ᴄᴏᴜʟᴅ ʙᴇ ᴜsᴇғᴜʟ ᴀᴛ sᴏᴍᴇ ᴘᴏɪɴᴛs ᴀɴᴅ sʜᴏᴡs ᴛʜᴇ ᴊsᴏɴ ᴅᴀᴛᴀ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ.__

**ᴇxᴀᴍᴘʟᴇ:**
- `/json` : ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴊsᴏɴ.
"""

    CONVERT_TXT = """
**📚 ᴠɪᴅᴇᴏ ᴛᴏ ᴍᴘ𝟹ᴄᴏɴᴠᴇᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ**

➪ __ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ, ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ. ғɪʀsᴛ sᴇɴᴅ ᴀ ᴠɪᴅᴇᴏ ғᴏʀ ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ.__

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴠɪᴅᴇᴏ ғɪʟᴇ
- `/convertaudio` :  ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴛʜᴇɴ ɪᴍ ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴀᴜᴅɪᴏ.
"""

    MYBOTS_TXT = """
╭──•**Mʏ ʙᴏᴛs ʟɪsᴛ**
├•**Tʜᴇɪs ᴀʀᴇ ᴍʏ ᴏᴛʜᴇʀ ʙᴏᴛs**
│
├•𝟙. `Stylish Text bot`
├•𝟚. `Youtube Dl bot`
├•𝟛. `Mention All bot`
├•𝟜. `URL Uploader bot`
├•𝟝. `Music Dl bot`
├•𝟞. `GoogleTranslator-bot` **[offline]**
├•𝟟. `AntiChannel Ban bot`
├•𝟠. `YouTube-playlist-dl-bot`
├•𝟡. `Spotify dl bot`
├•𝟙𝟘. `All-in-one-Musicdlbot`
├•𝟙𝟙. `Shazam Bot`
╰───────────⍟   
"""

    LYRICS_TXT = """
**📚 ʟʏʀɪᴄ ᴅʟ ᴄᴏᴍᴍᴀɴᴅ**

➪ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ʟʏʀɪᴄs ᴅᴏᴡɴʟᴏᴀᴅ, ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ  ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ sᴏɴɢ ʟʏʀɪᴄs ғʀᴏᴍ ʜᴇʀᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/lyric` - [ᴍᴜsɪᴄ ɴᴀᴍᴇ] sᴇᴀʀᴄʜᴇs ʟʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴍᴜsɪᴄ ᴏɴ ᴡᴇʙ.
- `/lyric beggin`
- `/lyric faded Alen walker`
"""

    SAAVNDL_TXT = """
**Jio Saavn Dl**
Sᴀᴀᴠɴ ɪs ᴀɴ Iɴᴅɪᴀɴ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴀ ᴅɪɢɪᴛᴀʟ ᴅɪsᴛʀɪʙᴜᴛᴏʀ ᴏғ Bᴏʟʟʏᴡᴏᴏᴅ, Eɴɢʟɪsʜ ᴀɴᴅ ᴏᴛʜᴇʀ ʀᴇɢɪᴏɴᴀʟ Iɴᴅɪᴀɴ ᴍᴜsɪᴄ ᴀᴄʀᴏss ᴛʜᴇ ᴡᴏʀʟᴅ. 
Sɪɴᴄᴇ ɪᴛ ᴡᴀs ғᴏᴜɴᴅᴇᴅ ɪɴ 𝟸𝟶𝟶𝟽, ᴛʜᴇ ᴄᴏᴍᴘᴀɴʏ ʜᴀs ᴀᴄǫᴜɪʀᴇᴅ ʀɪɢʜᴛs ᴛᴏ ᴏᴠᴇʀ 𝟹𝟼…

Tʜɪs ɪs ᴀ Jɪᴏ-sᴀᴀᴠɴ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ. 
ɪᴛs ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs ғʀᴏᴍ ᴊɪᴏsᴀᴀᴠɴ.
<coode>/saavn</code> To Download Songs from Jiosaavn.🎶

**ᴇxᴀᴍᴘʟᴇ:**
<code>/saavn Verithanam</code>
<code>/saavn dilbar</code>
<code>/saavn de taali</code>
"""
    SONGDLR_TXT = """
**📚 sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴍᴀɴᴅ**

➪ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ, ᴜsᴇ /song sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴜsᴇ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ sᴏɴɢ's
`/song` (ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ ᴏʀ sᴏɴɢ ɴᴀᴍᴇ) - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ғᴀsᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/song love nwantiti`
- `/song beggin`
- `/s alone marshmallow`

ᴏʀ
`/song https://www.youtube.com/watch?v=HhjHYkPQ8F0`
`/s https://www.youtube.com/watch?v=HhjHYkPQ8F0`
"""

    PURGS_TXT = """
📚 **ᴘᴜʀɢᴇs**
➪ ɴᴇᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʟᴏᴛs ᴏғ ᴍᴇssᴀɢᴇs? Tʜᴀᴛ's ᴡʜᴀᴛ ᴘᴜʀɢᴇs ᴀʀᴇ ғᴏʀ!

- /purge : ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ.
- /purge : ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ X ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴜɴᴛɪʟ ɴᴏᴡ.
-> `/purge`

- ᴍᴀʀᴋ ᴛʜᴇ ғɪʀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘᴜʀɢᴇ ғʀᴏᴍ (ᴀs ᴀ ʀᴇᴘʟʏ).
"""
    VIDEODLR_TXT = """
**📚 ᴠᴇᴅɪᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴍᴀɴᴅ**

➪ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴠᴇᴅɪo ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
`/video` (ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ ᴏʀ sᴏɴɢ ɴᴀᴍᴇ) - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ғᴀsᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏs ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/video beggin`
- `/video love nwantiti`
- `/v alone marshmallow`

ᴏʀ
`/video https://www.youtube.com/watch?v=HhjHYkPQ8F0`
`/v https://www.youtube.com/watch?v=HhjHYkPQ8F0`
"""

    GTRANCE_TXT = """
**ɢᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ**

➪ ɢᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ ᴡʜɪᴄʜ ᴍᴇᴀɴs , ᴀ ʙᴏᴛ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ғᴇᴡ ʟᴀɴɢᴜᴀɢᴇs ғʀᴏᴍ ᴀɴʏ ᴏᴛʜᴇʀ ʟᴀɴɢᴜᴀɢᴇ ɪɴ ᴡᴏʀʟᴅ.
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɢᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ ɪɴ ʜɪs ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ & ɢʀᴏᴜᴘs.

**ᴇxᴀᴍᴘʟᴇ:**
/tr (ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs ᴏʀ ᴍʏ ᴘᴍ 
Cʟɪᴄᴋ ʟᴀɴɢ ʟɪsᴛ ʙᴏᴛᴛᴏɴ ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ.
"""

    FUNNY_TXT = """
📚 **ғᴜɴ ᴄᴏᴍᴍᴀɴᴅ**

➪ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ ғᴜɴ ᴍᴏᴅᴜʟᴇ

- `/roll` : ʀᴏʟʟ ᴀ ᴅɪᴄᴇ
- `/ball` : ᴘʟᴀʏ ᴛʜᴇ ʙᴀsᴋᴇᴛʙᴀʟʟ
- `/pog` : through the ball
- `/throw` : Bla
- `/goal` : play football
- `/luck` : you lucky
- `/slap` : sʟᴀᴘ ᴀ ᴜsᴇʀ, ᴏʀ ɢᴇᴛ sʟᴀᴘᴘᴇᴅ ɪғ ɴᴏᴛ ᴀ ʀᴇᴘʟʏ.
- `/shout` `<keyword>`: ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ʟᴏᴜᴅ sʜᴏᴜᴛ.
- `/bluetext` : ᴄʜᴇᴄᴋ ᴜʀsᴇʟғ :V
- `/react` : ʀᴀɴᴅᴏᴍ ʀᴇᴀᴄᴛɪᴏɴ.
- `/run` : ʀᴇᴘʟʏ ᴀ ʀᴀɴᴅᴏᴍ sᴛʀɪɴɢ ғʀᴏᴍ ᴀɴ ᴀʀʀᴀʏ ᴏғ ʀᴇᴘʟɪᴇ.
- `/runml` : ʀᴇᴘʟʏ ᴀ ʀᴀɴᴅᴏᴍ sᴛʀɪɴɢ ғʀᴏᴍ ᴀɴ Mᴀʟᴀʏᴀʟᴀᴍ ʟᴀɴɢ ᴀʀʀᴀʏ ᴏғ ʀᴇᴘʟɪᴇ.
- `/lnm` : ғɪɴᴅ ʏᴏᴜʀ ʟᴜᴄᴋʏ ɴᴜᴍʙᴇʀ.
- `/love` : ʟᴏᴠᴇ ʀᴇᴀᴄᴛɪᴏɴ😘
- `/toss` : ᴛᴏssᴇs ᴀ ᴄᴏɪɴ.
- `/shrug` : ɢᴇᴛ sʜʀᴜɢ xᴅ
- `/table` : ɢᴇᴛ ғʟɪᴘ/ᴜɴғʟɪᴘ :v
- `/decide` : ʀᴀɴᴅᴏᴍʟʏ ᴀɴsᴡᴇʀs ʏᴇs/ɴᴏ/ᴍᴀʏʙᴇ.
- `/truth` : ᴀsᴋs ʏᴏᴜ ᴀ ǫᴜᴇsᴛɪᴏɴ
- `/tord` : ᴄᴀɴ ʙᴇ ᴀ ᴛʀᴜᴛʜ ᴏʀ ᴀ ᴅᴀʀᴇ.
- `/dare` : ɢɪᴠᴇs ʏᴏᴜ ᴀ ᴅᴀʀᴇ
- `/rather` : ᴡᴏᴜʟᴅ ʏᴏᴜ ʀᴀᴛʜᴇʀ
- `/goodnight` : ɢᴏᴏᴅ ɴɪɢʜᴛ 😴
- `/morning` : ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌄
- `/abuse` : ʟᴀʙᴜsᴇ 🤬
- `/cry` : ᴄʀʏ 😭
- `/anime` : ᴀɴɪᴍᴇ
- `/metoo` : Mee to
- `/insultt` : Insult 😡
- `/engsongs` : English songs
- `/india` : type this to see india animation
"""

    ANIMAHYD_TXT = """
📚 **Animation commands***

- `/bombanimation`
- `/killanimation`
- `/clockanimation`
- `/earthanimation`
- `/moonanimation`
- `/loveanimation`
- `/amunganimation`
- `/lmaoanimation`
- `/monkeyanimation`
- `/muahanimation`

Powered by: @Htgtoolv4bot
"""
    INFORMATION_TXT = """
📚 **ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅ**

➪ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴜsᴇʀ's, ɢʀᴏᴜᴘ's, Bᴏᴛ's, ᴄʜᴀɴɴᴇʟ's Iᴅs.
ᴛʜɪs ɪs ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ғɪɴᴅɪɴɢ ᴍᴏᴅᴜʟᴇ, ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ғʀᴏᴍ ʜᴇʀᴇ

- sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪᴅ.
- ғᴏʀᴡᴀʀᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴀɴʏ ᴜsᴇʀ/ʙᴏᴛ/ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴏʀ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴs ᴛᴏ ɢᴇᴛ ɪᴅ.
- ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ / ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ɪᴅ.
- ᴜsᴇ /id ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ: ᴛᴏ ɢᴇᴛ ɪᴅ ᴛʜʀᴏᴜɢʜ ᴜsᴇʀɴᴀᴍᴇ.
- ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ: Tᴏ ɢᴇᴛ ɪᴅ ᴏғ ᴛʜᴀᴛ ᴄʜᴀᴛ.
- ғɪɴᴅ ʏᴏᴜʀ ᴅᴄ : ᴄʟɪᴄᴋ /dc ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴀᴛᴀᴄᴇɴᴛᴇʀ.
- /info : ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜsᴇʀ.
- ᴍᴇssᴀɢᴇ ɪᴅ : ᴊᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ /id ɪɴ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ᴍᴇssᴀɢᴇ ɪᴅ.
- /whois - ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ ᴀɴᴅ ɢʀᴏᴜᴘ.
"""
    YTTHUMB_TXT = """
📚 **ʏᴛᴛʜᴜᴍʙɴᴀɪʟ ᴄᴏᴍᴍᴀɴᴅ**

➪ sᴇɴᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.
`/ytthumb` ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʏᴛ ʟɪɴᴋ, ᴛᴏ ɢᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

**ᴇxᴀᴍᴘʟᴇ:**
`/ytthumb http://www.youtube.com/watch?v=HhjHYkPQ8F0`
"""

    PASTER_TXT = """
📚 **ᴘᴀsᴛᴇ**

➪ ᴘᴀsᴛᴇ sᴏᴍᴇ ᴛᴇxᴛs ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛs ᴏɴ ᴀ ᴡᴇʙsɪᴛᴇ!

**ᴇxᴀᴍᴘʟᴇ:**
- `/paste` [ᴛᴇxᴛ] - ᴘᴀsᴛᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴘᴀsᴛʏ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.",
"""

    TTS_TXT = """
📚 **ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ [ᴛᴛs]**

➪ ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ᴡɪᴛʜ ʟᴀɴɢᴜᴀɢᴇ sᴜᴘᴘᴏʀᴛ

**ᴇxᴀᴍᴘʟᴇ:**
- `/tts` : ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ I ᴡɪʟʟ ᴄᴏɴᴠᴇʀᴛ ᴀs ᴀᴜᴅɪᴏ.
"""

    GITHUB_TXT = """
📚 **ɢɪᴛʜᴜʙ**

➪ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʏᴏᴜʀ ɢɪᴛʜᴜʙ ᴘʀᴏғɪʟᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪɴ ᴍʏ ᴘᴍ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/github` [Usᴇʀɴᴀᴍᴇ]
"""

    COVID_TXT = """
📚 **ᴄᴏᴠɪᴅ Iɴғᴏʀᴍᴀᴛɪᴏɴ**

➪ ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ғɪɴᴅ ᴀʟʟ ᴄᴏᴜɴᴛʀʏ Iɴғᴏʀᴍᴀᴛɪᴏɴs. ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ ᴄᴏᴠɪᴅ Iɴғᴏʀᴍᴀᴛɪᴏɴs ᴏғ ᴀʟʟ ᴄᴏᴜɴᴛʀɪᴇs.

**ᴇxᴀᴍᴘʟᴇ:**
- `/covid` [ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ] - ᴜsᴇ ᴛʜɪs ᴍᴇᴛʜᴏᴅ Tᴏ ɢᴇᴛ ᴄᴏᴠɪᴅ Iɴғᴏʀᴍᴀᴛɪᴏɴs.
"""

    FORWERD_TXT = """
📚 **ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ʀᴇᴍᴏᴠᴇʀ**

➪ ɪ ᴀᴍ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇᴍᴏᴠᴇ ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ɢʀᴏᴜᴘ, ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ.
"""

    PLAYST_TXT = """
📚 **Anime**

➪ This is the anime themed fun & search module.

- `/animenews` - get anime news
- `/anime` {name} - Search animes in myanimelist.net.
- `/character` {name} - Search Character in myanimelist.net.
- `/upcoming` - details in upcoming animes in myanimelist.net.
- `/quotes` - random anime quotes.
"""

    REPORTS_TXT = """
📚 **ʀᴇᴘᴏʀᴛ** 💌</b>

<b>By using this command. You can contact me. Report anything of Any Type about this bot or else.📍</b>
<b>How it Works?</b>
- Send me the message you want to report.
- Reply that message with /report .
..
Done ✅.. I will forward that message to my Owner.
"""

    GOFILES_TXT = """
📚 **ɢᴏ ғɪʟᴇ**

ᴡʜᴀᴛ ɪs ɢᴏғɪʟᴇ!
➪ Gᴏғɪʟᴇ ɪs ᴀ ғʀᴇᴇ ᴀɴᴅ ᴜɴʟɪᴍɪᴛᴇᴅ ғɪʟᴇ sʜᴀʀɪɴɢ ᴀɴᴅ sᴛᴏʀᴀɢᴇ ᴘʟᴀᴛғᴏʀᴍ.
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɪᴛ ᴀs ᴀ ғɪʟᴇ ᴍᴀɴᴀɢᴇʀ ᴛᴏ sᴛᴏʀᴇ ᴀʟʟ ʏᴏᴜʀ ᴅᴀᴛᴀ, ᴏʀ ᴀs ᴀ sʜᴀʀɪɴɢ ᴘʟᴀᴛғᴏʀᴍ ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ᴏᴛʜᴇʀs. Aʟʟ ᴛʏᴘᴇs ᴏғ ғɪʟᴇs ᴀʀᴇ sᴜᴘᴘᴏʀᴛᴇᴅ (ғɪʟᴇs, ɪᴍᴀɢᴇs, ᴍᴜsɪᴄ, ᴠɪᴅᴇᴏs, ᴘᴅғ ᴇᴛᴄ...).
Tʜᴇʀᴇ ɪs ɴᴏ ʟɪᴍɪᴛ, ʏᴏᴜ ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴛ ᴛʜᴇ ᴍᴀxɪᴍᴜᴍ sᴘᴇᴇᴅ ᴏғ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴍᴏsᴛ ᴏғ ᴛʜᴇ sᴇʀᴠɪᴄᴇ ɪs ғʀᴇᴇ.
ᴡʜᴀᴛ ɪs ᴛʜᴇ ᴜsᴇ ᴏғ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ❓👇🏼
I ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴏғɪʟᴇ.ɪᴏ ᴀɴᴅ ʀᴇᴛᴜʀɴ ᴛʜᴇ ʟɪɴᴋ ᴇᴀsɪʟʏ.

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ ɢɪᴠᴇ ᴍᴇ ᴀɴʏ ғɪʟᴇ ɪᴍɢ ᴀɴʏᴛʜɪɴɢ
- `/go` - Rᴇᴘʟᴀʏ ᴛᴏ ᴀɴʏ ғɪʟᴇs, ᴛʜᴇɴ ɪ ᴜᴘʟᴏᴀᴅ ᴛᴏ ɢᴏғɪʟᴇ.ɪᴏ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ ᴀ ʟɪɴᴋ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ.
"""

    MUSICTAG_TXT = """
📚 **Anime Themed SFW:**

You can use this Commands in also groups, and reply to any user's
• Kiss : `/kiss` To Kiss A Person
• Highfive : `/highfive` To Highfive A Person
• Happy : `/happy` To Makes A Person Happy
• Laugh : `/laugh` To Makes A Person Laugh
• Bite : `/bite` To Bite A Person
• Poke : `/poke` To Poke A Person
• Tickle : `/tickle` To Tickle A Person
• Wave : `/wave` To Wave A Person
• Thumbsup : `/thumbsup` To Thumbsup A Person
• Stare : `/stare` To Makes A Person Stare
• Cuddle : `/cuddle` To Cuddle A Person
• Smile : `/smile` To Makes A Person Smile
• Baka : `/baka` To Say A Person Baka
• Blush : `/blush` To Makes A Person Blush
• joke : `/joke` To make A joke
• /wallpaper, /ngif, /gasm, /foxgirl, /8ball

**Message as to Lang below click the more button know more commandslist!!**
"""
    JIFFUN_TXT = """
• Think : `/think` To Makes A Person Think
• Pout : `/pout` To Makes A Person Pout
• Facepalm : `/facepalm` To Makes A Person Facepalm
• Wink : `/wink` To Makes A Person Wink
• Smug : `/smug` To Makes A Person Smug
• Cry : `/crying` To Makes A Person Cry
• Dance : `/dance` To Makes A Person Dance
• Feed : `/feed` To Feed A Person
• Shrug : `/shrug` To Shrug A Person
• Bored : `/bored` To Makes A Person Bored
• Pat : `/pat` To Pat A Person
• Hug : `/hug` To Hug A Person
• Slap : `/slap` To Slap A Person
• Cute : `/cute` To Say Me Cute
• Waifu : `/waifu` To Send Random Waifu Image
• Kitsune : `/kitsune` To Send Random Kitsune Image
• Sleep : `/sleep` To Say I Am Going To Sleep
• Neko : `/neko` To Get Random Neko quotes
"""

    MEMESS_TXT = """
📚 **ᴍᴇᴍᴇs**

This is the module for funny memes🦹, 
just give the `/mame` command Group or my pm.

- meme : `/meme` To make a fun meme
"""
    SHAZAM_TXT = """ 
📚 **sʜᴀᴢᴀᴍ** 

➪ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴘᴀʀᴛ ᴏғ ᴀ sᴏɴɢ, ʙᴜᴛ ᴄᴏᴜʟᴅ ɴᴏᴛ ғɪɴᴅ ᴏᴜᴛ ᴡʜᴀᴛ ᴛʜᴀᴛ sᴏɴɢ ɪs?
ʜᴇʀᴇ's ᴛʜᴇ ʙᴇsᴛ sᴏʟᴜᴛɪᴏɴ ғᴏʀ ʏᴏᴜ.
ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴀᴜᴅɪᴏ ғɪʟᴇ sᴀᴍᴘʟᴇ ᴀɴᴅ I'ʟʟ ᴛᴇʟʟ ʏᴏᴜ ᴡʜᴀᴛ ɪs ᴛʜᴀᴛ sᴏɴɢ.

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴀᴜᴅɪᴏ
- ʀᴇᴘʟʏ ʏᴏᴜʀ ᴛᴏ ᴀᴜᴅɪᴏ ᴡɪᴛʜ ᴛʜɪs `/audify` ᴄᴏᴍᴍᴀɴᴅ
- `/audify` : ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ
"""

    ANONFILS_TXT = """
📚 **ᴀɴᴏɴʏᴍᴏᴜs ғɪʟᴇ's ᴜᴘʟᴏᴀᴅᴇr**

➪ ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ᴀɴᴏɴғɪʟᴇs.ᴄᴏᴍ ᴀɴᴅ ʀᴇᴛᴜʀɴ ᴛʜᴇ ʟɪɴᴋ ᴇᴀsɪʟʏ.
 
**ᴇxᴀᴍᴘʟᴇ:**
- `/anon` : Rᴇᴘʟᴀʏ ᴛᴏ ᴀɴʏ ғɪʟᴇs,ɪᴍɢ ᴇɢ.. ᴢᴀᴘGᴇᴛ ᴀɴᴏɴғɪʟᴇs.ᴄᴏᴍ ʟɪɴᴋ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ.
"""

    YTTAGFY_TXT = """
📚 **ʏᴏᴜᴛᴜʙᴇ ᴛᴀɢ ғɪɴᴅᴇʀ**

➪ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛʜᴀᴛ ᴄᴀɴ ᴇxᴛʀᴀᴄᴛ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛᴀɢ ᴇᴀsʏ.
‼️ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪs ғᴏʀ ʏᴏᴜᴛᴜʙᴇʀs. ʙᴇᴄᴀᴜsᴇ ᴛʜᴇʏ ʜᴀᴠᴇ ᴡᴏʀᴋ ᴏғ ᴛʜᴇ ᴛᴀɢs. ᴏᴛʜᴇʀs ᴄᴀɴ ɪɢɴᴏʀᴇ ᴛʜɪs.‼️
<b>How it Works 🙂?</b>
 Send me a message in the below format:-
- `/yttags` [youtube link]
- <code>/yttags http://www.youtube.com/watch?v=bPs0xFd4skY</code>
- `/yttags` : Reply to some Youtube link...
ᴀɴᴅ ɪ ᴇxᴛʀᴀᴄᴛ ᴛᴀɢ ғᴏʀ ᴜ
"""

    FILTOVID_TXT = """
📚 **ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ**

➪ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ғᴏʀ ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇ,

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪsᴛ ɢɪᴠᴇ ᴍᴇ ᴀ ғɪʟᴇ
- `/convert2video` : ʀᴇᴘʟᴀʏ ᴛᴏ ғɪʟᴇ ғᴏʀ ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ᴠɪᴅᴇᴏ.
"""

    VIDTOFIL_TXT = """
📚 **ᴠɪᴅᴇᴏ ᴛᴏ ғɪʟᴇ**

➪ ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴛᴏ ғɪʟᴇ ᴍᴏᴅᴜʟᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ ɢɪᴠᴇ ᴍᴇ ᴀ ғɪʟᴇ
- `/convert2file` : ʀᴇᴘʟʏ ᴛᴏ ᴄᴏɴᴠᴇʀᴛɪɴɢ Fɪʟᴇ.
"""

    PINGS_TXT = """
📚 **ᴘɪɴɢ**

➪ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ʀᴀᴍ, ᴄᴘᴜ ᴇᴛᴄ sᴛᴀᴛs ᴏғ Bᴏᴛ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/ping` : Cʜᴇᴄᴋ ɪғ Bᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.
"""

    PASSWED_TXT = """
📚 **ᴘᴀssᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴇʀ**

➪ ᴛʜɪs ɪs ᴀ ᴘᴀssᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ ᴍᴏᴅᴜʟᴇ, ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴘᴀssᴡᴏʀᴅ ғʀᴏᴍ ʜᴇʀᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/genpassword`
"""

    IMDBS_TXT = """
📚 **ᴍᴏᴠɪᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ [ɪᴍᴅʙ]**

➪ ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴs, ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ ᴍᴏᴠɪᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴs Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs.

**ᴇxᴀᴍᴘʟᴇ:**
- `/imdb` [ᴍᴏᴠɪᴇ ɴᴀᴍᴇ] : ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ.
- `/sᴇᴀʀᴄʜ` : ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs
"""

    STYLISHT_TXT = """
📚 **sᴛʏʟɪsʜ ᴛᴇxᴛ**

➪ ᴀ ᴍᴏᴅᴜʟᴇ ғᴏʀ sᴛʏʟɪsʜ ᴛᴇxᴛ
ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ɢᴇᴛ sᴛʏʟɪsʜ ғᴏɴᴛs.
ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ sᴏᴍᴇ ᴛᴇxᴛ & ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ sᴛʏʟɪsʜ ᴛᴇxᴛ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/text` [text]: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴀs ᴛᴏ ᴍᴀᴋᴇ sᴛʏʟɪsʜ ᴛᴇxᴛ.
"""

    HANDWRIT_TXT = """
📚 **ʜᴀɴᴅᴡʀɪᴛɪɴɢ**

➪ᴛʜɪs ᴀɴ ʜᴀɴᴅᴡʀɪᴛɪɴɢ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴍᴏᴅᴜʟᴇ,
sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇxᴛ, I'ʟʟ ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʜᴀɴᴅᴡʀɪᴛɪɴɢ. (ʙᴏᴛ ᴄᴀɴ'ᴛ ᴄᴏɴᴠᴇʀᴛ sᴏᴍᴇ ʟᴀɴɢᴜᴀɢᴇs)

**ᴇxᴀᴍᴘʟᴇ:**
- /h
- `/write` [ʏᴏᴜʀ ᴛᴇxᴛ] : To handwriting converter
"""

    ALIVED_TXT = """
😌 **ᴀʟɪᴠᴇ**

😒ᴛᴏ ғɪɴᴅ ᴏᴜᴛ Iғ I'ᴍ 🤒ᴅᴇᴀᴅ ᴏʀ ɴᴏt

**ᴇxᴀᴍᴘʟᴇ:**
- `/alive` - ᴅᴇᴀᴅ ᴏʀ ɴᴏᴛ",
"""

    PDFTOTXT_TXT = """
📚 **ᴘᴅғ ᴛᴏ ᴛᴇxᴛ**

➪ ᴀ ᴍᴏᴅᴜʟᴀʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴡʜɪᴄʜ ᴘʀᴏᴠɪᴅᴇs ᴘᴅғ ᴛᴏᴏʟs ᴜsɪɴɢ ᴘʏᴘᴅғ𝟸 ғᴏʀᴋ, 
sᴇɴᴅ ᴍᴇ ᴀ ᴘᴅғ ғɪʟᴇ ᴛᴏ ᴍᴏᴠᴇ ᴏɴ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/pdf2txt` : ᴇxᴛʀᴀᴄᴛ ᴛᴇxᴛ ᴛᴏ ᴛᴇxᴛ ғɪʟᴇ.
- `/pinfo` : ᴛᴏ ɢᴇᴛ ᴘᴅғ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
"""

    AUDIOBOOK_TXT = """
📚 **ᴘᴅғ ᴛᴏ ᴀᴜᴅɪᴏʙᴏᴏᴋ**

➪ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴏɴᴠᴇʀᴛs ᴘᴅғ ᴛᴏ ᴀᴜᴅɪᴏ ᴜsɪɴɢ ᴘʏᴘᴅғ𝟸 ᴀɴᴅ ɢᴛᴛs.
ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴘᴅғ ᴛʜᴇɴ ɪᴍ ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴀᴜᴅɪᴏʙᴏᴏᴋ

**ᴇxᴀᴍᴘʟᴇ:**
- `/audiobook` : ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴘᴅғ ғɪʟᴇ ᴏɴʟʏ.
"""

    CARBON_TXT = """
📚 **ᴄᴀʀʙᴏɴ Iᴍᴀɢᴇ**

➪ ɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ᴍᴏᴅᴜʟᴇ. I ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇs ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ.

**ᴇxᴀᴍᴘʟᴇ:**
◉ `/carbon` : ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ.
"""

    NOLINKS_TXT = """
📚 **ʀᴇᴍᴏᴠᴇ ᴜʀʟ's**

➪ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴡʜᴏ sᴇɴᴅs ᴀɴʏ ᴋɪɴᴅ ᴏғ ʟɪɴᴋ ,ʀᴇᴍᴏᴠᴇ ᴀʟʟ ʟɪɴᴋs ғʀᴏᴍ ɢʀᴏᴜᴘ.

**ʟɪsᴛ ᴏғ ʟɪɴᴋs ɪ ᴅᴇʟᴇᴛᴇ!**
- https
- http
- t.me
- www
- com
"""

    STIKERPH_TXT =  """
📚 **sᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ & image to sticker**

➪ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ,
ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ sᴛɪᴄᴋᴇʀ, ᴛʜᴇɴ ɪ ɢɪᴠᴇ ʏᴏᴜ ᴀ Iᴍᴀɢᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʜᴇʀᴇ sᴛɪᴄᴋᴇʀ

ᴅᴏɴ'ᴛ sᴇɴᴅ ᴍᴇ ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ ᴏʀ ᴠɪᴅᴇᴏ sᴛɪᴄᴋᴇʀ.
"""

    SHARET_TXT = """
📚 **sʜᴀʀᴇ ᴛᴇxᴛ**

➪ ᴀ ʙᴏᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʟɪɴᴋ ᴛᴏ sʜᴀʀᴇ ᴛᴇxᴛ ɪɴ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ

**ᴇxᴀᴍᴘʟᴇ:**
- `/share` - ɢᴇᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴛᴇxᴛ ᴏʀ ʟɪɴᴋ.
"""

    URLSHORT_TXT = """
📚 **ᴜ𝗋𝗅 sʜᴏʀᴛɴᴇʀ**

➪ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ sʜᴏʀᴛ ᴀ ᴜʀʟ.
`/short` 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌.

**ᴇxᴀᴍᴘʟᴇ:**
`/short https://t.me/htgtoolv4bot`
"""

    TAGALL_TXT = """
📚 **ᴛᴀɢᴀʟʟᴀ**

➪ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴛᴀɢᴀʟʟ, ɪ ᴄᴀɴ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/tag` : ᴊᴜsᴛ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
"""

    UNZIPER_TXT = """
📚 **ᴜɴᴢɪᴘᴇʀ**

➪ ɪ ᴄᴀɴ ᴜɴᴢɪᴘ ᴢɪᴘ ғɪʟᴇ's, ғɪʀsᴛ ɢɪᴠᴇ ᴍᴇ ᴢɪᴘ ғɪʟᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ sᴇɴᴅ ᴍᴇ ᴢɪᴘ ғɪʟᴇ.
- ᴛʜᴇɴ `/unzip` ᴛᴏ ʀᴇᴘʟᴀʏ  ᴢɪᴘ ғɪʟᴇ
"""

    RENAMEER_TXT = """
📚 **ʀᴇɴᴀᴍᴇʀ ᴍᴏᴅᴜʟᴇ**

➪ I ᴄᴀɴ ᴛɢʀᴇɴᴀᴍᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ.
ɪ ᴀᴍ  sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇʀ ᴍᴏᴅᴜʟᴇ.ᴅᴏᴡɴʙᴇʟᴏᴡ ᴍʏ ᴡᴏʀᴋɪɴɢ sᴛᴇᴘs

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ ɢɪᴠᴇ ᴍᴇ ᴀ ғɪʟᴇ
- /rename : ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ғɪʟᴇ ᴡɪᴛʜ /ʀᴇɴᴀᴍᴇ ғɪʟᴇɴᴀᴍᴇ.ᴇxᴛᴇɴsɪᴏɴ ғᴏʀ ʀᴇɴᴀᴍɪɴɢ.
"""

    SCRESHOT_TXT = """
📚 **sᴄʀᴇᴇɴsʜᴏᴛ ɢᴇɴᴇʀᴀᴛᴏʀ**

➪ ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ sᴄʀᴇᴇɴsʜᴏᴛ ɢᴇɴᴇʀᴀᴛᴏʀ ᴍᴏᴅᴜʟᴇ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ғʀᴏᴍ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs ᴡɪᴛʜ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ᴇɴᴛɪʀᴇ ғɪʟᴇ.

**ᴇxᴀᴍᴘʟᴇ:**
`/screenshot` : ᴊᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ғɪʟᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ
"""

    TRIMER_TXT = """
📚 **ᴛʀɪᴍ ᴍᴇᴅɪᴀ**

➪ ᴛʜɪs ɪs ᴀɴ ᴍᴇᴅɪᴀ ᴛʀɪᴍ ᴍᴏᴅᴜʟᴇ, ʏᴏᴜ ᴄᴀɴ ᴛʀɪᴍ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ɪɴ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ

**ᴇxᴀᴍᴘʟᴇ:**
- ғɪʀsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ `/downloadmedia` ᴄᴏᴍᴍᴀɴᴅ 
- `/trim` : ᴛʀɪᴍ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ
- `/storage` : ғɪɴᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ɪɴ ᴍʏ ᴅʙ
"""

    PLAYRER_TXT = """
**ᴘʟᴀʏᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ**

»ᴊᴜsᴛ `/play` [sᴏɴɢ ɴᴀᴍᴇ] ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴊᴏɪɴᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

» `/play` (sᴏɴɢ/ʏᴛ ʟɪɴᴋ) : ᴩʟᴀʏ's ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴀs ᴀᴜᴅɪᴏ.
» `/pause` : ᴩᴀᴜsᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.
» `/resume` : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.
» `/skip` : sᴋɪᴩ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.
» `/end` : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ʟᴇᴀᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ.

» ᴍʏ ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ: @assistanttg
**ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏʜʀɪx ᴛᴏᴏʟs ʙᴏᴛ**
"""

    ANIMATION_TXT = """
Animation 

You want to animate again?
Click down botton.
"""
    
    WHATSAPPS_TXT = """
📚 **ᴡʜᴀᴛsᴀᴘᴘ sʜᴀʀᴇ ᴛxᴛ**

ᴡɪᴛʜ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ʏᴏᴜ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ᴄᴜsᴛᴏᴍ ᴍᴇssᴀɢᴇs ᴛᴏ sᴇɴᴅ ᴠɪᴀ ʟɪɴᴋ!

**ᴇxᴀᴍᴘʟᴇ:** `/washare hello`
"""
    BEYFILS_TXT = """
📚 **ʙᴀʏ ғɪʟᴇ's ᴜᴘʟᴏᴀᴅᴇr**

➪ ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ bayfile.com ᴀɴᴅ ʀᴇᴛᴜʀɴ ᴛʜᴇ ʟɪɴᴋ ᴇᴀsɪʟʏ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/bay` - zapGet bayfiles.com link of telegram file.
- `/transfersh` - upload to transfer.sh
"""
    WIKIPDS_TXT = """
📚 <b>ᴡɪᴋɪᴘᴇᴅɪᴀ</b>

➪ ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ғɪɴᴅ ᴀɴᴅ sʜᴀʀᴇ ʟɪɴᴋs ᴛᴏ ᴡɪᴋɪᴘᴇᴅɪᴀ ᴀʀᴛɪᴄʟᴇs. 
ǫᴜɪᴄᴋ ᴡɪᴋɪ sᴇᴀʀᴄʜᴇs ᴛʜʀᴏᴜɢʜ Tᴇʟᴇɢʀᴀᴍ.
Wikipedia bot! Type `/wiki {search query}`
**Exᴀᴍᴘʟᴇ:**
- /wiki [search input]
"""
    QUOTES_TXT = """
📚 **ǫᴜᴏᴛᴇs**

➪ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ sᴜᴘᴘᴏʀᴛᴇᴅ ᴄᴀᴛᴇɢᴏʀɪᴇs ᴏғ ǫᴜᴏᴛᴇs:
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀɴʏ ᴏғ ᴛʜᴇᴍ ʙʏ ᴜsɪɴɢ: <code>/quot</code> [category]
**Tʜɪs ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ Qᴜᴏᴛᴇ ᴏғ ᴛʜᴀᴛ ᴄᴀᴛᴇɢᴏʀʏ.**

**CATEGORIES:**
<code>business</code>, <code>education</code>, <code>faith</code>, <code>famous-quotes</code>, <code>friendship</code>, <code>future</code>, <code>happiness</code>, <code>history</code>, <code>inspirational</code>, <code>life</code>, <code>literature</code>, <code>love</code>, <code>nature</code>, <code>politics</code>, <code>proverb</code>, <code>religion</code>, <code>science</code>, <code>success</code>, <code>technology</code>, <code>wisdom</code>
"""
    ATTACHLINK_TXT = """
📚 <b>ᴀᴛᴛᴀᴄʜ ʟɪɴᴋ</b>

➪ ғᴜɴᴄᴛɪᴏɴ: <b>ᴀᴛᴛᴀᴄʜ ᴛʜᴇ ʟɪɴᴋ ᴡɪᴛʜ ᴛᴇxᴛ ᴏʀ ᴍᴇᴅɪᴀ.📍</b>
<b>ʜᴏᴡ ɪᴛ's ᴡᴏʀᴋ?</b>
- sᴇɴᴅ ᴍᴇ ᴀ <b>ᴍᴇᴅɪᴀ ᴏʀ ᴀ ᴛᴇxᴛ.</b>
- ʀᴇᴘʟʏ ᴛʜᴀᴛ <b>ᴍᴇᴅɪᴀ ᴏʀ ᴛᴇxᴛ</b> ᴡɪᴛʜ ᴀ <b>ʟɪɴᴋ</b>
- <b>Done ✅ : ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴀᴛᴛᴀᴄʜᴇᴅ ʟɪɴᴋ.</b>
"""
    IMG2PDF_TXT = """
📚 <b>Iᴍᴀɢᴇ ᴛᴏ ᴘᴅғ</b>

➪ <b>ᴄᴏɴᴠᴇʀᴛ ᴀɴʏ ᴛʏᴘᴇ ᴏғ ɪᴍᴀɢᴇ(s) ᴛᴏ ᴘᴅғ, .ᴘᴅғ ғɪʟᴇ ғᴏʀᴍᴀᴛ.</b>
<b>ʜᴏᴡ ɪᴛ ᴡᴏʀᴋs?</b>
- Send an <b>Image.</b>. {Not as Document}
- ɴᴏᴡ, ʏᴏᴜ ʜᴀᴠᴇ 𝟹 ᴏᴘᴛɪᴏɴs.
1.  If you want to <b>add</b> more image, Send me <b>images One by One</b>. When done send `/c2pdf`
2.  If <b>done</b> click here  or send  `/c2pdf`
3. If you want to <b>cancel or clear</b> this <b>list or queue or process</b>. Send `/clearpdfcache`

<i>YOU WILL GET YOUR REPLY ON THE BASIS OF COMMAND YOU SEND ( `/C2PDF` OR `/CLEARPDFCACHE`) </i>
""" 
    JOKES_TXT = """
📚 <b>Joke</b>

➪ <b>Get a Random Joke each time. 😂</b>
<b>How it Works ?</b>
- Send the command `/jokes` to get a joke.
"""
    INSPIRE_TXT = """
📚 <b>Inspire Me</b>

<b>Get yourself Inspired with a quote and an image...😱✨</b>
<b>How it Works?</b>
- Send the command `/inspire`
"""
