#Made by Hydrix

import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

import pytz
from datetime import datetime



#===================================
IST = pytz.timezone('Asia/Kolkata')

#Iindian-time-zone
@Client.on_message(filters.command("indtime"))
async def india_time(bot, hydrix):
    datetime_ist = datetime.now(IST)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Indian Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
BGS = pytz.timezone('Asia/Dhaka')

#bangladhesh-time-zone
@Client.on_message(filters.command("banglatime"))
async def bang_time(bot, hydrix):
    datetime_ist = datetime.now(BGS)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Bangladesh Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
AFG = pytz.timezone('Asia/Kabul')

#Afganistan-time-zone
@Client.on_message(filters.command("afgantime"))
async def afga_time(bot, hydrix):
    datetime_ist = datetime.now(AFG)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Afghanistan Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
ALB = pytz.timezone('Europe/Tirane')

#Albania-time-zone
@Client.on_message(filters.command("albaniatime"))
async def albania_time(bot, hydrix):
    datetime_ist = datetime.now(ALB)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Albanian Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
ANT = pytz.timezone('Antarctica/Casey')

#Antarctica-time-zone
@Client.on_message(filters.command("antarcticatime"))
async def antartica_time(bot, hydrix):
    datetime_ist = datetime.now(ANT)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Antarctican Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
ARM = pytz.timezone('Asia/Yerevan')

#Armenia-time-zone
@Client.on_message(filters.command("armeniatime"))
async def armeni_time(bot, hydrix):
    datetime_ist = datetime.now(ARM)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Armenia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
AUS = pytz.timezone('Antarctica/Macquarie')

#Australia-time-zone
@Client.on_message(filters.command("australiatime"))
async def autralia_time(bot, hydrix):
    datetime_ist = datetime.now(AUS)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Australia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
AZB = pytz.timezone('Asia/Baku')

#Azerbaijan-time-zone
@Client.on_message(filters.command("azerbaijantime"))
async def azerbej_time(bot, hydrix):
    datetime_ist = datetime.now(AZB)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Azerbaijan Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
AUST = pytz.timezone('Europe/Vienna')

#Austria-time-zone
@Client.on_message(filters.command("austriatime"))
async def austria_time(bot, hydrix):
    datetime_ist = datetime.now(AUST)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Austria Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
BHRN = pytz.timezone('Asia/Bahrain')

#Bahrain-time-zone
@Client.on_message(filters.command("bahrintime"))
async def baharin_time(bot, hydrix):
    datetime_ist = datetime.now(BHRN)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Bahrain Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
BELG = pytz.timezone('Europe/Brussels')

#Belgium-time-zone
@Client.on_message(filters.command("belgiamtime"))
async def belgian_time(bot, hydrix):
    datetime_ist = datetime.now(BELG)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Belgium Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
ARGN = pytz.timezone('America/Argentina/Buenos_Aires')

#Argentina-time-zone
@Client.on_message(filters.command("argentinatime"))
async def argentina_time(bot, hydrix):
    datetime_ist = datetime.now(ARGN)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Argentina Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
BELG = pytz.timezone('Europe/Brussels')

#Belgium-time-zone
@Client.on_message(filters.command("belgiumtime"))
async def belgium_time(bot, hydrix):
    datetime_ist = datetime.now(BELG)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Belgium Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
BRAZ = pytz.timezone('America/Rio_Branco')

#Brazil-time-zone
@Client.on_message(filters.command("braziltime"))
async def brazila_time(bot, hydrix):
    datetime_ist = datetime.now(BRAZ)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Brazil Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
CHIL = pytz.timezone('America/Santiago')

#Chile-time-zone
@Client.on_message(filters.command("chiletime"))
async def chili_time(bot, hydrix):
    datetime_ist = datetime.now(CHIL)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Chile Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
CHIN = pytz.timezone('Asia/Shanghai')

#China-time-zone
@Client.on_message(filters.command("chinatime"))
async def china_time(bot, hydrix):
    datetime_ist = datetime.now(CHIN)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**China Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
CAMB = pytz.timezone('Asia/Phnom_Penh')

#Cambodia-time-zone
@Client.on_message(filters.command("cambotime"))
async def cambodia_time(bot, hydrix):
    datetime_ist = datetime.now(CAMB)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Cambodia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
CAND = pytz.timezone('America/Yellowknife')

#Canada-time-zone
@Client.on_message(filters.command("canadatime"))
async def canada_time(bot, hydrix):
    datetime_ist = datetime.now(CAND)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Canada Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
EGPT = pytz.timezone('Africa/Cairo')

#Egypt-time-zone
@Client.on_message(filters.command("egyptime"))
async def egipth_time(bot, hydrix):
    datetime_ist = datetime.now(EGPT)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Egypt Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
ETHI = pytz.timezone('Africa/Addis_Ababa')

#Ethiopia-time-zone
@Client.on_message(filters.command("ethiotime"))
async def ethiopia_time(bot, hydrix):
    datetime_ist = datetime.now(ETHI)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Ethiopia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
FRAN = pytz.timezone('Europe/Paris')

#France-time-zone
@Client.on_message(filters.command("fracetime"))
async def franc_time(bot, hydrix):
    datetime_ist = datetime.now(FRAN)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**France Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
GEOR = pytz.timezone('Asia/Tbilisi')

#Georgia-time-zone
@Client.on_message(filters.command("geortime"))
async def georjia_time(bot, hydrix):
    datetime_ist = datetime.now(GEOR)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Georgia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)


#===================================
GERMA = pytz.timezone('Europe/Berlin')

#Germany-time-zone
@Client.on_message(filters.command("germatime"))
async def germany_time(bot, hydrix):
    datetime_ist = datetime.now(GERMA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Germany Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#===================================
GREEC = pytz.timezone('Europe/Athens')

#Greece-time-zone
@Client.on_message(filters.command("greecetime"))
async def greece_time(bot, hydrix):
    datetime_ist = datetime.now(GREEC)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Greece Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
HOKO = pytz.timezone('Asia/Hong_Kong')

#HongKong-time-zone
@Client.on_message(filters.command("hongkongtime"))
async def hongkog_time(bot, hydrix):
    datetime_ist = datetime.now(HOKO)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Hong Kong Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
HUNGA = pytz.timezone('Europe/Budapest')

#Hungary-time-zone
@Client.on_message(filters.command("hungarytime"))
async def hungary_time(bot, hydrix):
    datetime_ist = datetime.now(HUNGA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Hungary Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
ICLA = pytz.timezone('Atlantic/Reykjavik')

#icland-time-zone
@Client.on_message(filters.command("icelandtime"))
async def icla_time(bot, hydrix):
    datetime_ist = datetime.now(ICLA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Iceland Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
INDO = pytz.timezone('Asia/Jayapura')

#indonetia-time-zone
@Client.on_message(filters.command("indonetime"))
async def indone_time(bot, hydrix):
    datetime_ist = datetime.now(INDO)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Indonesian Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
IRAQ = pytz.timezone('Asia/Baghdad')

#eraq-time-zone
@Client.on_message(filters.command("iraqtime"))
async def iraq_time(bot, hydrix):
    datetime_ist = datetime.now(IRAQ)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Iraq Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
ITAL = pytz.timezone('Europe/Rome')

#Italy-time-zone
@Client.on_message(filters.command("Italytime"))
async def italy_time(bot, hydrix):
    datetime_ist = datetime.now(ITAL)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Italy Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
JAPP = pytz.timezone('Asia/Tokyo')

#Japan-time-zone
@Client.on_message(filters.command("japantime"))
async def jappan_time(bot, hydrix):
    datetime_ist = datetime.now(JAPP)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Japan Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
MALE = pytz.timezone('Asia/Kuching')

#Malaysia-time-zone
@Client.on_message(filters.command("malaysiatime"))
async def malesh_time(bot, hydrix):
    datetime_ist = datetime.now(MALE)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Malaysia Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
MAXC = pytz.timezone('America/Mexico_City')

#Mexico-time-zone
@Client.on_message(filters.command("mexicotime"))
async def maxic_time(bot, hydrix):
    datetime_ist = datetime.now(MAXC)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Mexico Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
NZLD = pytz.timezone('Pacific/Auckland')

#Newzealand-time-zone
@Client.on_message(filters.command("newzetime"))
async def nezeeelf_time(bot, hydrix):
    datetime_ist = datetime.now(NZLD)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**New Zealand Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
PANA = pytz.timezone('America/Panama')

#Panama-time-zone
@Client.on_message(filters.command("panamatime"))
async def panama_time(bot, hydrix):
    datetime_ist = datetime.now(PANA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Panama Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
PHLI = pytz.timezone('Asia/Manila')

#Philippines-time-zone
@Client.on_message(filters.command("philiptime"))
async def pilipi_time(bot, hydrix):
    datetime_ist = datetime.now(PHLI)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Philippines Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
POLAD = pytz.timezone('Europe/Warsaw')

#Poland-time-zone
@Client.on_message(filters.command("polandtime"))
async def poland_time(bot, hydrix):
    datetime_ist = datetime.now(POLAD)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Poland Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
PORTU = pytz.timezone('Atlantic/Azores')

#Portugal-time-zone
@Client.on_message(filters.command("portutime"))
async def portu_time(bot, hydrix):
    datetime_ist = datetime.now(PORTU)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Portugal Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
QATA = pytz.timezone('Asia/Qatar')

#Qatar-time-zone
@Client.on_message(filters.command("qatartime"))
async def qatar_time(bot, hydrix):
    datetime_ist = datetime.now(QATA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Qatar Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
ROMA = pytz.timezone('Europe/Bucharest')

#Romania-time-zone
@Client.on_message(filters.command("romanitime"))
async def roman_time(bot, hydrix):
    datetime_ist = datetime.now(ROMA)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Romania Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)
#===================================
RUSS = pytz.timezone('Asia/Anadyr')

#Russian-time-zone
@Client.on_message(filters.command("russiatime"))
async def russi_time(bot, hydrix):
    datetime_ist = datetime.now(RUSS)
    ISTIME = datetime_ist.strftime("`%I:%M:%S %p`\n├⎆**DATE:** `%d %B %Y`\n╰──────────⎆")
    await hydrix.reply_sticker(
        sticker="CAACAgIAAxkBAAIXEGK0KLgkNetwAAHFa07eD4yTn0PPxQACTgADWbv8JQ3rz9n50HgqHgQ"             
    )
    
    text = f"""
╭──────────⎆
├⎆**Russian Time**
│
├⎆**TIME:** {ISTIME}
"""

    await hydrix.reply_text(text=text)

#==============➪=============➪========
# Service clear--------------------
@Client.on_message(filters.service)
async def delete(bot,message):
 await message.delete() 

# Group forword rm------
@Client.on_message(filters.group & filters.forwarded)
async def forward(bot, message):
    await message.delete("This group doesn't allow forward messages")
    
#Inline search Remove---
@Client.on_message(filters.via_bot & filters.group)
async def inline(bot,message):
     await message.delete()
