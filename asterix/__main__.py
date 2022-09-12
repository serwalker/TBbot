import asyncio

from pyrogram import idle

from TBbot.clients import app

loop = asyncio.get_event_loop()


async def start_assistant():
    """
    this function starts the pyrogram bot client.
    """
    if app.bot:
        print("Activating assistant.\n")
        await app.bot.start()
        print("Assistant activated.\n")
    else:
        print(
            "Assistant start unsuccessful, please check that you have given the bot token.\n"
        )
        print("skipping assistant start !")


async def start_userbot():
    """
    this function starts the pyrogram userbot client.
    """
    if app:
        print("Activating TBbot.\n")
        await app.start()
        print("TBbot activated.\n")
    else:
        print("Userbot startup unsuccessful, please check everything again ...")
        print("Couldn't load modules of TBbot")


async def start_bot():
    """
    This function uses 'start_assistant' & 'start_TBbot' with
    clients custom 'import_module' to start clients & import modules.
    """
    print(
        "___________________________________. Welcome to TBbot World .___________________________________\n\n\n"
    )
    print("PLUGINS: Installing.\n\n")
    plugins = app.import_module("TBbot/plugins/", exclude=app.NoLoad())
    print(f"\n\n{plugins} plugins Loaded\n\n")
    print("MODULES: Installing.\n\n")
    modules = app.import_module("TBbot/modules/", exclude=app.NoLoad())
    print(f"\n\n{modules} modules Loaded\n\n")
    await start_assistant()
    await start_userbot()
    print("You successfully deployed 💥 TBbot 💥 ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!].")
    await idle()  # block execution


if __name__ == "__main__":
    loop.run_until_complete(start_bot())
