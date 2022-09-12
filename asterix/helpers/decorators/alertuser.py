from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery


class AlertUser(object):
    def alert_user(self, func):
        async def wrapper(_, cb: CallbackQuery):
            if cb.from_user and not (
                cb.from_user.id == self.id or cb.from_user.id in self.SudoUsers()
            ):
                await cb.answer(
                    f"Sorry, but you can't use this userbot ! make your own TBbot at @Oh_ken",
                    show_alert=True,
                )
            else:
                try:
                    await func(_, cb)
                except MessageNotModified:
                    pass

        return wrapper
