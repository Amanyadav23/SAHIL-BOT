
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**✨𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗣𝗼𝘄𝗲𝗿 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁\n💕𝗙𝗲𝗲𝗹 𝗡𝗼 𝗟𝗮𝗴 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗩𝗼𝗶𝗰𝗲-𝗖𝗵𝗮𝘁 \n🌴𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲 𝗢𝗳 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 [𝗖𝗹𝗶𝗰𝗸](https://t.me/Prayagraj_Op)\n🌱𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 [𝗛𝗲𝘅𝗼𝗿](https://t.me/Its_Hexor)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/Sanki_Owner")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url="https://t.me/Sanki_BOTs_Support"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/Prayagraj_Op"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝗖𝗼𝗺𝗺𝗮𝗱𝘀❱", url="https://telegra.ph/%EA%9C%B1%E1%B4%8D%E1%B4%8F%E1%B4%8B%E1%B4%87%CA%80-%E1%B4%8D%E1%B4%9C%EA%9C%B1%C9%AA%E1%B4%84-%CA%99%E1%B4%8F%E1%B4%9B-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85%EA%9C%B1-08-29"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗛𝗲𝘅𝗼𝗿'𝘅𝗗 𝗢𝗻𝗹𝗶𝗻𝗲🎶**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔈𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/SankiPublicEnjoy")
                ]
            ]
        )
   )
