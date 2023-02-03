
from pyrogram import Client, filters
from pymongo import MongoClient
import os
from info import DATABASE_URI

Chat_Group = [-1001500208686]





levellink =["https://telegra.ph/file/6620fe683ff3989268c7f.mp4", "https://telegra.ph/file/c6bbce91cb75d4ab318ae.mp4", "https://telegra.ph/file/c2ac7b63d248f49da952c.mp4", "https://telegra.ph/file/b100466a5f0c42fa7255f.mp4", "https://telegra.ph/file/67c9dc7b59f78aa7aaf4c.mp4", "https://telegra.ph/file/06e2d74343e89c9d3cd12.mp4", "https://telegra.ph/file/88458a18eea8e86292b14.mp4", "https://telegra.ph/file/e3786d4f321ff4335a70f.mp4"]
levelname = ["Team Rocket", "Stray God", "Vector", "Hero Association", "Z Warrior", "Black Knight", "Ghoul", "Overlord"]
levelnum = [2,5,15,25,35,50,70,100]




@Client.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & ~filters.private,
    group=8,
)
async def level(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    

    leveldb = MongoClient(DATABASE_URI)
    
    level = leveldb["LevelDb"]["Level"] 
 
    if message.chat.id in Chat_Group:
        xpnum = level.find_one({"level": user_id})

        if not message.from_user.is_bot:
            if xpnum is None:
                newxp = {"level": user_id, "xp": 10}
                level.insert_one(newxp)   
                    
            else:
                xp = xpnum["xp"] + 10
                level.update_one({"level": user_id}, {
                    "$set": {"xp": xp}})
                l = 0
                while True:
                    if xp < ((50*(l**2))+(50*(l))):
                         break
                    l += 1
                xp -= ((50*((l-1)**2))+(50*(l-1)))
                if xp == 0:
                    await message.reply_text(f"🌟 {message.from_user.mention}, You have reached level {l}**, Nothing can stop you on your way!")
    
                    for lv in range(len(levelname)) and range(len(levellink)):
                            if l == levelnum[lv]:            
                                Link = f"{levellink[lv]}"
                                await message.reply_video(video=Link, caption=f"{message.from_user.mention}, You have reached Rank Name **{levelname[lv]}**")
                  

                               
@Client.on_message(
    filters.command("rank", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rank(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    
    
    leveldb = MongoClient(DATABASE_URI)
    
    level = leveldb["LevelDb"]["Level"] 
    
    if message.chat.id in Chat_Group:
        xpnum = level.find_one({"level": user_id})
        xp = xpnum["xp"]
        l = 0
        r = 0
        while True:
            if xp < ((50*(l**2))+(50*(l))):
                break
            l += 1

        xp -= ((50*((l-1)**2))+(50*(l-1)))
        rank = level.find().sort("xp", -1)
        for k in rank:
            r += 1
            if xpnum["level"] == k["level"]:
                break                     
        await message.reply_text(f"{message.from_user.mention} Level Info:\nLevel: {l}\nProgess: {xp}/{int(200 *((1/2) * l))}\n Ranking: {r}")


