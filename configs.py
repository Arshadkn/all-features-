import os







class Config(object):
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "784589736 5013387325").split())
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    DEF_WATER_MARK_FILE = "Uploaded by: @HTgToobot"
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DATABASE_URL = os.environ.get("mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

   


