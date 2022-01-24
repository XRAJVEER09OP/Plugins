import inspect
import re

from pathlib import Path
from telethon import events

from .session import V2, V3, V4, V5
from vincenzobot import CMD_LIST, LOAD_PLUG, bot
from vincenzobot.config import Config
from vincenzobot.sql.gvar_sql import gvarstat


def hell_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats
    sudo_user = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for c in a:
            a = int(c)
            sudo_user.append(a)

    if pattern is not None:
        global vincenzo_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            vincenzo_reg = sudo_reg = re.compile(pattern)
        else:
            vincenzo = "\\" + Config.HANDLER
            sudo_ = "\\" + Config.SUDO_HANDLER
            vincenzo_reg = re.compile(vincenzo_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = vincenzo_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (vincenzo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=vincenzo_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=vincenzo_reg))
        if allow_sudo:
            if not disable_edited:
                bot.add_event_handler(func, events.MessageEdited(**args, from_users=sudo_user, pattern=sudo_reg))
            bot.add_event_handler(func, events.NewMessage(**args, from_users=sudo_user, pattern=sudo_reg))
        if V2:
            if not disable_edited:
                V2.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=vincenzo_reg))
            V2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=vincenzo_reg))
        if H3:
            if not disable_edited:
                V3.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=vincenzo_reg))
            V3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=vincenzo_reg))
        if V4:
            if not disable_edited:
                V4.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=vincenzo_reg))
            V4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=vincenzo_reg))
        if V5:
            if not disable_edited:
                V5.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=vincenzo_reg))
            V5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=hell_regvincenzo_reg
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def hell_handler(
    **args,
):
    def decorator(func):
        bot.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if V2:
            V2.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if V3:
            V3.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if V4:
            V4.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if V5:
            V5.add_event_handler(func, events.NewMessage(**args, incoming=True))
        return func

    return decorator
