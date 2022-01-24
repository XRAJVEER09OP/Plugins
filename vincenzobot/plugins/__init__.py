import datetime
import time

from vincenzobot import *
from vincenzobot.clients import *
from vincenzobot.config import Config
from vincenzobot.helpers import *
from vincenzobot.utils import *
from vincenzobot.random_strings import *
from vincenzobot.version import __hell__
from vincenzobot.sql.gvar_sql import gvarstat
from telethon import version

hell_logo = "./vincenzobot/resources/pics/vincenzobot_logo.jpg"
cjb = "./vincenzobot/resources/pics/cjb.jpg"
restlo = "./vincenzobot/resources/pics/rest.jpeg"
shuru = "./vincenzobot/resources/pics/shuru.jpg"
shhh = "./vincenzobot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "RealVincenzo"
my_group = Config.MY_GROUP or "VincenzoSupport"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/RealVincenzo"
vincenzo_channel = f"[Real Vincenzo]({chnl_link})"
grp_link = "https://t.me/VincenzoSupport"
vincenzo_grp = f"[Vincenzo Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# vincenzobot
