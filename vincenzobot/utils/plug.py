import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from vincenzobot import *
from vincenzobot.clients import *
from vincenzobot.helpers import *
from vincenzobot.config import *
from vincenzobot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from vincenzobot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import vincenzobot.utils

        path = Path(f"vincenzobot/plugins/{shortname}.py")
        name = "vincenzobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Vincenzobot - Successfully imported " + shortname)
    else:
        import vincenzobot.utils

        path = Path(f"vincenzobot/plugins/{shortname}.py")
        name = "vincenzobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Vincenzo
        mod.V1 = Vincenzo
        mod.V2 = V2
        mod.V3 = V3
        mod.V4 = V4
        mod.V5 = V5
        mod.Vincenzo = Vincenzo
        mod.Vincenzobot = Vincenzobot
        mod.tbot = Vincenzobot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = vincenzobot.utils
        mod.Config = Config
        mod.borg = bot
        mod.vincenzobot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.vincenzo_cmd = vincenzo_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = vincenzobot.utils
        sys.modules["userbot"] = vincenzobot
        # support for paperplaneextended
        sys.modules["userbot.events"] = vincenzobot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["vincenzo.plugins." + shortname] = mod
        LOGS.info("⚡ 𝓥𝓘𝓝𝓒𝓔𝓝𝓩𝓞𝓑𝓞𝓣 ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"vincenzo.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

# vincenzobot
