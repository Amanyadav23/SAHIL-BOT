from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**ᴘʀᴏꜰꜱꜱɪᴏɴᴀʟ ꜱᴇʀᴠᴇʀ ᴜꜱᴇ ꜰᴏʀ ʜᴏꜱᴛɪɴɢ 

ꜱᴍᴏᴋᴇʀ ᴍᴜꜱɪᴄ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ᴘʀɪᴠᴀᴛᴇ ꜱᴇʀᴠᴇʀ ꜱᴇʀᴠᴇʀ. ꜰᴜᴄᴋᴋ ᴠᴄ ɴᴏ ʟᴀɢ ꜰᴜʟʟ ᴍᴀꜱᴛɪ🎶[🌹| ꜱᴀɴᴋɪ ᴘᴜʙʟɪᴄ |🌹](https://t.me/SankiPublic).

ᴛʜɪꜱ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ꜰɪʀᴇʙᴀꜱᴇ ꜱᴇʀᴠᴇʀ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹ᴏᴡɴᴇʀ ", url="https://t.me/Sanki_Owner")
                  ],[
                    InlineKeyboardButton(
                        "⭐ ꜱᴀɴᴋɪ ᴘᴜʙʟɪᴄ", url="https://t.me/SankiPublic"
                    ),
                    InlineKeyboardButton(
                        "🔊 ᴇꜱᴘᴏʀᴛ ᴏᴘ", url="https://t.me/EsportCheater"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/SmokerMusicRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ɢʀᴏᴜᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ᴏɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ᴏᴡɴᴇʀ", url="https://t.me/Sanki_Owner")
                ]
            ]
        )
   )





