import telethon.utils

from telethon.tl.functions.users import GetFullUserRequest

from .session import Vincenzo, V2, V3, V4, V5
from vincenzobot.sql.gvar_sql import gvarstat


async def clients_list(Config, Vincenzo, V2, V3, V4, V5):
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await Vincenzo.get_me()
    user_ids.append(main_id.id)

    try:
        if V2 is not None:
            id2 = await V2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if V3 is not None:
            id3 = await V3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if V4 is not None:
            id4 = await V4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if V5 is not None:
            id5 = await V5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        XD_RAJVEER = uid.user.id
        VINCENZO_USER = uid.user.first_name
        hell_mention = f"[{VINCENZO_USER}](tg://user?id={XD_RAJVEER})"
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        XD_RAJVEER = uid
        VINCENZO_USER = client.first_name
        hell_mention = f"[{VINCENZO_USER}](tg://user?id={XD_RAJVEER})"
    return XD_RAJVEER, VINCENZO_USER, vincenzo_mention
