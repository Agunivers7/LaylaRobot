
import os


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 10651048  # integer value, dont use ""
    API_HASH = "37775aca7d11f450ecde375baac17fe7"
    TOKEN = "5743646572:AAEn0QWcJtEMN3EbRRj_rNoshdhRZfqrKb8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1323557247  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "@Spoidermon12"
    MONGO_DB_URI = "mongodb+srv://Aadhi:42426840@cluster0.h9rky.mongodb.net/?retryWrites=true&w=majority"
    SUPPORT_CHAT = "Agunivers_backup"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -647696969
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -647696969
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://apex:aadhi@8.219.177.252:5432/apexdb"  # needed for any database modules
    REDIS_URI = "redis-10774.c265.us-east-1-2.ec2.cloud.redislabs.com:10774"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "TcOjJ8pWGP8OxnkQWQqORD3LVm8qp8rNvZ~hP9A27fMw~fnUfWk3TvITNTkqnGyG"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 1323557247
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 1323557247
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 1323557247
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 1323557247
    WOLVES = 1323557247
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
